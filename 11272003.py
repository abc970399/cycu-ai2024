print("Hello, World!")

#https://news.pts.org.tw/xml/newsfeed.xml

import requests
import feedparser

url = "https://news.pts.org.tw/xml/newsfeed.xml"
#解析網頁
response = requests.get(url)

feed = feedparser.parse(response.text)

#找到所有的標題並印出
for entry in feed.entries:
    print(entry.title)
    print(entry.summary)

    if "  " in entry.title:
        with open("C:\\Users\\User\\Desktop\\cycu_ai2024\\cycu_ai2024\\20240227\\news.txt", "a", encoding="utf-8") as file:
            file.write(entry.title + "\n")
            file.write(entry.summary + "\n")

print("--------------------")
            

