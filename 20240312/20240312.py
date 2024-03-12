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
# 印出事故次數
print(grouped)
# 將里程按照數字小到大排列
grouped = grouped.sort_values('里程')

print(grouped)

# 將數據另存於原始資料夾，命名為'國道一號'
df.to_csv('C:\\Users\\User\\Desktop\\cycu_ai2024\\20240312\\國道一號_S.csv', index=False)
# 繪製長條圖
grouped.plot(kind='bar', x='里程', y='count')
plt.xticks(range(0, len(grouped), 60), grouped['里程'][::60])
plt.xlabel('里程數')
plt.ylabel('次數')
plt.show()

max_count_row = grouped.loc[grouped['count'].idxmax()]
max_count_mileage = max_count_row['里程']
print("The mileage with the highest count is:", max_count_mileage)