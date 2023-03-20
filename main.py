from requests import get
from bs4 import BeautifulSoup

base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_term = 'python'

response = get(f'{base_url}{search_term}')
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('section', class_="jobs")  #   'class' 대신 'class_'를 사용하는 이유는 'class'는 이미 python 예약어이기 때문
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop()
        for post in job_posts:
            print(post)
            print('////////////')