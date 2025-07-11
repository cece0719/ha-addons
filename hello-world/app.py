#!/usr/bin/env python3
import json
import logging
import os
import sys
from flask import Flask, render_template_string

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def get_options():
    """Home Assistant 옵션 읽기"""
    try:
        with open('/data/options.json', 'r') as f:
            options = json.load(f)
            logger.info(f"Options loaded: {options}")
            return options
    except FileNotFoundError:
        logger.warning("Options file not found at /data/options.json, using defaults")
        return {"message": "Hello World!"}
    except Exception as e:
        logger.error(f"Error reading options: {e}")
        return {"message": "Hello World!"}

@app.route('/')
def hello():
    options = get_options()
    message = options.get('message', 'Hello World!')
    
    html_template = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World Add-on</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 3rem;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            .subtitle {
                font-size: 1.2rem;
                opacity: 0.8;
                margin-bottom: 2rem;
            }
            .info {
                font-size: 1rem;
                opacity: 0.7;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{{ message }}</h1>
            <p class="subtitle">Home Assistant Add-on</p>
            <p class="info">포트: 8099 | 상태: 실행 중</p>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template, message=message)

@app.route('/health')
def health():
    """헬스 체크 엔드포인트"""
    return {"status": "healthy", "port": 8099, "message": "Hello World Add-on is running"}

@app.route('/debug')
def debug():
    """디버그 정보"""
    options = get_options()
    return {
        "status": "running",
        "port": 8099,
        "options": options,
        "message": "Debug info"
    }

if __name__ == '__main__':
    logger.info("=" * 50)
    logger.info("Hello World Add-on starting...")
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Flask app: {app}")
    logger.info("Checking data directory...")
    
    # 데이터 디렉토리 확인
    if os.path.exists('/data'):
        logger.info("Data directory exists")
        if os.path.exists('/data/options.json'):
            logger.info("Options file found")
        else:
            logger.warning("Options file not found")
    else:
        logger.warning("Data directory not found")
    
    logger.info("Starting Flask server on 0.0.0.0:8099...")
    logger.info("=" * 50)
    
    try:
        app.run(host='0.0.0.0', port=8099, debug=False, threaded=True)
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        sys.exit(1)
