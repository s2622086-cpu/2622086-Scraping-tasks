import requests
import time
from bs4 import BeautifulSoup

url='https://www.musashino-u.ac.jp'
res = requests.get(url)

# HTMLのソースコードをBeautifulSoupオブジェクトに変換する処理
# html_soup = BeautifulSoup(res.text, 'html.parser')
html_soup = BeautifulSoup(res.content, 'html.parser')
print(f"html_soupの型：{type(html_soup)}")

soup_title = html_soup.title
print(soup_title)
print(f"{type(soup_title)}")

time.sleep(10)  # 1秒待機