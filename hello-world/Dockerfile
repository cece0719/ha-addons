ARG BUILD_FROM
FROM $BUILD_FROM

# 필요한 패키지 설치
RUN apk add --no-cache \
    python3 \
    py3-pip \
    curl \
    && rm -rf /var/cache/apk/*

# 작업 디렉토리 설정
WORKDIR /app

# Python 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY app.py .
COPY run.sh /
RUN chmod a+x /run.sh

# 포트 노출
EXPOSE 8099

# 헬스체크 추가
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8099/health || exit 1

# curl 설치 (헬스체크용)
RUN apk add --no-cache curl

# Home Assistant 레이블
LABEL \
    io.hass.name="Hello World" \
    io.hass.description="A simple Hello World add-on" \
    io.hass.arch="armhf|aarch64|amd64|armv7|i386" \
    io.hass.type="addon" \
    io.hass.version="1.0.0"

# 애플리케이션 실행
CMD ["/run.sh"]
