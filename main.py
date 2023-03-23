from flask import Flask

app = Flask('JobScrapper')

@app.route('/') # '@':decorator, synractic sugar : 문법적 기능은 유지하되 코드 작성 및 읽는 것에서 편의성을 높인 프로그래밍 문법
def home():
    return 'hey there!'

app.run('127.0.0.1')