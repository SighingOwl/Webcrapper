from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask('JobScrapper')

db = {}

@app.route('/') # '@':decorator, synractic sugar : 문법적 기능은 유지하되 코드 작성 및 읽는 것에서 편의성을 높인 프로그래밍 문법
def home():
    return render_template('home.html', name='A')   # flask는 render_template을 사용해서 주어진 변수를 template에 적용할 수 있다.

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword == None or keyword == '':
        return redirect('/')
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template('search.html', keyword=keyword, jobs=jobs)

@app.route('/export')
def export():
    keyword = request.args.get('keyword')
    if keyword == None or keyword == '':
        return redirect('/')
    if keyword not in db:
        return redirect(f'/search?keyword={keyword}')
    save_to_file(keyword, db[keyword])
    return send_file(f'{keyword}.csv', as_attachment=True)  # 결과를 사용자가 다운로드할 수 있도록 하는 방법


app.run('127.0.0.1', port=5001)