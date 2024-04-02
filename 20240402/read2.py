import requests
import feedparser

for num in range(1, 23):
    url = 'https://www.cwa.gov.tw/rss/forecast/36_' + str(num).zfill(2) + '.xml'
    print(url)
    response = requests.get(url)
    feed = feedparser.parse(response.content)
    
    # 直接取得最後一個條目
    entry = feed.entries[-1]

    # 從最後一個條目中提取出所需的資訊
    title = entry.title[0:3]
    description = entry.description[12:20]

    # 直接印出這些資訊
    print(f"COUNTYNAME: {title}, 溫度: {description}")

    print("=======================================")