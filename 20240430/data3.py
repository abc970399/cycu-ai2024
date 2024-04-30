import os
import pandas as pd
import requests
import time
from io import StringIO

# 儲存所有的 DataFrame
dfs = []

for i in range(0,24):
    for j in range(0, 60, 5):
        time.sleep(1)
        url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/' + str(i).zfill(2) + '/'
        filename = 'TDCS_M03A_20240429_' + str(i).zfill(2) + str(j).zfill(2) + '00.csv'
        urletc = url + filename
        print(urletc)
        # 從網路上讀取資料
        response = requests.get(urletc)
        response.encoding = 'big5'
        # 將資料轉換為 DataFrame
        data = pd.read_csv(StringIO(response.text), header=None)
        dfs.append(data)
        response.close()

# 獲取目錄下的所有文件
directory = 'C:/Users/User/Desktop/cycu_ai2024/20240430/data/'
files = os.listdir(directory)

# 過濾出所有的csv文件
csv_files = [f for f in files if f.endswith('.csv')]

# 為每個csv文件創建一個DataFrame，並將這些DataFrame存儲在一個列表中
for filename in csv_files:
    data = pd.read_csv(directory + filename)
    grouped_data = data.groupby(data.index // 5).apply(lambda x: pd.Series({
        '時間': x.iloc[0, 0] if len(x) > 0 else None,
        '門架': x.iloc[0, 1] if len(x) > 0 else None,
        '方向': x.iloc[0, 2] if len(x) > 0 else None,
        '小客車': x.iloc[-1, 4] if len(x) > 0 else None,
        '小貨車': x.iloc[0, 4] if len(x) > 1 else None,
        '大客車': x.iloc[1, 4] if len(x) > 2 else None,
        '大貨車': x.iloc[2, 4] if len(x) > 3 else None,
        '聯結車': x.iloc[3, 4] if len(x) > 4 else None,
    }))
    dfs.append(grouped_data)

# 合併所有的DataFrame，並忽略原始的索引
merged_df = pd.concat(dfs, ignore_index=True)

# 將合併後的DataFrame保存為csv文件
merged_df.to_csv('C:/Users/User/Desktop/cycu_ai2024/20240430/collect2.csv', index=False)