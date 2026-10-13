# fundoscopy-study

안저사진(fundus) 기반 **의료 AI 앱**과 **의사 학습자료**를 함께 만드는 프로젝트.

## 목표

1. **안저 이미지 분석 AI 앱** — State Space Model(vision mamba 등) 기반, **GPU 없는 환경**에서도
   실험·추론 가능. 건강검진에서 흔한 소견을 우선 판독.
2. **의사 공부자료** — 안저검사 기초 → 흔한 소견 해석 → 각론(아틀라스) → red flag를
   PPT형 HTML로 만들고 PDF로도 렌더링.

## 산출물

| 경로 | 설명 |
|---|---|
| `docs/fundus-common-findings-and-red-flags.md` | 1-a. 흔한 소견 + red flag 정리(출처/이미지 포함) |
| `docs/datasets.md` | 1-b. 지도학습용 공개 데이터셋 카탈로그 + 실험 계획 |
| `slides/index.html` | 2. 학습자료 슬라이드(27장, PPT형) |
| `slides/fundoscopy-slides.pdf` | 2. PDF 렌더링 결과 |
| `slides/figures/*.svg` | 적색반사·유두·황반·C/D·A/V·ISNT 도해(스키매틱) |
| `app/PLAN-keras-tensorflow.md` | 1. AI 앱을 **Keras/TensorFlow로** 구현하는 계획(미착수) |
| `assets/images/` | 크롭하지 않은 안저 이미지 원본 + `CREDITS.json` |

## 빌드 방법

```bash
# 슬라이드 PDF 재생성 (Windows Chrome headless 사용, /mnt/d 기준 D:\ 경로)
"/mnt/c/Program Files/Google/Chrome/Application/chrome.exe" \
  --headless=new --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf="D:\\kimaki-projects\\fundoscopy-study\\slides\\fundoscopy-slides.pdf" \
  "file:///D:/kimaki-projects/fundoscopy-study/slides/index.html"
```

- 이미지 재다운로드: `python3 scripts/download_images.py`
- Commons 검색: `python3 scripts/fetch_commons_images.py search "glaucoma fundus"`

## 다음 단계 (예정)

- [ ] Keras/TF 계획에 따라 구현: `app/PLAN-keras-tensorflow.md` (M1 SSM 레이어 → M2 합성 학습 → M4 APTOS 베이스라인)
- [ ] 데이터: APTOS로 파이프라인 고정 → IDRiD/RFMiD/녹내장으로 확장 (환자 단위 split 필수)
- [ ] 라벨 체계를 위 문서의 소견/red flag 목록과 정렬

## 라이선스 / 주의

- 이미지는 Wikimedia Commons의 Public Domain / CC-BY / CC-BY-SA. 배포 시 저작자 표시 필요(`CREDITS.json`).
- 문서·슬라이드는 **의료진 학습/개발 참고자료**이며 개별 환자 진단·치료 지침이 아니다.
