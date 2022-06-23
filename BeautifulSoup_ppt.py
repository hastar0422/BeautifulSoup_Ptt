"""
作品名稱     ： PTT爬蟲
__author__ ： Ning 甯詠城
"""

from bs4 import BeautifulSoup
import sys
import urllib.request as httplib  # 3.x

#  SSL  處理，  https    SSSSSS 就需要加上以下2行
import ssl
ssl._create_default_https_context = ssl._create_unverified_context    # 因.urlopen發生問題，將ssl憑證排除
"""
抓 Holo 資訊
"""

url="https://www.ptt.cc/bbs/C_Chat/search?q=holo"
req = httplib.Request( url, data=None,  # 連線
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
)
reponse = httplib.urlopen(req)               # 開啟連線動作
if reponse.code==200:                        # 當連線正常時
    contents=reponse.read()                  # 讀取網頁內容
    contents=contents.decode("utf-8")        # 轉換編碼為 utf-8
#    print(contents)
str1=contents
soup=BeautifulSoup(str1, "html.parser")     #抓全部的資料下來

t1=soup.select('.title')                    #抓title的部分
#print(t1)
t2=t1[0].select('a')    #顯示a到/a     t2=<a href="/bbs/C_Chat/M.1650969770.A.7AF.html">[情報] Hololive 3D 立牌</a>
t3=t2[0].string         #抓tag的部分
t4=t2[0].get('href')    #取得href部分
for row in t1:          #用迴圈印出網頁裡所有的tag和href
    title=row.select('a')
    print("標題：",title[0].string,"\nhref:",title[0].get('href'),"\n")


