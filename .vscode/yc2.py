import requests
from bs4 import BeautifulSoup
html1 = "https://www.cust.edu.cn/lgxw/index.htm"
realhtml = html1 
req = requests.get(url=realhtml)
req.encoding = "utf-8"
information = req.text
soup = BeautifulSoup(req.text, features="html.parser")
win = soup.find_all('ul', class_="newsList")
for win in win:
    out = win.text.strip()
    with open('2022大赛信息.txt', 'a+', encoding='utf-8') as f:
        for data in out:
            f.write(data)
        f.close()
f = open('2022大赛信息.txt', 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    if '2022' in line:
        if '学生' in line:
            if '竞赛' in line:
                print(line.strip())
f.close()

