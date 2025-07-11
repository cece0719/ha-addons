# Home Assistant Add-ons Repository

이 저장소는 Home Assistant 애드온들을 포함하고 있습니다.

## 애드온 목록

### Hello World
- 8099 포트에서 실행되는 간단한 Hello World 웹 서버
- 설정 가능한 메시지
- 아름다운 웹 인터페이스

## 설치 방법

1. Home Assistant에서 **Supervisor** > **Add-on Store**로 이동
2. 우측 상단의 메뉴(⋮)를 클릭하고 **Repositories** 선택
3. 다음 URL을 추가: `https://github.com/cece0719/ha-addons`
4. 새로운 애드온들이 Add-on Store에 나타납니다

## 개발 및 테스트

로컬에서 애드온을 테스트하려면:

```bash
# 애드온 빌드
cd hello-world
docker build -t hello-world-addon .

# 애드온 실행
docker run -p 8099:8099 hello-world-addon
```

그런 다음 `http://localhost:8099`에서 확인할 수 있습니다.

## 기여

이슈나 풀 리퀘스트를 환영합니다!
