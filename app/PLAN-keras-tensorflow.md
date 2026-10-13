# 안저 AI 앱 — Keras / TensorFlow 구현 계획 (v0.2)

> 상태: **계획만** (구현 미착수). 기존 PyTorch 스켈레톤은 프레임워크를 Keras/TF로 확정하며 제거.
> 이 문서는 “Keras/TF로 만든다면 어떻게 만들지”의 설계도이자 **의사결정 기록**이다.
>
> 목표: State Space Model(vision mamba 등) 기반, **GPU 없는 환경**에서 실험·추론 가능,
> 건강검진에서 흔한 소견을 우선 판독.
>
> 이 문서는 **의료진 학습·개발 참고용**이며, 결과물은 진단 보조(Clinical Decision Support)로 명시한다.

---

## 1. 요약과 핵심 결정

| 항목 | 결정 | 근거 |
|---|---|---|
| 프레임워크 | TensorFlow 2.x + Keras 3 (TF 백엔드) | TFLite CPU 배포, tf.data, 콜백 생태계 |
| 아키텍처 방향 | 하이브리드 CNN + SSM (전략 A) | 국소+전역 동시, 선형 복잡도 |
| 안전판 | KerasHub 사전학습 백본 (전략 B) | SSM 구현 리스크 회피, 비교 기준선 |
| 최초 태스크 | `normal vs abnormal` 이진 분류 | 검진 1차 선별에 부합, 데이터 요구 적음 |
| 입력 해상도 | 224×224 (기본), tiny preset 64×64 | CPU 학습/추론 비용 |
| 배포 형태 | TFLite (float16/int8) + FastAPI | GPU 불필요 |
| 불변 규칙 | **환자 단위 split**, 라벨=문서 소견 목록과 동기화 | 데이터 누수·정의 불일치 방지 |

### 아직 결정하지 않은 것 (Open decisions)

1. SSM 구현: `tf.scan` vs 청크 병렬 스캔 중 어느 것을 기본으로 갈지 — M1 실측 후 결정.
2. 전략 A vs B 최종 채택 — M5 비교표 후 결정.
3. 다질환을 multi-class로 갈지 multi-label로 갈지 — M3 데이터 확보 후 결정.
4. 증류(LEMUR식) 도입 여부 — A/B 성능·지연 확인 후.
5. 외부 검증셋 우선순위(RFMiD vs KEH vs BRSET).

---

## 2. 전략 결정 매트릭스 (Go / No-Go 게이트)

```
        ┌───────────────────────────────────────────────┐
        │  전략 B (KerasHub 백본) 먼저 → 베이스라인 확보  │
        └───────────────┬───────────────────────────────┘
                        │  M4: val AUC 보고
                        ▼
        ┌───────────────────────────────────────────────┐
        │  전략 A (하이브리드 CNN+SSM) 구현·학습         │
        └───────────────┬───────────────────────────────┘
                        │  M5: B 대비 성능·지연 비교
        ┌───────────────┴───────────────┐
        ▼                               ▼
 A가 B 이상 or 지연 유리        A가 B보다 현저히 열등/불안정
 → A 채택                       → B 유지, A는 연구 브랜치로
```

| 전략 | 내용 | 리스크 | 채택 조건 |
|---|---|---|---|
| A 하이브리드 SSM | MedMamba식 SS-Conv-SSM | 커스텀 레이어 정확성/속도 | M5에서 AUC 동등 이상 & CPU 지연 허용 |
| B KerasHub 백본 | EffNet/ViT 전이학습 | 도메인 시프트 | 항상 베이스라인으로 유지 |
| C SSM 가중치 이식 | VMamba/Mamba pretrained 매핑 | 매핑 시간 큼 | A/B 모두 부족할 때만 |

**No-Go 기준**: M1에서 SSM 수치 불일치가 해결 안 되거나, CPU 지연이 허용치(예: 단일 이미지 목표)를 크게 초과하면 전략 A를 접고 B로 간다.

---

## 3. SSM 구현 심화 (핵심 기술 리스크)

### 3.1 이산화 수식 (구현 기준)

연속 SSM `h'(t)=A h(t)+B x(t), y(t)=C h(t)+D x(t)` 를 영차홀드로 이산화:

- `Ā = exp(Δ·A)`, `B̄ = Δ·B`
- 재귀: `h_t = Ā_t ⊙ h_{t-1} + B̄_t ⊙ x_t`, `y_t = C_t · h_t + D ⊙ x_t`
- Mamba의 selective 특성: `Δ, B, C`가 입력에 따라 변함(time-varying).

### 3.2 구현 3안과 트레이드오프

| 구현 | 정확성 | 속도(CPU) | 병렬화 | 용도 |
|---|---|---|---|---|
| ① 참조 `for t` 루프 | 기준(정답) | 매우 느림 | 불가 | **정확성 검증 전용** |
| ② `tf.scan` | 동일 | 중간 | 부분 | 기본 후보 |
| ③ 청크/associative scan (Blelloch) | 동일 | 빠름 | 높음 | 최적화 단계 |
| ④ XLA(`jit_compile=True`) 융합 | 동일 | 향상 | - | ②③에 적용 |

**기본 계획**: ①을 테스트 오라클로 두고 ②를 기본 구현으로. 지연이 병목이면 ③으로 승격.

### 3.3 정확성·안정성 가드레일 (필수)

- 파라미터화: `A = -exp(A_log)`, `Δ = softplus(dt)` → 수치 안정.
- **수치 일치 테스트**: ①vs② 최대 절대오차 `< 1e-5` (float32)를 **CI 게이트**로.
- **기울기 테스트**: `tf.GradientTape`로 유한차분 대비 기울기 방향 검증.
- **초기화**: `dt_proj` bias를 log-uniform 범위로 초기화(Mamba 관례).
- **결정성**: CPU에서도 일부 op 비결정 가능 → seed 고정 + `TF_DETERMINISTIC_OPS` 문서화.

### 3.4 레이어/모델 스펙 (구현 시 채울 값)

| preset | img_size | patch | dim | depth | d_state | 예상 파라미터* | 용도 |
|---|---|---|---|---|---|---|---|
| tiny | 64 | 8 | 32 | 2 | 8 | 수백 K | 단위테스트/합성 |
| small | 128 | 8 | 64 | 4 | 16 | 수 M | CPU 실험 |
| base | 224 | 16 | 96 | 6 | 16 | 수십 M | 성능 상한 |

\* 파라미터 수는 **M0에서 실측**해 채운다(추정치를 문서에 확정 수치로 적지 않음).

---

## 4. 아키텍처 (전략 A)

```
입력 안저 224×224×3
   │
Conv Stem (Conv2D patch, stride)          ← 국소 특징
   │  + learnable positional embedding
   │
┌── SS-Conv-SSM Block × N ────────────────┐
│  LayerNorm                              │
│  channel split ─┬─ Conv 브랜치(dw conv)  │  국소
│                 └─ SSM 브랜치(Bi selective scan)  전역, O(L)
│  concat → channel shuffle → residual    │
└─────────────────────────────────────────┘
   │
Global Average Pooling
   │
Dropout → Dense(head, n_classes, softmax)
```

- 양방향(bi-directional) SSM으로 시퀀스 방향 민감성 완화(Vim 취지).
- 분류 head만 교체하면 태스크 전환(binary→DR 등급→multi-label) 가능.
- (선택) BCE vs CE: multi-label이면 sigmoid+BCE, 단일 등급이면 softmax+CE.

---

## 5. 데이터 파이프라인 (tf.data)

```
CSV(index, image, label, patient_id, eye)
   │
tf.data.Dataset.from_tensor_slices
   │ map(decode_jpeg → resize → normalize)  (num_parallel_calls=AUTOTUNE)
   │
   ├─ train: RandomFlip · RandomRotation · RandomContrast · RandomBrightness
   │         (선택) MixUp/CutMix, CircleCrop(검은 테두리 제거)
   └─ val/test: 결정적 전처리만
   │
shuffle(buffer) → batch(32) → cache()/prefetch(AUTOTUNE)
```

**환자 단위 split**: `patient_id` 기준 GroupShuffleSplit(자체 구현 또는 sklearn). 양안이 train/test에 섞이면 성능 과대평가.

**불균형 처리**: `class_weight`(빈도 역수) 또는 focal loss(γ=2 권장 시작). 검진 목적상 소수(질환) 클래스 recall 우선.

**라벨 정의 동기화**: `docs/fundus-common-findings-and-red-flags.md` 소견 목록과 코드 `labels.py`를 1:1 대응. 태스크:
- `normal_abnormal` (binary, 1차)
- `dr_icdr` (5등급)
- `glaucoma` (3)
- `multi_finding`, `redflag_binary`

---

## 6. 평가 프로토콜 (검진 목적에 맞춤)

| 항목 | 방법 |
|---|---|
| 판별력 | ROC-AUC, PR-AUC(불균형 시) |
| 운영점 | **고정 특이도에서 민감도**(예: spec 90%에서 sens) — 임계값을 사전 지정 |
| 임상 지표 | 혼동행렬, PPV/NPV(유병률 가정 하), F1 |
| 보정 | reliability diagram + ECE, temperature scaling |
| 불확실성 | MC-dropout 분산 또는 예측 엔트로피 |
| 하위군 | 나이/성별/카메라/화질별 성능 감사(subgroup audit) |
| 외부 검증 | RFMiD/KEH/BRSET 등 다른 분포에서 재평가 |

> 검진에서는 **민감도(recall)** 를 우선하되, 불필요 의뢰 비용을 특이도로 관리한다.

---

## 7. 재현성 · 실험 관리

- seed 고정(파이썬/넘파이/TF), 데이터 split 고정 파일로 저장.
- 환경 고정: `requirements.txt` + 파이썬/패키지 버전 명시.
- 기록: TensorBoard(오프라인 가능) + 실험 config(yaml)와 체크포인트 함께 저장.
- 모든 수치는 스크립트로 재생성 가능해야 함(노트북은 탐색용, 최종은 스크립트).

---

## 8. CPU 추론 / 배포

1. **TFLite 변환**: `TFLiteConverter.from_keras_model`.
2. **양자화**:
   - `float16`: 크기 절반, 정확도 손실 적음, CPU에서 제한적 이득.
   - `int8`: 대표 데이터셋(수백 장) 필요, 크기·지연 최소. **정확도 하락 검증 필수**.
3. **지연 벤치**: TFLite 인터프리터로 단일/배치 지연, 메모리 측정 → 목표 설정.
4. **서빙**: FastAPI + TFLite(CPU). 모바일은 동일 TFLite 재사용.
5. **전/후처리 일관성**: `config.yaml`로 resize/normalize/임계값을 학습·추론이 공유.
6. **모델 카드**: 학습 데이터, 라벨 정의, 성능, 한계, 의도된 사용(CDS), 금기(단독 진단 불가) 명시.

---

## 9. 테스트 전략

| 테스트 | 대상 | 통과 기준 |
|---|---|---|
| 수치 일치 | SelectiveScan 참조 vs tf.scan | 최대오차 < 1e-5 |
| 기울기 | Tape vs 유한차분 | 방향 일치, 상대오차 허용범위 |
| 형태 | 각 레이어/모델 입출력 | shape 어서션 |
| 파이프라인 | tf.data 증강/배치/split | 형태·라벨 보존, 누수 없음 |
| 스모크 학습 | 합성 데이터 2 epoch | loss 감소, 체크포인트 저장/복원 |
| 추론 | 저장→로드→단일 이미지 | 클래스/확률 출력, 결정성 |

---

## 10. 규제 · 거버넌스 (한국 맥락)

- 환자 데이터: **개인정보보호법**상 가명/익명 처리, 학습용 비식별화. 원본 안저사진은 민감정보.
- 의료기기 해당성: 진단 보조로 실사용 시 **식약처 SaMD(의료기기 소프트웨어)** 허가 검토 필요.
  - 연구 단계는 IRB/윤리 검토, 상용화 전 인허가 로드맵 수립.
- 표시: 사용자에게 **AI 보조 판독**임을 명시, 최종 판단은 의료인.
- 데이터셋 라이선스: 대부분 research-only → 상용 전 재확인.

---

## 11. 범위 밖 (우리가 하지 않는 것)

- 완전 자율 진단(의료인 개입 없는 단독 판정) — 하지 않음.
- 초광각·OCT 등 추가 모달리티(1차는 color fundus만).
- 대규모 분산 학습, 자체 데이터 수집 파이프라인(필요 시 별도 계획).
- 웹 프론트엔드 고도화(1차는 로컬 추론 데모까지).

---

## 12. 마일스톤과 수용 기준

| 단계 | 내용 | 수용 기준 (Acceptance) | 거친 추정* |
|---|---|---|---|
| M0 | TF/Keras 설치, 환경 확인, preset 실측 | `import tensorflow` OK, 파라미터 표 확정 | 0.5일 |
| M1 | SelectiveScan + SSBlock + **수치 일치 테스트** | 참조 대비 오차 < 1e-5, 기울기 테스트 통과 | 2–3일 |
| M2 | 합성 데이터 end-to-end 학습 | loss 감소, 저장/복원 재현 | 1일 |
| M3 | tf.data 파이프라인 + 증강 + 환자 split | 대규모 CSV 로딩, 누수 테스트 통과 | 2일 |
| M4 | APTOS 이진 베이스라인(전략 B) | val AUC·민감도/특이도 리포트 | 2–3일 |
| M5 | 전략 A 학습 + B와 비교 | 비교표(성능·지연), 재현 스크립트 | 3–5일 |
| M6 | TFLite 변환 + 양자화 + 지연 벤치 | 단일 이미지 지연 수치, 정확도 하락 허용범위 내 | 2일 |
| M7 | 외부 검증 + 캘리브레이션 | 외부 AUC·ECE, 하위군 감사 | 3–5일 |
| M8 | FastAPI/TFLite 추론 데모 | 로컬 추론 동작, 모델 카드 첨부 | 2일 |

\* 일정은 **거친 추정**이며 하드웨어·데이터 접근에 좌우된다. 순서는 의존성 순.

**의존**: 데이터 확보는 `docs/datasets.md`(APTOS→IDRiD→RFMiD→녹내장) 순.

---

## 13. 리스크 레지스터

| 리스크 | 확률 | 영향 | 대응 |
|---|---|---|---|
| TF selective scan 느림 | 중 | 중 | ②→③→XLA 단계적 최적화, B로 폴백 |
| SSM 수치 불안정 | 중 | 높음 | log-A/softplus, 수치 일치 테스트 게이트 |
| CPU 학습 지연 | 높음 | 중 | tiny/small, 저해상도, 선형 프로빙, 증류 |
| 양안 데이터 누수 | 높음 | 높음 | patient_id split + 코드 리뷰 체크리스트 |
| 도메인 시프트 | 높음 | 높음 | 외부 검증, 색/조명 증강, 캘리브레이션 |
| 라벨 정의 불일치 | 중 | 높음 | 문서↔코드 단일 소스, 라벨 리뷰 |
| 라이선스/규제 | 중 | 높음 | research-only 준수, 인허가 로드맵 |

---

## 14. 참고

- MedMamba (SS-Conv-SSM, arXiv:2403.03849) — 하이브리드 블록 설계 근거
- Vision Mamba / VMamba — 양방향 SSM 비전 백본(전략 C)
- LEMUR — RETFound→VMamba 증류(경량화 아이디어)
- TensorFlow `tf.scan`, `tf.while_loop`, XLA, TFLite quantization 문서
- 데이터/소견 정의: `docs/datasets.md`, `docs/fundus-common-findings-and-red-flags.md`

---
*문서 버전: v0.2 · 계획/의사결정 문서 (구현 미착수)*
