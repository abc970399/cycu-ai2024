
import requests
import xml.etree.ElementTree as ET

# 迴圈從1到22
for i in range(1, 23):
    # 建立URL
    url = f"https://www.cwa.gov.tw/rss/forecast/36_{str(i).zfill(2)}.xml"
    
    # 獲取網頁內容
    response = requests.get(url)
    
    # 解析網頁內容
    root = ET.fromstring(response.content)
    
    # 找到所有的"item"元素
    items = root.findall(".//item")
    
    # 如果有"item"元素，則選擇最後一個
    if items:
        last_item = items[-1]
        
        # 找到"title"和"description"元素並印出其文字
        title = last_item.find("title")
        description = last_item.find("description")
        
        if title is not None:
            print("Title:", title.text)
        
        if description is not None:
            print("Description:", description.text)