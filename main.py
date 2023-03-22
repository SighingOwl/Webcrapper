from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
'''
options = Options()
options.add_argument("--no-sandbox")    # replit에서 selenium을 동작시키기 위한 코드 
options.add_argument("--disable-dev-shm-usage")    # replit에서 selenium을 동작시키기 위한 코드 
'''
browser = webdriver.Chrome() # request를 쓰지 않는 이유는 indeed 페이지가 봇 검사를 하므로 request를 사용한 접속을 막고 있다.
browser.get("https://kr.indeed.com/jobs?q=python&l=&vjk=958ade57ee98b45a")

print(browser.page_source)