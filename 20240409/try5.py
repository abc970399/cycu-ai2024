import pandas as pd
import folium

# 讀取 CSV 檔案
df = pd.read_csv('D:\\File\\cycu_ai2024\\20240409\\地震活動彙整_638483048004417544.csv', encoding='big5', skiprows=1)

# 將 "地震時間" 列轉換為 datetime 對象，並按照時間排序
df['地震時間'] = pd.to_datetime(df['地震時間'])
df = df.sort_values('地震時間')

# 讀取'經度'和'緯度'列
longitude = df['經度']
latitude = df['緯度']

# 創建一個地圖對象
m = folium.Map(location=[latitude.mean(), longitude.mean()], zoom_start=6)

# 創建一個用於存儲地點的列表
locations = []
# 將地點添加到地圖上
for index, row in df.iterrows():
    locations.append({
        'coordinates': [row['緯度'], row['經度']],
        'time': row['地震時間'].isoformat() if pd.notnull(row['地震時間']) else None,
        'properties': {
            'popup': str(row.to_dict()),  # 顯示所有資料
            'icon': 'circle',
            'iconstyle': {
                'fillColor': 'red' if row['規模'] >= 6 else 'orange' if row['規模'] == 5 else 'yellow' if row['規模'] == 4 else 'lightgreen' if row['規模'] == 3 else 'blue',
                'fillOpacity': 0.6,
                'stroke': 'false',
                'radius': row['規模']
            }
        }
    })

# 保存地圖
m.save('D:\\File\\cycu_ai2024\\20240409\\earthquake_locations8.html')