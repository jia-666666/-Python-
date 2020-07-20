# 代理ip
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

url = 'https://2020.ip138.com/'
#HTTP://
page_text = requests.get(url=url, headers=headers, proxies={'http': '182.92.113.148:8118'}).text
print(page_text)
# with open('./ip.html', 'w', encoding='utf-8') as fp:
#     fp.write(page_text)

https_proxies = [
    {'https': '134.209.13.16:8080'},
    {'https': '134.209.13.14:8080'},
    {'https': '134.209.13.19:8080'}
]
http_proxies = [
    {'http': '134.209.13.16:8080'},
    {'http': '134.209.13.14:8080'},
    {'http': '134.209.13.19:8080'}
]

# 获取请求的url
# url = 'https://www.baidu.com/s?wd=ip'
# response = requests.get(url=url, headers=headers)
# response.url.split(':')[0]