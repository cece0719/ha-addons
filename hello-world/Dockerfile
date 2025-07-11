FROM python:3.11-alpine

# 필요한 패키지 설치
RUN apk add --no-cache \
    gcc \
    musl-dev \
    && rm -rf /var/cache/apk/*

# 작업 디렉토리 설정
WORKDIR /app

# Python 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY app.py .

# 포트 노출
EXPOSE 8099

# Home Assistant 레이블
LABEL \
    io.hass.name="Hello World" \
    io.hass.description="A simple Hello World add-on" \
    io.hass.arch="armhf|aarch64|amd64|armv7|i386" \
    io.hass.type="addon" \
    io.hass.version="1.0.0"

# 애플리케이션 실행
CMD ["python", "app.py"]
