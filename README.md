# Dog Random Ear

강아지 사진 위에 랜덤 귀와 모자 장식을 합성하는 웹 기반 이미지 편집 프로젝트입니다.  
사진을 업로드하면 장식이 릴스처럼 위에서 아래로 내려오고, 사용자가 직접 멈춰 강아지 얼굴에 맞출 수 있습니다.

## Live Demo

GitHub Pages 배포 후 아래 주소에서 실행할 수 있습니다.

https://RohKJ.github.io/dog_random_ear/

## 프로젝트 개요

Dog Random Ear는 반려동물 사진을 더 재미있게 꾸밀 수 있는 브라우저 앱입니다.  
별도 설치 없이 HTML, CSS, JavaScript만으로 동작하며 Canvas API를 사용해 이미지 합성과 저장 기능을 구현했습니다.

현재 버전은 TensorFlow.js COCO-SSD 모델로 사진 속 강아지 영역을 먼저 탐지합니다.  
탐지된 위치를 기준으로 얼굴 근처 목표 지점을 만들고, 장식이 그 위치에 가까울 때 멈추면 자연스럽게 스냅됩니다.

## 주요 기능

- 강아지 사진 업로드
- 귀, 모자, 왕관, 리본 장식 선택
- 릴스처럼 내려오는 장식 멈추기
- 사진에서 잘라낸 듯한 `사진 귀 컷` 장식
- 사진 기반 자동 맞춤
- 위치, 크기, 기울기 수동 조절
- 완성 이미지 PNG 저장

## 기술 스택

| 영역 | 기술 |
| --- | --- |
| Frontend | HTML, CSS, JavaScript |
| AI / Vision | TensorFlow.js, COCO-SSD |
| Image Processing | Canvas API, lightweight fallback detection |
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
3. TensorFlow.js COCO-SSD 모델로 강아지 영역을 탐지합니다.
4. 귀 또는 모자 장식이 릴스처럼 위에서 아래로 내려옵니다.
5. 사용자가 원하는 순간 멈추면 장식을 얼굴 위치에 합성합니다.
6. 사용자가 최종 이미지를 PNG로 저장합니다.

## AI 확장 계획

### 1단계: 현재 자동 맞춤 개선

이미지의 주 피사체 영역을 더 안정적으로 찾도록 색상, 경계, 중심 가중치 기반 로직을 개선합니다.

### 2단계: 객체 탐지 모델 적용

TensorFlow.js COCO-SSD 모델을 사용해 사진 속 `dog` 영역을 먼저 탐지하고, 탐지된 영역을 기준으로 장식 위치를 계산합니다.

현재 구현 상태: 완료

### 3단계: 릴스형 사용자 인터랙션

자동으로 멈추는 룰렛이 아니라, 사용자가 직접 타이밍을 맞춰 멈추는 방식으로 변경합니다.  
얼굴 기준점과 가까운 곳에서 멈추면 장식이 스냅되어 실제로 입혀지는 느낌을 강화합니다.

현재 구현 상태: 완료

### 4단계: 커스텀 강아지 얼굴 모델

강아지 얼굴과 귀 위치를 직접 라벨링한 데이터셋으로 keypoint detection 또는 object detection 모델을 학습합니다.

## 개발 방향

이 프로젝트는 단순한 사진 꾸미기 앱에서 시작해, 브라우저 기반 AI 추론과 커스텀 비전 모델 학습까지 확장하는 것을 목표로 합니다.  
작은 인터랙션 기능을 먼저 완성하고, 이후 실제 모델을 붙이며 AI 개발 포트폴리오로 발전시킬 예정입니다.

## 참고 자료

- TensorFlow.js Models: https://www.tensorflow.org/js/models
- MediaPipe Tasks Vision: https://ai.google.dev/edge/api/mediapipe/js/tasks-vision
