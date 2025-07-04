#!/usr/bin/env python3
"""
Hello World 애드온
포트 8030에서 Hello World를 표시하는 간단한 웹 애플리케이션
"""

from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML 템플릿
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World 애드온</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 3rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        .status {
            background: rgba(255, 255, 255, 0.2);
            padding: 1rem;
            border-radius: 10px;
            margin-top: 2rem;
        }
        .time {
            font-size: 1.1rem;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌍 Hello World!</h1>
        <p>홈어시스턴트 애드온이 성공적으로 실행 중입니다.</p>
        <div class="status">
            <strong>상태:</strong> 실행 중 ✅<br>
            <strong>포트:</strong> 8030<br>
            <strong>버전:</strong> 1.0.0
        </div>
        <div class="time">
            현재 시간: {{ current_time }}
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello_world():
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML_TEMPLATE, current_time=current_time)

@app.route('/health')
def health():
    return {"status": "healthy", "message": "Hello World 애드온이 정상적으로 실행 중입니다."}

if __name__ == '__main__':
    # 환경 변수에서 포트 가져오기 (기본값: 8030)
    port = int(os.environ.get('PORT', 8030))
    
    print(f"🚀 Hello World 애드온 시작 중...")
    print(f"📡 포트: {port}")
    print(f"🌐 웹 UI: http://localhost:{port}")
    
    app.run(host='0.0.0.0', port=port, debug=False) 