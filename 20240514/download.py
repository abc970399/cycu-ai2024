import os
import requests
import shutil
import datetime

# 建立下載和保存檔案的函數
def download_and_save(url, save_dir, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # 確保保存目錄存在
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        # 保存檔案
        with open(os.path.join(save_dir, filename), 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)

# 基礎 URL
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/"

# 設定日期
date = datetime.datetime(2024, 4, 29)

# 對於每個小時和每五分鐘
for hour in range(24):
    for minute in range(0, 60, 5):
        # 生成 URL 和檔案名稱
        date_str = date.strftime("%Y%m%d")
        time_str = f"{hour:02d}{minute:02d}00"
        url = f"{base_url}{date_str}/{hour:02d}/TDCS_M05A_{date_str}_{time_str}.csv"
        filename = f"TDCS_M05A_{date_str}_{time_str}.csv"

    
        # 下載和保存檔案
        download_and_save(url, 'D:\\File\\cycu_ai2024\\20240514\\dataframe\\', filename)