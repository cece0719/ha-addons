ARG BUILD_FROM
FROM $BUILD_FROM

# 환경 변수 설정
ENV LANG C.UTF-8

# Python 및 필요한 패키지 설치
RUN \
    apk add --no-cache \
        python3 \
        py3-pip \
        gcc \
        musl-dev \
        python3-dev \
    \
    && pip3 install --no-cache --upgrade pip \
    && pip3 install --no-cache flask

# 작업 디렉토리 설정
WORKDIR /app

# 애플리케이션 파일 복사
COPY app.py .
COPY run /run

# 실행 권한 부여
RUN chmod a+x /run

# 포트 노출
EXPOSE 8030

# 애플리케이션 실행
CMD ["/run"] 