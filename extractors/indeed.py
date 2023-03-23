from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

'''
options = Options()
options.add_argument("--no-sandbox")    # replit에서 selenium을 동작시키기 위한 코드 
options.add_argument("--disable-dev-shm-usage")    # replit에서 selenium을 동작시키기 위한 코드 
'''

def get_page_count(keyword):
    base_url = 'https://kr.indeed.com/jobs?q='
    browser = webdriver.Chrome()
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    pagination = soup.find('nav', class_='ecydgvn0')
    if pagination == None:
        return 1
    pages = pagination.find_all('div', recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):   # page만큼 job scrape
        base_url = 'https://kr.indeed.com/jobs'
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)
        browser = webdriver.Chrome() # request를 쓰지 않는 이유는 indeed 페이지가 봇 검사를 하므로 request를 사용한 접속을 막고 있다.
        browser.get(final_url)

        soup = BeautifulSoup(browser.page_source, 'html.parser')
        job_list = soup.find('ul', class_='jobsearch-ResultsList')
        jobs = job_list.find_all('li', recursive=False)
        for job in jobs:
            zone = job.find('div', class_='mosaic-zone')
            if zone == None:
                '''
                h2 = job.find('h2', class_='jobTitle')
                a = h2.find('a')
                '''
                anchor = job.select_one('h2 a') # 위 코드 2줄을 select를 사용해서 한 줄로 만들 수 있다. select인자는 css selector를 사용해서 찾고자 하는 것을 찾을 수 있다. '상윈 selector 하위 selector'. selector_one을 사용하면 하나의 결과만 가져온다.
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find('span', class_='companyName')
                location = job.find('div', class_='companyLocation')
                job_data = {
                    'link' : f'{"https://kr.indeed.com/{link}"}',
                    'company' : company.string,
                    'location' : location.string,
                    'position' : title
                }
                results.append(job_data)
    return results

jobs = extract_indeed_jobs('python')
print(jobs)