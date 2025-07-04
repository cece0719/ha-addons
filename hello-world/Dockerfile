FROM python:3.9-alpine

# 필요한 패키지 설치
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev

# 작업 디렉토리 설정
WORKDIR /app

# Python 의존성 설치
RUN pip install flask

# 애플리케이션 파일 복사
COPY app.py .

# 포트 노출
EXPOSE 8030

# 애플리케이션 실행
CMD ["python", "app.py"] 