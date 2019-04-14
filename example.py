import requests

url = "https://www.bilibili.com/"
kv = {'user-agent': 'Chrome/10.0'}
try:
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    print(r.status_code)
    print(r.encoding)
    print(r.text[:1000])
except:
    print("爬取失败")