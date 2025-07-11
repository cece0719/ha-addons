# Hello World Add-on

A simple Hello World add-on for Home Assistant that runs a web server on port 8099.

## Features

- 간단한 "Hello World" 메시지 출력
- 8099 포트에서 웹 인터페이스 제공
- 아름다운 그라디언트 UI
- 설정 가능한 메시지
- 헬스 체크 엔드포인트

## Configuration

```yaml
message: "Hello World!"
```

### Option: `message`

출력할 메시지를 설정합니다.

## Usage

1. 애드온을 설치하고 시작합니다
2. 웹 UI를 통해 `http://[HOST]:8099`에 접속합니다
3. 설정에서 메시지를 변경할 수 있습니다

## Support

문제가 있으시면 GitHub 이슈를 등록해 주세요.
