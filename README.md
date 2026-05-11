# Dog Random Ear

강아지 사진 위에 랜덤 귀와 모자 장식을 합성하는 웹 기반 이미지 편집 프로젝트입니다.  
사진을 업로드하면 장식이 룰렛처럼 내려오고, 자동 맞춤 기능으로 강아지 얼굴 근처에 배치됩니다.

## 프로젝트 개요

Dog Random Ear는 반려동물 사진을 더 재미있게 꾸밀 수 있는 브라우저 앱입니다.  
별도 설치 없이 HTML, CSS, JavaScript만으로 동작하며 Canvas API를 사용해 이미지 합성과 저장 기능을 구현했습니다.

현재 버전은 가벼운 이미지 분석 방식으로 강아지 위치를 추정합니다.  
이후에는 객체 탐지 모델과 커스텀 강아지 얼굴 모델을 붙여 AI 기반 자동 합성 프로젝트로 확장하는 것을 목표로 합니다.

## 주요 기능

- 강아지 사진 업로드
- 귀, 모자, 왕관, 리본 장식 선택
- 랜덤 룰렛 애니메이션
- 사진 기반 자동 맞춤
- 위치, 크기, 기울기 수동 조절
- 완성 이미지 PNG 저장

## 기술 스택

| 영역 | 기술 |
| --- | --- |
| Frontend | HTML, CSS, JavaScript |
| Image Processing | Canvas API |
| Runtime | Browser, Python launcher |
| Version Control | Git, GitHub |

## 실행 방법

Windows에서 바로 실행할 수 있습니다.

```bash
룰렛_실행.bat
```

Python으로 실행할 수도 있습니다.

```bash
python Untitled-1.py
```

브라우저에서 직접 열려면 `index.html`을 실행하면 됩니다.

## 프로젝트 구조

```text
dog_random_ear/
├── dog_ear_roulette.html
├── index.html
├── Untitled-1.py
├── 룰렛_실행.bat
├── docs/
│   └── AI_ROADMAP.md
└── README.md
```

## 시스템 흐름

1. 사용자가 강아지 사진을 업로드합니다.
2. Canvas에 사진을 렌더링합니다.
3. 이미지의 색상과 경계 차이를 분석해 강아지 위치를 추정합니다.
4. 귀 또는 모자 장식이 룰렛 애니메이션으로 내려옵니다.
5. 선택된 장식을 사진 위에 합성합니다.
6. 사용자가 최종 이미지를 PNG로 저장합니다.

## AI 확장 계획

### 1단계: 현재 자동 맞춤 개선

이미지의 주 피사체 영역을 더 안정적으로 찾도록 색상, 경계, 중심 가중치 기반 로직을 개선합니다.

### 2단계: 객체 탐지 모델 적용

TensorFlow.js 기반 모델을 사용해 사진 속 `dog` 영역을 먼저 탐지하고, 탐지된 영역을 기준으로 장식 위치를 계산합니다.

### 3단계: 커스텀 강아지 얼굴 모델

강아지 얼굴과 귀 위치를 직접 라벨링한 데이터셋으로 keypoint detection 또는 object detection 모델을 학습합니다.

## 개발 방향

이 프로젝트는 단순한 사진 꾸미기 앱에서 시작해, 브라우저 기반 AI 추론과 커스텀 비전 모델 학습까지 확장하는 것을 목표로 합니다.  
작은 인터랙션 기능을 먼저 완성하고, 이후 실제 모델을 붙이며 AI 개발 포트폴리오로 발전시킬 예정입니다.

## 참고 자료

- TensorFlow.js Models: https://www.tensorflow.org/js/models
- MediaPipe Tasks Vision: https://ai.google.dev/edge/api/mediapipe/js/tasks-vision
