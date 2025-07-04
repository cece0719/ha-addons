#!/usr/bin/env python3
"""
Merong 애드온
포트 8040에서 Merong을 표시하는 재미있는 웹 애플리케이션
"""

from flask import Flask, render_template_string
import os
import random

app = Flask(__name__)

# HTML 템플릿
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Merong 애드온</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.15);
            padding: 3rem;
            border-radius: 25px;
            backdrop-filter: blur(15px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .merong {
            font-size: 8rem;
            margin: 1rem 0;
            animation: bounce 2s infinite;
            cursor: pointer;
            user-select: none;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-20px); }
            60% { transform: translateY(-10px); }
        }
        
        h1 {
            font-size: 2.5rem;
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
            border-radius: 15px;
            margin-top: 2rem;
        }
        
        .counter {
            font-size: 1.5rem;
            font-weight: bold;
            margin: 1rem 0;
            color: #ffeb3b;
        }
        
        .rainbow-text {
            background: linear-gradient(45deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #4b0082, #9400d3);
            background-size: 400% 400%;
            animation: rainbow 3s ease infinite;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        @keyframes rainbow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="merong" onclick="clickMerong()">😊</div>
        <h1 class="rainbow-text">Merong!</h1>
        <p>클릭해서 Merong을 더 많이 만들어보세요! 🎉</p>
        <div class="counter">클릭 횟수: <span id="clickCount">0</span></div>
        <div class="status">
            <strong>상태:</strong> Merong 중 😊<br>
            <strong>포트:</strong> 8040<br>
            <strong>버전:</strong> 1.0.0
        </div>
    </div>
    
    <script>
        let clickCount = 0;
        const merongEmojis = ['😊', '😄', '😁', '😆', '😃', '😉', '😋', '😎', '🤗', '😍'];
        
        function clickMerong() {
            clickCount++;
            document.getElementById('clickCount').textContent = clickCount;
            
            // 랜덤한 이모지로 변경
            const randomEmoji = merongEmojis[Math.floor(Math.random() * merongEmojis.length)];
            document.querySelector('.merong').textContent = randomEmoji;
            
            // 클릭 효과
            const container = document.querySelector('.container');
            container.style.transform = 'scale(1.05)';
            setTimeout(() => {
                container.style.transform = 'scale(1)';
            }, 150);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def merong():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/click')
def api_click():
    return {"message": "Merong!", "timestamp": "현재 시간"}

@app.route('/health')
def health():
    return {"status": "merong", "message": "Merong 애드온이 정상적으로 실행 중입니다."}

if __name__ == '__main__':
    # 환경 변수에서 포트 가져오기 (기본값: 8040)
    port = int(os.environ.get('PORT', 8040))
    
    print(f"😊 Merong 애드온 시작 중...")
    print(f"📡 포트: {port}")
    print(f"🌐 웹 UI: http://localhost:{port}")
    
    app.run(host='0.0.0.0', port=port, debug=False) 