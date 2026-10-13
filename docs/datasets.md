# Public fundus datasets for supervised learning (1-b)

> 목적: 안저사진 **지도학습(supervised learning)**에 쓸 수 있는 공개 데이터셋 카탈로그와
> GPU 없는 환경에서의 현실적 실험 계획. 각 항목은 접근 방식(open / registration / request)을
> 구분했다. 수치는 데이터셋 공식 문서 기준이며, 실제 사용 전 **원 논문/다운로드 페이지에서 최신 수치를 확인**할 것.
>
> 주의: 대부분 **research / non-commercial 용도**로만 허용된다. 라이선스와 이용약관은 배포처에서 확인.

---

## 1. 한눈에 보는 추천 (CPU 실험 시작용)

| 우선순위 | 데이터셋 | 과제 | 규모 | 접근 | 이유 |
|---|---|---|---|---|---|
| 1 | **APTOS 2019** | DR 5단계 분류 | 3,662장 | Kaggle(무료 계정) | 깨끗하고 라벨 명확, 빠른 반복 실험 |
| 2 | **IDRiD** | DR 등급+병변분할 | 516장 | open (Grand Challenge) | 병변 픽셀 라벨 → localization 연구 |
| 3 | **Messidor-2** | DR 분류 | 1,748장 | open | 국제 표준 비교 기준 |
| 4 | **RFMiD 2.0** | 다질환(45클래스) | 3,200장 | open (Nature Data) | 다질환 multi-label, 검진 소견에 근접 |
| 5 | **ACRIMA / ORIGA / REFUGE** | 녹내장 | 705 / 650 / 1,200 | open | 녹내장 축 소규모 벤치 |
| 6 | **ODIR-2019** | 8질환 다중라벨 | 10,000장(5,000명) | open | 다질환, 양안 paired |

> 전략: **소규모·고품질 데이터로 파이프라인을 먼저 고정**한 뒤, EyePACS/AIROGS 같은 대규모로 확장.

---

## 2. 당뇨망막병증 (Diabetic Retinopathy)

| 데이터셋 | 규모 | 라벨 | 접근 | 링크 |
|---|---|---|---|---|
| **EyePACS (Kaggle DR)** | ~88,702장 | DR 0–4 (5단계) | Kaggle 등록 | kaggle.com/c/diabetic-retinopathy-detection |
| **APTOS 2019** | 3,662장 | DR 0–4 | Kaggle 등록 | kaggle.com/c/aptos2019-blindness-detection |
| **Messidor-2** | 1,748장 | DR 등급 + DME | open | ADCIS / 원 배포처 |
| **IDRiD** | 516장 | DR 등급 + 병변/landmark 분할 | open | idrid.grand-challenge.org |
| **DDR** | 13,673장 | DR 등급 + 병변 | request | (중국) 원 논문 배포처 |
| **DeepDRiD** | 2,000장(500명) | DR 등급 | open | deepdrdiag.ie |
| **DiaRetDB1 / E-Ophtha / DRiDB** | 소규모 | DR 병변 | open | 각 배포처 |
| **MAPLES-DR** | 198장(고해상) | DR/DME 병변 재라벨 | open | 원 논문 |
| **BRSET** | ~16,000장 | 다중라벨(DR 포함) | open | Brazilian, 피부색 다양성 |
| **UWF-DR (2026)** | 1,630장 | Normal/NPDR/PDR | open (Figshare) | 초광각(200°) DR |
| **MMRDR** | multimodal | CFP+OCT+UWF | open | 다중모달 |

## 3. 녹내장 (Glaucoma)

| 데이터셋 | 규모 | 라벨 | 접근 | 링크 |
|---|---|---|---|---|
| **AIROGS / EyePACS-AIROGS** | 101,442장 | referable glaucoma | open(Grand Challenge) | airogs.grand-challenge.org |
| **ORIGA-light** | 650장 | 녹내장 + CDR/OC/OD | open | Kaggle/배포처 |
| **REFUGE / REFUGE2** | 1,200장 | 분류+유두/황반 분할 | 등록 | refuge.grand-challenge.org |
| **ACRIMA** | 705장 | 정상/녹내장 | open | Figshare |
| **RIM-ONE (r1–r3/DL)** | ~485장 | 녹내장 | open | medimrg.webs.ull.es |
| **DRISHTI-GS** | 101장 | 유두/컵 분할 | open | cvit.iiit.ac.in |
| **G1020** | 1,020장 | 녹내장 + 유두/컵 | 등록 | Kaggle |
| **GAMMA** | 다수 | 녹내장 grading + 유두/컵 | 등록 | gamma.grand-challenge.org |
| **PAPILA** | 488장 | 녹내장 + 임상데이터(양안) | open | Figshare / Sci Data |
| **JustRAIGS** | ~101,767장 | referable glaucoma grading | 공모전 | justraigs.grand-challenge.org |
| **HYGD (Hillel Yaffe)** | - | 녹내장 + 화질 | open | PhysioNet |

## 4. 황반변성 / 다질환 / 기타

| 데이터셋 | 규모 | 라벨 | 접근 | 링크 |
|---|---|---|---|---|
| **ODIR-2019** | 10,000장(5,000명) | 8질환 다중라벨 | open | odir2019.grand-challenge.org |
| **iChallenge-AMD** | 400장 | AMD 등급 | open | iChallenge-AMD |
| **iChallenge-PM (병적근시)** | 1,200장 | PM 등급 | open | iChallenge-PM |
| **RFMiD 1.0 / 2.0** | 3,200장 | 45개(빈도+희귀) 질환 | open | Nature Sci Data |
| **Harvard-EF30k** | 30,000장 | 녹내장/AMD/DR | request | ophai.hms.harvard.edu |
| **FIVES** | 800장 | 질환 + 혈관분할 | open | Figshare |
| **ROSE** | 320장 | 혈관/AMD/기타 | open | Mendeley |
| **JSIEC-1000 (OIA-ODIR)** | 1,000장 | 8그룹 | 등록 | Kaggle |
| **KEH (Kim's Eye Hospital)** | - | 다중라벨(한국) | open | Harvard Dataverse (doi:10.7910/DVN/1YRRAC) |
| **STARE / DRIVE / CHASE_DB1 / HRF** | 소규모 | 혈관분할 | open | 각 배포처 |

## 5. foundation model / 사전학습 가중치 (전이학습용)

지도학습 성능을 끌어올리려면 사전학습 백본을 쓴다. 특히 **SSM 계열**을 우선 검토.

| 모델 | 설명 | 링크 |
|---|---|---|
| **RETFound** | 안저(OCT) self-supervised foundation model | github.com/rmaphoh/RETFound_MAE |
| **Vision Mamba (Vim)** | bidirectional SSM 비전 백본, 선형 복잡도 | github.com/hustvl/Vim |
| **VMamba** | cross-scan 기반 SSM 백본 | github.com/MzeroMiko/VMamba |
| **MedMamba** | 의료영상용 hybrid SSM, 경량 | github.com/YubiaoYue/MedMamba |
| **LEMUR** | RETFound를 VMamba로 **증류한 초경량** 안저 모델 | github.com/andregdmitri/LEMUR |
| **StageMamba** | EfficientNet-B4 + Mamba, 10질환 다중분류 | github.com/Rizzwanth/StageMamba |

> **LEMUR**가 이 프로젝트 목표(CPU 친화 + 안저 특화)에 가장 부합. RETFound teacher를
> 경량 VMamba student로 증류 → 추론 비용 절감. IDRiD/APTOS/Messidor/PAPILA를 지원한다.

---

## 6. GPU 없는 환경에서의 실험 계획

1. **해상도 축소 + 소형 백본**: 512×512 또는 384×384 입력, 백본은 경량(MobileNet/EffNet-B0 또는
   distilled VMamba). 배치 작게, gradient accumulation.
2. **선형 프로빙(linear probe) 우선**: frozen backbone + 단일 linear head만 학습 → CPU에서도 빠름.
3. **증류/프루닝**: LEMUR 파이프라인처럼 teacher→student 증류로 파라미터·FLOPs 축소.
4. **데이터 순서**: APTOS(파이프라인) → IDRiD(병변) → RFMiD(다질환) → ORIGA/REFUGE(녹내장) → 확장.
5. **leakage 방지(매우 중요)**: 같은 환자의 좌/우안이 train·test에 나뉘지 않도록 **환자 단위 split**.
   EyePACS/APTOS/ODIR은 양안 존재 → 반드시 환자 ID 기반 분할. (문헌에서 성능 과대평가의 주원인)
6. **평가**: 질환별 민감도/특이도, AUC, calibration. 검진 목적상 **민감도(recall) 우선** + 불필요 의뢰 관리.
7. **도메인 shift**: 카메라/인종/조명 차이가 큼. 외부 검증셋(BRSET, KEH, RFMiD)으로 일반화 확인.
8. **클래스 불균형**: 희귀 병변은 focal loss / 재샘플링. normal vs abnormal 이진 분류부터 시작 권장.

## 7. 한국 검진 맥락 메모

- 국가건강검진에서 **당뇨병 환자는 매년 당뇨병 눈검사(안저검사)** 대상 → DR 스크리닝이 1차 목표.
- 검진에서 흔한 병적 소견: DR, 고혈압망막병증, AMD, 녹내장 의심, 근시성 변화 (→ §문서
  `fundus-common-findings-and-red-flags.md`).
- 한국/아시아 데이터는 상대적으로 부족 → KEH, 필요 시 자체 수집(비식별화) 고려.

## 8. 참고문헌 / 카탈로그

1. Conquer V, et al. Comprehensive Review of Open-Source Fundus Image Databases for DR Diagnosis. 2025.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC12473202/
2. Fatima Z, Dhaliwal P, Gupta DK. A comprehensive review of retinal disease diagnosis and open access
   datasets: Fundus and OCT images. 2024. https://exa.ai/library/publication/6lkhc5qlnfb
3. Krzywicki T, et al. A Global Review of Publicly Available Datasets Containing Fundus Images.
   *J Clin Med*. 2023;12(10):3587. doi:10.3390/jcm12103587
4. Awesome-Ophthalmology-Dataset (curated list) https://github.com/NanxuGong/Awesome-Ophthalmology-Dataset
5. Glaucoma dataset metadata catalog https://github.com/TheBeastCoding/glaucoma-dataset-metadata
6. LEMUR (Mamba distillation for retina) https://github.com/andregdmitri/LEMUR
7. MedMamba https://arxiv.org/html/2403.03849v4
8. Vision Mamba (ICML 2024) https://proceedings.mlr.press/v235/zhu24f.html
9. Peng S, et al. A fundus image dataset for intelligent diabetic retinopathy system. *Sci Data* 13:777 (2026).
   doi:10.1038/s41597-026-07093-7

---
*문서 버전: v0.1 · 수치는 공식 문서 기준이며 사용 전 재확인 필요*
