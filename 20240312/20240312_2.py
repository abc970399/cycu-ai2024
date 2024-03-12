import pandas as pd
import matplotlib.pyplot as plt

# 讀取CSV檔案
df = pd.read_csv('C:\\Users\\User\\Desktop\\cycu_ai2024\\20240312\\112年1-10月交通事故簡訊通報資料.csv')

# 過濾出國道一號的數據
df['國道名稱'] = df['國道名稱'].fillna('')
df = df[df['國道名稱'].str.contains('國道1號')]
df = df[df['方向'].str.contains('南|南向')]
# 統計每個里程數出現的次數
grouped = df['里程'].value_counts().reset_index()
grouped.columns = ['里程', 'count']


event_data = df[['年', '月', '日', '時', '分', '事件發生', '事件排除']]
# 將'事件發生' '事件排除'的時間轉換成分鐘單位
event_data['事件發生'] = pd.to_datetime(event_data['事件發生'])
event_data['事件排除'] = pd.to_datetime(event_data['事件排除'])
event_data['事件持續時間'] = (event_data['事件排除'] - event_data['事件發生']).dt.total_seconds() / 60
# 將'年', '月', '日', '時', '分'的時間資料轉換成分鐘，若有nan則替除該筆數據
event_data['年'] = event_data['年'].fillna(0).astype(int)
event_data['月'] = event_data['月'].fillna(0).astype(int)
event_data['日'] = event_data['日'].fillna(0).astype(int)
event_data['時'] = event_data['時'].fillna(0).astype(int)
event_data['分'] = event_data['分'].fillna(0).astype(int)

event_data['時間'] = event_data['年'] * 525600 + event_data['月'] * 43800 + event_data['日'] * 1440 + event_data['時'] * 60 + event_data['分']
event_data = event_data[event_data['時間'] != 0]


# 將'時間'按照時間排序
event_data = event_data.sort_values('時間')


# 繪製由時序拍裂的與里程有關的棒狀圖
plt.bar(event_data['時間'], event_data['事件持續時間'], width=1, align='edge')
plt.xlabel('時間')
plt.ylabel('事件持續時間')
plt.xticks(range(0, event_data['時間'].max()+1, 60))
plt.title('事件持續時間與里程的關係')
plt.xticks(rotation=45)
plt.show()