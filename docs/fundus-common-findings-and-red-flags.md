# 안저검사 흔한 소견 & Red Flag 정리 (Fundoscopy: common findings & red flags)

> 문서 목적: 건강검진·외래에서 안저사진/안저검사로 마주치는 **흔한 소견**과 반드시 놓치면 안 되는
> **red flag sign**을 정리한 참조문서. `1-a` 요구사항에 따라 모든 이미지는 **크롭하지 않은** 원본 전체이며
> 출처/라이선스는 §7에 정리했다. 향후 AI 앱 태스크(라벨 설계, 클래스 정의)와 학습자료 슬라이드의 근거자료로 쓴다.
>
> 주의: 이 문서는 의료진용 학습·개발 참고자료이며, 개별 환자 진단/치료 지침이 아니다. 판독 및 최종 판단은
> 안과 전문의 또는 면허 있는 임상의의 책임이다.

---

## 0. 30초 요약 (TL;DR)

- 안저 판독 순서는 **적색반사 → 시신경유두(Disc) → 황반(Macula) → 혈관(Vessels) → 주변부(Periphery)**.
- 검진에서 가장 흔한 병적 소견: **당뇨망막병증, 고혈압망막병증, AMD, 근시성 변화, 녹내장 의심 소견**.
- 그보다 더 흔한 것은 **병적으로 오인되는 정상 변이**(유두드루젠, 수초섬유, 경사유두, 맥락막모반).
- **놓치면 실명/사망으로 이어지는 red flag**: 양안 시신경유두부종(papilledema), 망막박리/열공,
  망막동맥폐쇄, 망막중심정맥폐쇄, 유리체출혈, 악성고혈압 안저, 신생혈관(PDR/NVG), 소아 백색동공.
- 정상 변이와 red flag를 구분하는 것이 검진 안저판독의 핵심 역량이다.

---

## 1. 판독 기본: 정상 안저 해부와 판독 순서

정상 안저는 다음 4개 구조로 나누어 체계적으로 본다. 순서를 고정하면 "안 보이는 소견"이 줄어든다.

| 구조 | 정상 소견 | 이상 시 의심 |
|---|---|---|
| 시신경유두 (optic disc) | 분홍빛, 경계 명확, C/D 비 ≤ 0.5, 신경망막테두리(rim) 균일 | 부종, 창백, 함몰 증가(CDR↑), 유두출혈 |
| 황반 (macula) | 중심와(fovea)보다 어둡고 무혈관, 반사 정상 | 삼출물, 출혈, 부종, 드루젠, 막 |
| 혈관 (vessels) | 동맥:정맥 굵기비 ≈ 2:3, 정맥 자연박동, 규칙적 주행 | 협착, 굴곡, 염주상, 폐쇄, 색전 |
| 배경망막 (background) | 균일한 주황색, 병변 없음 | 출혈, 견과반점, 색소변화, 위축 |

기본 용어:
- **C/D ratio**: optic cup / optic disc 직경비. 좌우 차이 > 0.2 또는 CDR ≥ 0.6~0.7이면 녹내장 의심.
- **A/V ratio**: 동맥/정맥 직경비. 정상 ≈ 0.66. 0.5 이하이면 동맥협착.
- **ISNT rule**: 신경망막테두리 두께는 Inferior > Superior > Nasal > Temporal 순으로 두꺼운 것이 정상.
- **자연정맥박동(spontaneous venous pulsation)**: 존재하면 두개내압 상승을 배제하는 데 유용(단, 소실이
  곧 상승을 의미하지는 않음).

### 1.1 적색반사 (Red reflex)

- 검사법: 약 60cm 거리에서 검안경 빛을 눈에 비춘다. 망막에서 반사된 붉은 빛이 보인다.
- 정상: 선명한 주황-적색 반사, **양안 대칭**.
- 매체(각막·수정체·유리체)가 투명해야 보이므로, 반사 이상은 매체혼탁의 신호다.

| 이상 소견 | 먼저 의심 |
|---|---|
| 반사 소실/혼탁 | 백내장, 각막혼탁 |
| 검붉음/어두움 | 유리체출혈, (큰) 망막박리 |
| 흰색 반사(leukocoria) | 소아 망막모세포종, 선천백내장 |
| 좌우 비대칭 | 사시, 안구내 종양 |

> "들여다볼 수 없으면 환자도 못 본다." 안저가 안 보이면 매체혼탁부터 평가한다.
> 검안경/안저사진 예시는 `slides/figures/red-reflex.svg` 참조.

### 1.2 판독 지표의 정의와 이상 시 우선 의심

| 지표 | 정의 | 정상 | 이상 시 먼저 의심 |
|---|---|---|---|
| **C/D ratio** | 컵(cup) 직경 ÷ 유두(disc) 직경 | ≤ 0.5, 좌우 차 < 0.2 | ≥ 0.6~0.7 또는 좌우 차 ≥ 0.2 → **녹내장** |
| **ISNT rule** | 테두리 두께 순서: I > S > N > T | 아래(I)가 가장 두꺼움 | 순서 위반·테두리 패임 → **녹내장** |
| **A/V ratio** | 동맥/정맥 굵기비 | ≈ 2:3 (0.66) | ≤ 0.5 → **고혈압망막병증**, 동맥경화 |
| **AV crossing** | 동정맥 교차부 정맥 압박 | 부드럽게 통과 | AV nicking → 고혈압/동맥경화 |
| **유두 경계** | 시신경유두 테두리 선명도 | 명확 | 흐림/융기 → **유두부종(두개내압↑)**. 양안=두개내압, 편측=시신경병증 |
| **황반** | 중심와 무혈관 여부 | 무혈관, 정상 반사 | AMD · DME · 망막전막 · CSCR |
| **배경망막** | 균일성 | 균일한 주황색 | 출혈 · 견과반점 · 색소변화 |

- 도해(스키매틱 그림): `slides/figures/fundus-anatomy.svg`, `cd-ratio.svg`, `av-ratio.svg`, `isnt-rule.svg`.
- 핵심: **유두 경계흐림은 양안 여부가 결정적** — 양안이면 두개내압 상승을, 편측이면 시신경병증을 먼저 생각한다.

---

## 2. 건강검진에서 흔한 소견

### 2.1 병적으로 오인되기 쉬운 정상 변이 (pseudopathology)

가장 먼저 익혀야 하는 항목. "이상 소견"으로 오인되어 불필요한 의뢰·검사를 유발한다.

- **유두드루젠 (optic disc drusen)**: 시신경유두 내 칼슘 침착. 경계 흐림·유두 융기로 **유두부종과 오인**한다.
  자가형광·OCT·B-scan 초음파로 감별. 대개 무증상.
- **수초화 신경섬유 (myelinated retinal nerve fibers)**: 유두 주변의 흰 깃털 모양 반점. 양성 소견.
- **경사시신경유두 (tilted disc)**: 유두가 비스듬히 보여 CDR이 커 보이고 시야 결손처럼 보일 수 있음.
- **맥락막 모반 (choroidal nevus)**: 편평한 색소 병변. 두께·orange pigment·drusen·subretinal fluid 여부로
  악성 흑색종과 감별(초음파/OCT).
- **시신경유두 주변 위축(peripapillary atrophy)**, **근시성 시신경 (myopic disc)**: 근시에서 흔함.

> 핵심: 편측성/양측성, 색소 변화, 두께 변화, 신경섬유층 결손, 시야 이상을 함께 보면 변이와 병적을 나눌 수 있다.

### 2.2 당뇨망막병증 (Diabetic Retinopathy, DR)

국가검진에서 **당뇨병 환자는 매년 안저검사** 대상이다. 당뇨병성 망막병증은 성인 실명의 주요 원인이며
초기에는 무증상이다.

**병리 소견 (병변 용어)**
- 미세혈관류 (microaneurysm): 첫 임상 징후.
- 점상/반상 출혈 (dot-blot hemorrhage), 화염상 출혈.
- 경성 삼출물 (hard exudate): 지질침착, 황반부에 배열 시 시력 위협.
- 견과반점 (cotton-wool spot): 국소 신경섬유경색.
- 정맥염주 (venous beading), IRMA (intraretinal microvascular abnormality).
- 신생혈관 (neovascularization, NVD/NVE), 유리체출혈, 섬유혈관증식막, 견인망막박리.
- **당뇨황반부종 (DME)**: 황반 중심 침범 여부가 시력 예후를 좌우.

**ICDR 국제 임상 등급** (Wilkinson 2003) — 참고문헌 [1]

| 등급 | 소견 | 권고 |
|---|---|---|
| No apparent DR | 병변 없음 | 1년 후 재검 |
| Mild NPDR | 미세혈관류만 | 1년 후 재검 |
| Moderate NPDR | 경증 이상이나 severe 기준 미만 | 6개월 후 재검 (또는 의뢰) |
| Severe NPDR | 4-2-1 rule (4사분면 출혈, 2사분면 정맥염주, 1사분면 IRMA) 중 하나 | 안과 의뢰, 2~4개월 |
| PDR | 신생혈관/유리체출혈/전방출혈 | **즉시 안과 의뢰** |

DME는 별도로 "없음 / 비중심와 / 중심와 침범"으로 평가. **중심와 침범 DME는 시력 위협 → 신속 의뢰.**

### 2.3 고혈압망막병증 (Hypertensive Retinopathy)

**Keith-Wagener-Barker (KWB) 등급** — 참고문헌 [2]

| Grade | 소견 |
|---|---|
| 1 | 동맥 협착/경도 경화, AV ratio 감소 |
| 2 | 동맥 초점성 협착, AV crossing change |
| 3 | 출혈, 견과반점, 경성삼출물 (전압성/망막병증) |
| 4 | Grade 3 + **시신경유두부종** (악성 고혈압) |

- **Grade 4 / 유두부종 동반은 악성 고혈압 = 의학적 응급.** 혈압을 수주에 걸쳐 조절하는 것이 아니라
  즉시(수일 내, 필요 시 입원) 조절해야 한다.
- 망막 출혈이 있으면 "accelerated hypertension"으로 재분류된다 — 단순 혈압 수치보다 강한 위험 신호.

### 2.4 연령관련황반변성 (Age-related Macular Degeneration, AMD)

- **건성(dry)**: 드루젠(drusen), 지도상 위축(geographic atrophy). 서서히 진행.
- **습성(wet, nAMD)**: 맥락막신생혈관(CNV) → 망막하출혈, 삼출, 급격한 시력저하. **항VEGF 치료 대상,
  가능한 빨리 의뢰** (치료 지연 시 실명).
- 자가점검: 암슬러(AmSler) 격자. 변시증(metamorphopsia)은 습성 전환의 경고 신호.

### 2.5 녹내장 의심 소견 (Glaucoma suspect)

- CDR ≥ 0.6, 좌우 CDR 차이 ≥ 0.2, 신경망막테두리 패임(notching), **ISNT rule 위반**.
- **국소 신경섬유층 결손(RNFL defect)**: 방사상/쐐기형 어두운 띠.
- **시신경유두 출혈(disc hemorrhage, Drance hemorrhage)**: 진행성 녹내장의 강한 표지.
- 개방각 녹내장은 안압이 정상 범위일 수 있어 안저 유두 소견이 선별의 핵심. 40세 이상 검진에서 특히 중요.

### 2.6 근시성 안저 변화 (Myopic fundus)

- 호랑이무늬(tessellation), 시신경유두 주변 위축, 후포도종(posterior staphyloma).
- **병적 근시**: 황반 위축, lacquer crack, Fuchs spot, 망막하출혈 → 시력저하.
- **연관 위험**: 망막열공/박리, 견인황반증. 굴절 -6D 이상은 고위험군으로 정기 검사.

### 2.7 망막 혈관폐쇄 질환

- **망막분지정맥폐쇄 (BRVO)**: 한 사분면에 출혈·견과반점·부종, 정맥 굴곡. 황반부종 시 시력저하.
- **망막중심정맥폐쇄 (CRVO)**: 전체 망막에 화염상 출혈("blood and thunder"), 정맥 확장·굴곡.
  **허혈성 CRVO는 2~4개월 내 신생혈관녹내장(NVG) 위험** → 정기 추적 필수.
- **망막중심동맥폐쇄 (CRAO)**: 망막 창백 + **벚꽃빨강반점(cherry-red spot)** → **안과적·신경과적 응급**.
- **망막분지동맥폐쇄 (BRAO)**: 국소 백색 망막 부종, 색전 관찰.
- **Hollenhorst plaque (콜레스테롤 색전)**: 혈관 분지부의 반짝이는 황색 색전 → 목동맥/심장 색전원 평가.

### 2.8 그 밖에 흔히 보는 소견

- **망막전막 (epiretinal membrane)**: 황반 표면 반사 증가, 주름, 변시증. 진행 시 의뢰.
- **중심장액망막병증 (CSCR)**: 젊은 남성, 스테로이드/스트레스 관련, 원형 장액망막박리.
- **백내장/매체혼탁**: 적색반사 감소. "들여다볼 수 없으면 환자도 못 본다." 안저가 안 보이면 원인 평가.
- **망막색소변성증 (RP)**: 골세포양 색소침착, 혈관협착, 시신경창백(waxy pallor) 삼징후.

---

## 3. Red Flag Signs (즉시 조치 필요)

> 아래 소견은 "우연히 발견"될 수 있으므로, 검진 판독 시 최우선으로 체크한다.

| Red flag 소견 | 시사하는 상태 | 즉시 조치 | 응급도 |
|---|---|---|---|
| **양안 시신경유두부종** (papilledema: 유두 융기, 경계흐림, 정맥확장, 유두주위 출혈) | 두개내압 상승(종양, VP shunts, 정맥동혈전, IIH, 뇌수막염) | 양안 확인 → **즉시 뇌 MRI/MRV**, 신경과/신경외과 의뢰, 필요 시 LP (영상 후) | 최긴급 |
| **거대세포동맥염 의심 시신경병증** (고령, 시력저하, 턱통증, 두통) | GCA → 실명 위험 | **스테로이드 즉시 시작 후** 안과/류마티스 (조직검사) | 최긴급 |
| **망막박리 / 망막열공** (암막(curtain), 섬광(photopsia), 비문증 급증) | 열공성 망막박리 → 실명 | 즉시 안과 응급 의뢰, 안정/체위 | 최긴급 |
| **망막중심동맥폐쇄** (돌연 무통성 시력소실, 창백+벚꽃빨강반점) | 색전(심장/목동맥), GCA | 즉시 안과+신경과, **급성 뇌졸중 평가**, 색전원 탐색 | 최긴급 |
| **유리체출혈** (갑작스러운 연기/거미줄 시야, 적색반사 소실) | PDR, 망막열공/박리, 외상 | 즉시 안과 의뢰, 통상 파열 열공 확인까지 | 긴급 |
| **신생혈관 (NVD/NVE/NVI, 홍채신생혈관)** | PDR, 허혈성 CRVO, NVG | 즉시 안과 의뢰 (범망막광응고/항VEGF) | 긴급 |
| **망막중심정맥폐쇄 (특히 허혈성)** | NVG·황반부종 위험 | 안과 의뢰 + 정기 추적 (2~4개월) | 준응급 |
| **악성 고혈압 안저 (KWB Gr3–4, 유두부종)** | accelerated/malignant HTN | 즉시 혈압 조절(입원 고려), 내과 협진 | 최긴급 |
| **중심와 침범 황반부종/삼출** | 시력 위협 DME, wet AMD | 안과 의뢰 (항VEGF 등) | 준응급 |
| **Roth spot / 다발성 백색중심 출혈** | 감염성 심내막염, 백혈병 | 전신 평가, 혈액배양/혈액검사, 내과 의뢰 | 긴급 |
| **소아 백색동공(leukocoria) / 비정상 적색반사** | 망막모세포종, 선천백내장 | 즉시 안과 의뢰 | 최긴급 |
| **안구내 종양 의심 (융기 색소병변 + 망막하액)** | 맥락막 흑색종 | 안과 의뢰, 초음파/OCT | 긴급 |
| **급격한 시력저하 + 유두부종/출혈** | 광범위 망막·시신경 병변 | 즉시 안과 | 최긴급 |

참고: 검진용 안저사진은 **단안(mongle)이고 주변부가 일부 가려질 수 있어** 주변부 병변(열공/박리 전구)은
놓칠 수 있다. 증상(비문증, 섬광, 시야 결손)이 있으면 사진이 정상처럼 보여도 의뢰한다.

---

## 4. 이미지 아틀라스 (크롭하지 않은 원본)

각 이미지는 크롭 없이 원본 전체를 사용했다. 출처/라이선스는 §7.

### 4.1 정상 안저 (Normal)

![정상 우안 안저](../assets/images/normal_right_fundus.jpg)

*정상 안저. 시신경유두 경계 명확, 혈관 주행 규칙적, 병변 없음.*

![정상 근시 안저 (OD)](../assets/images/normal_myopic_asian_od.jpg)

*정상 안저(근시, 아시아 남성 23세). 근시성 호랑이무늬가 정상변이로 보임.*

![정상 안저 고해상](../assets/images/normal_od_highres.jpg)

*정상 안저(고해상 원본).*

![경사시신경유두](../assets/images/tilted_disc.jpg)

*경사시신경유두(tilted disc) — 정상 변이. CDR이 커 보여 녹내장으로 오인될 수 있음.*

### 4.2 당뇨망막병증 (DR / DME / PDR)

![비증식성 당뇨망막병증](../assets/images/dr_nonproliferative_eda03.jpg)

*당뇨망막병증: 출혈, 미세혈관 이상 소견.*

![당뇨황반부종](../assets/images/dr_dme.jpg)

*당뇨황반부종(DME). 황반부 삼출/부종.*

![DME (EDA04)](../assets/images/dr_dme_eda04.jpg)

*황반부종을 동반한 당뇨망막병증.*

![증식성 당뇨망막병증](../assets/images/dr_pdr_eda01.jpg)

*증식성 당뇨망막병증(PDR): 신생혈관/섬유증식.*

![PDR 신생혈관](../assets/images/dr_pdr_neovascular.jpg)

*증식성 망막병증. 신생혈관 및 출혈.*

![당뇨황반부종 (NEI)](../assets/images/dme_nei.jpg)

*당뇨황반부종(DME, NEI). 황반부 부종/삼출.*

![범망막광응고(PRP) 후](../assets/images/dr_laser_eda09.jpg)

*범망막광응고(PRP) 치료 후 안저 — 레이저 반흔. 증식성 DR의 표준 치료 흔적.*

### 4.3 고혈압망막병증 (Hypertensive retinopathy)

![고혈압망막병증](../assets/images/hypertensive_retinopathy.jpg)

*고혈압망막병증: 동맥협착, AV crossing change, 출혈/삼출.*

![견과반점과 출혈](../assets/images/cotton_wool_spots.jpg)

*견과반점(cotton-wool spot)과 출혈 — 고혈압/당뇨/허혈에서 관찰.*

### 4.4 시신경유두부종 (Papilledema / disc edema)

![유두부종](../assets/images/papilledema.jpg)

*시신경유두부종: 경계흐림, 융기, 정맥확장.*

![중증 유두부종 (우안)](../assets/images/papilledema_severe_od.jpg)

*중증 유두부종(우안). 두개내압 상승 평가 필요.*

![유두부종과 출혈](../assets/images/optic_disc_edema_hemorrhage.jpg)

*시신경유두 부종과 주변 출혈.*

![유두부종 IIH 우안](../assets/images/papilledema_iih_right.jpg)

*특발성두개내고혈압(IIH) 우안 — 유두 융기, 경계흐림.*

![유두부종 IIH 좌안](../assets/images/papilledema_iih_left.jpg)

*특발성두개내고혈압(IIH) 좌안 — 양안성 유두부종.*

### 4.5 녹내장 (Glaucoma)

![녹내장 시신경유두](../assets/images/glaucoma_disc.jpg)

*녹내장성 시신경유두: 함몰 증가, 테두리 소실.*

![녹내장 진행](../assets/images/glaucoma_progression.jpg)

*녹내장 진행(시계열). CDR 진행 관찰.*

### 4.6 황반변성 (AMD)

![중간 단계 AMD](../assets/images/amd_intermediate.jpg)

*중간 단계 연령관련황반변성: 드루젠.*

### 4.7 망막박리 / 망막열공 (Retinal detachment / tear)

![열공성 망막박리](../assets/images/retinal_detachment_rhegmatogenous.jpg)

*열공성 망막박리. 응급 안과 의뢰 대상.*

![망막박리 (VHL)](../assets/images/retinal_detachment_vhl.jpg)

*Von Hippel-Lindau병에서의 망막박리.*

![망막열공](../assets/images/retinal_tear_hole.jpg)

*망막열공(round hole).*

### 4.8 망막혈관폐쇄 (Vein / artery occlusion)

![망막분지정맥폐쇄](../assets/images/brvo.jpg)

*망막분지정맥폐쇄(BRVO): 국소 출혈/견과반점.*

![망막중심동맥폐쇄 색전](../assets/images/retinal_embolism.jpg)

*망막동맥폐쇄/색전.*

![CRAO 벚꽃빨강반점](../assets/images/crao_cherry_red_spot.jpg)

*망막중심동맥폐쇄(CRAO)의 벚꽃빨강반점(cherry-red spot).*

![Hollenhorst plaque](../assets/images/hollenhorst_plaque.jpg)

*Hollenhorst plaque: 혈관 분지부 콜레스테롤 색전.*

### 4.9 기타

![중심장액망막병증](../assets/images/cscr.jpg)

*중심장액망막병증(CSCR).*

![망막색소변성증](../assets/images/retinitis_pigmentosa_mid.jpg)

*망막색소변성증(RP) 중기: 골세포양 색소침착.*

![망막모세포종](../assets/images/retinoblastoma.jpg)

*망막모세포종(retinoblastoma). 소아 백색동공 감별.*

### 4.10 황반원공 · RP 진행 · 맥락망막 반흔

![황반원공 (양안 비교)](../assets/images/macular_hole_pair.jpg)

*황반원공(macular hole) — 중심와 결손.*

![황반원공 (우안)](../assets/images/macular_hole_od.jpg)

*황반원공(우안). 중심 시력저하 + 변시증.*

![RP 초기](../assets/images/rp_early.jpg)

*망막색소변성증(RP) 초기.*

![RP 말기](../assets/images/rp_end.jpg)

*망막색소변성증(RP) 말기 — 골세포양 색소·혈관협착·시신경창백.*

![맥락망막 반흔](../assets/images/toxoplasma_scar.png)

*선천성 톡소플라스마 맥락망막 반흔(chorioretinal scar).*

---

## 5. 표준 척도 요약

- **DR 등급**: ICDR (No apparent / Mild / Moderate / Severe NPDR / PDR) + DME 별도. [1]
- **DME**: 중심와 침범 여부가 핵심(시력 예후). [1]
- **유두부종 등급**: Frisén grade 1–5 (유두주위 경계흐림 → 시신경혈관 완전 은폐). [3]
- **고혈압망막병증**: Keith-Wagener-Barker grade 1–4 (Grade 4 = 유두부종). [2]
- **녹내장**: CDR, ISNT rule, RNFL defect, 유두출혈의 조합으로 판단(단일 지표 불충분).

## 6. 참고문헌

1. Wilkinson CP, Ferris FL 3rd, Klein RE, et al. Proposed international clinical diabetic retinopathy and
   diabetic macular edema disease severity scales. *Ophthalmology*. 2003;110(9):1677-1682.
   doi:10.1016/S0161-6420(03)00475-5. PMID: 13129861.
2. Keith NM, Wagener HP, Barker NW. Some different types of essential hypertension: their course and
   prognosis. *Am J Med Sci*. 1939;197:332-343.
3. Frisén L. Swelling of the optic nerve head: a staging scheme. *J Neurol Neurosurg Psychiatry*.
   1982;45(1):13-18. doi:10.1136/jnnp.45.1.13. PMID: 7062066.
4. Tao B, Vosoughi A, Margolin E, Micieli JA. Papilledema. *StatPearls*. Updated 2025.
   https://www.ncbi.nlm.nih.gov/books/NBK538295/
5. Schneiderman H. The Funduscopic Examination. In: *Clinical Methods: The History, Physical, and
   Laboratory Examinations*. 3rd ed. Butterworths. https://www.ncbi.nlm.nih.gov/books/NBK221/
6. Stanford Medicine 25. Fundoscopic Exam (Ophthalmoscopy).
   https://med.stanford.edu/stanfordmedicine25/the25/fundoscopic.html
7. Conquer V, Lambolais T, Andrade-Miranda GX, Magnier B. Comprehensive Review of Open-Source Fundus
   Image Databases for Diabetic Retinopathy Diagnosis. *PMC12473202*. 2025.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC12473202/
8. Diagnosis of Optic Disc Oedema: Fundus Features, Ocular Imaging. *PMC10332214*.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC10332214/
9. The Value of Fundoscopy in General Practice. *The Open Ophthalmology Journal*. 2012;6:4.
   https://www.openophthalmologyjournal.com/VOLUME/6/PAGE/4/FULLTEXT/

## 7. 이미지 출처 및 라이선스

모든 이미지는 Wikimedia Commons에서 가져왔으며, Public Domain 또는 CC-BY / CC-BY-SA 라이선스다.
CC 라이선스 이미지는 저작자 표시가 필수다. 전체 메타데이터는 `assets/images/CREDITS.json` 참조.

| 파일 | 라이선스 | 출처/저작자 (요약) |
|---|---|---|
| normal_right_fundus.jpg | Public Domain | Wikimedia Commons |
| dr_dme_eda04.jpg | Public Domain | Wikimedia Commons |
| dr_pdr_eda01.jpg | Public Domain | Wikimedia Commons |
| dr_nonproliferative_eda03.jpg | Public Domain | Wikimedia Commons |
| dr_dme.jpg | Public Domain | National Eye Institute (NEI/NIH) |
| amd_intermediate.jpg | Public Domain | Wikimedia Commons |
| retinal_detachment_vhl.jpg | Public Domain | Wikimedia Commons |
| retinoblastoma_scan.jpg | Public Domain | Wikimedia Commons |
| normal_myopic_asian_od.jpg | CC BY-SA 2.0 | Wikimedia Commons |
| dr_pdr_neovascular.jpg | CC BY-SA 3.0 | Jekader |
| glaucoma_disc.jpg | CC BY-SA 3.0 | de:User:Snoop |
| glaucoma_progression.jpg | CC BY-SA 3.0 | Wikimedia Commons |
| retinal_tear_hole.jpg | CC BY-SA 4.0 | Amaris5 |
| retinal_detachment_rhegmatogenous.jpg | CC BY-SA 4.0 | Amaris5 |
| cotton_wool_spots.jpg | CC BY-SA 4.0 | Renátó Besenczi et al. |
| cscr.jpg | CC BY-SA 4.0 | Yoanmb |
| crao_cherry_red_spot.jpg | CC BY-SA 4.0 | Wikimedia Commons |
| optic_disc_edema_hemorrhage.jpg | CC BY-SA 4.0 | Maria Sieglinda von Nudeldorf |
| brvo.jpg | CC BY 2.0 | Ku C Yong et al. |
| papilledema_severe_od.jpg | CC BY 2.0 | Shveta Bansal, Timothy Dabbs, Vernon Long |
| retinitis_pigmentosa_mid.jpg | CC BY 2.0 | Christian Hamel |
| retinal_embolism.jpg | CC BY 2.0 | Robin G Jones, Adrian Peall |
| retinoblastoma.jpg | CC BY 2.0 | Wikimedia Commons |
| hypertensive_retinopathy.jpg | CC BY 3.0 | Frank Wood |
| papilledema.jpg | CC BY 3.0 | Jonathan Trobe, M.D. (Univ. of Michigan Kellogg Eye Center) |
| hollenhorst_plaque.jpg | CC BY 4.0 | Yong Meng Hsien et al. |
| dme_nei.jpg | Public Domain | National Eye Institute (NEI/NIH) |
| dr_laser_eda09.jpg | Public Domain | Wikimedia Commons |
| normal_od_highres.jpg | CC BY-SA 4.0 | Wikimedia Commons |
| tilted_disc.jpg | CC BY-SA 4.0 | Wikimedia Commons |
| macular_hole_pair.jpg | CC BY-SA 4.0 | Wikimedia Commons |
| macular_hole_od.jpg | CC BY-SA 3.0 | Wikimedia Commons |
| crvo_ecig.png | CC BY 4.0 | Wikimedia Commons (2022 case report) |
| papilledema_iih_right.jpg | CC BY 4.0 | Wikimedia Commons |
| papilledema_iih_left.jpg | CC BY 4.0 | Wikimedia Commons |
| rp_early.jpg | CC BY 2.0 | Christian Hamel |
| rp_end.jpg | CC BY 2.0 | Christian Hamel |
| toxoplasma_scar.png | CC BY 2.0 | Wikimedia Commons |

> 라이선스 상세와 정확한 저작자 표기는 `assets/images/CREDITS.json`의 `license`, `artist`, `source` 필드를 확인할 것. 배포/발표 시 각 이미지 저작자 표시 필요.

---
*문서 버전: v0.1 · 생성: fundoscopy-study 프로젝트 · 이미지 크롭 없음*
