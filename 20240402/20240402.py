import requests
import os

# 設定基本路徑
base_path = "C:\\Users\\User\\Desktop\\cycu_ai2024\\20240402\\basedata\\"

# 迴圈從1到22
for i in range(1, 23):
    # 建立URL
    url = f"https://www.cwa.gov.tw/rss/forecast/36_{str(i).zfill(2)}.xml"
    
    # 獲取網頁內容
    response = requests.get(url)
    
    # 建立檔案路徑
    file_path = os.path.join(base_path, f"36_{str(i).zfill(2)}.xml")
    
    # 寫入檔案
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)