from flask import Flask, render_template, request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask('JobScrapper')

db = {}

@app.route('/') # '@':decorator, synractic sugar : 문법적 기능은 유지하되 코드 작성 및 읽는 것에서 편의성을 높인 프로그래밍 문법
def home():
    return render_template('home.html', name='A')   # flask는 render_template을 사용해서 주어진 변수를 template에 적용할 수 있다.

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template('search.html', keyword=keyword, jobs=jobs)

app.run('127.0.0.1', port=5001)