# Dog Ear Roulette

강아지 사진을 넣으면 귀, 모자, 왕관, 리본 같은 장식이 룰렛처럼 내려와 사진 위에 합성되는 브라우저 앱입니다.

현재 버전은 설치 없이 실행되는 HTML/Canvas 앱입니다. 사진을 업로드하면 가벼운 이미지 분석으로 강아지가 있을 법한 영역을 찾고, 장식을 자동으로 배치합니다.

## 실행 방법

Windows에서 바로 실행:

```bash
룰렛_실행.bat
```

또는 Python으로 실행:

```bash
python Untitled-1.py
```

직접 열기:

```bash
index.html
```

GitHub Pages에 올리면 `index.html`이 자동으로 앱 화면으로 연결됩니다.

## 기능

- 강아지 사진 업로드
- 귀, 모자, 왕관, 리본 장식 선택
- 위에서 아래로 내려오는 룰렛 애니메이션
- 사진 기반 자동 맞춤
- 가로, 세로, 크기, 기울기 수동 보정
- PNG 저장

## AI 모델 업그레이드 방향

현재 자동 맞춤은 무거운 AI 모델이 아니라 브라우저 안에서 이미지 색상과 경계 차이를 분석하는 방식입니다. 빠르고 가볍지만, 배경이 복잡하거나 강아지가 여러 마리면 정확도가 떨어질 수 있습니다.

다음 단계로는 세 가지 선택지가 있습니다.

1. 가벼운 모델: TensorFlow.js COCO-SSD 같은 브라우저 모델로 `dog` 영역을 먼저 찾고, 그 영역 안에서 현재 자동 맞춤을 적용합니다. 구현 난이도와 속도 균형이 좋습니다.
2. 중간 모델: MediaPipe나 TensorFlow.js 기반 모델을 써서 브라우저에서 추론합니다. 서버 없이 동작하지만 모델 파일과 로딩 시간이 늘어납니다.
3. 무거운 모델: 직접 강아지 얼굴/귀 위치 데이터셋을 만들고 커스텀 keypoint/object detection 모델을 학습합니다. 정확도는 가장 좋지만, 데이터 수집과 학습 파이프라인이 필요합니다.

AI 개발자 포트폴리오 관점에서는 `현재 앱 -> dog box detector -> custom dog face detector` 순서로 키우는 게 좋습니다.

## Git에 올릴 때 주의

강아지 사진은 개인정보가 될 수 있어서 `.gitignore`에 이미지 파일을 제외했습니다. GitHub에는 코드와 문서만 올리고, 테스트 사진은 로컬에만 두는 것을 권장합니다.

처음 GitHub에 올리는 예시:

```bash
git init
git add .
git commit -m "Add dog ear roulette app"
git branch -M main
git remote add origin https://github.com/YOUR_NAME/dog-ear-roulette.git
git push -u origin main
```

## 참고할 공식 문서

- TensorFlow.js models: https://www.tensorflow.org/js/models
- MediaPipe Tasks Vision for Web: https://ai.google.dev/edge/api/mediapipe/js/tasks-vision
