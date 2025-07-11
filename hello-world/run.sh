#!/usr/bin/with-contenv bashio

bashio::log.info "Starting Hello World Add-on..."

# 옵션 읽기
MESSAGE=$(bashio::config 'message')
bashio::log.info "Message: ${MESSAGE}"

# 환경 변수 설정
export MESSAGE="${MESSAGE}"

# Python 애플리케이션 실행
bashio::log.info "Starting Python application on port 8099..."
cd /app
exec python app.py
