from requests import get

websites = (
    'google.com',
    'airbnb.com',
    'https://twitter.com',
    'facebook.com',
    'https://tiktok.com'
)

results = {}

for website in websites:
    if not website.startswith('https://'):  #webstie가 'https://'로 시작하면(True) 조건에 충족하지 않고 그렇지 않으면(False)이면 조건에 충족한다.
        website = f'https://{website}'
    response = get(website) #  'get' returns response
    if response.status_code == 200: # http 응답 코드 확인
        results[website] = "OK"
    else:
        results[website] = "FAILED"

print(results)