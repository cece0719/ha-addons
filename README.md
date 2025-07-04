# 홈어시스턴트 애드온 모음

이 저장소는 홈어시스턴트용 커스텀 애드온들을 모아놓은 곳입니다.

## 📦 포함된 애드온

### 1. Hello World 애드온
- **포트**: 8030
- **설명**: 포트 8030에서 Hello World를 표시하는 간단한 웹 애플리케이션
- **기능**: 
  - 아름다운 그라데이션 배경
  - 실시간 시간 표시
  - 상태 확인 엔드포인트 (`/health`)

### 2. Merong 애드온
- **포트**: 8040
- **설명**: Merong을 표시하는 재미있는 인터랙티브 웹 애플리케이션
- **기능**:
  - 클릭 가능한 이모지
  - 클릭 횟수 카운터
  - 랜덤 이모지 변경
  - 무지개색 텍스트 애니메이션
  - API 엔드포인트 (`/api/click`, `/health`)

## 🚀 설치 방법

### 1. 저장소 추가
홈어시스턴트의 설정 > 애드온 > 애드온 스토어에서 다음 URL을 추가:
```
https://github.com/your-username/ha-addons
```

### 2. 애드온 설치
1. 홈어시스턴트 대시보드에서 **설정** > **애드온**으로 이동
2. **애드온 스토어** 탭에서 원하는 애드온을 찾아 **설치** 클릭
3. 설치 후 **시작** 버튼을 눌러 애드온 실행

## 🔧 사용법

### Hello World 애드온
- 설치 후 `http://your-ha-ip:8030`으로 접속
- 웹 UI에서 애드온 상태 확인 가능

### Merong 애드온
- 설치 후 `http://your-ha-ip:8040`으로 접속
- 이모지를 클릭하여 재미있는 인터랙션 즐기기
- 클릭 횟수와 다양한 이모지 효과 확인

## 📁 파일 구조

```
ha-addons/
├── hello-world/
│   ├── config.yaml      # 애드온 설정
│   ├── Dockerfile       # Docker 이미지 설정
│   └── app.py          # Flask 애플리케이션
├── merong/
│   ├── config.yaml      # 애드온 설정
│   ├── Dockerfile       # Docker 이미지 설정
│   └── app.py          # Flask 애플리케이션
└── README.md           # 이 파일
```

## 🛠️ 개발

### 새로운 애드온 추가하기
1. 새 디렉토리 생성 (애드온 이름으로)
2. `config.yaml` 파일 생성 (홈어시스턴트 애드온 설정)
3. `Dockerfile` 생성 (컨테이너 설정)
4. 애플리케이션 코드 작성
5. README 업데이트

### 로컬 테스트
```bash
# Hello World 애드온 테스트
cd hello-world
docker build -t hello-world .
docker run -p 8030:8030 hello-world

# Merong 애드온 테스트
cd merong
docker build -t merong .
docker run -p 8040:8040 merong
```

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 🤝 기여하기

1. 이 저장소를 포크하세요
2. 새로운 브랜치를 만드세요 (`git checkout -b feature/amazing-addon`)
3. 변경사항을 커밋하세요 (`git commit -m 'Add amazing addon'`)
4. 브랜치에 푸시하세요 (`git push origin feature/amazing-addon`)
5. Pull Request를 생성하세요

## 📞 지원

문제가 있거나 새로운 애드온을 제안하고 싶으시면 이슈를 생성해주세요! 