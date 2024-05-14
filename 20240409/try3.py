import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
# 讀取CSV文件，並將其轉換為DataFrame
df = pd.read_csv('D:\\File\\cycu_ai2024\\20240409\\地震活動彙整_638483048004417544.csv', encoding='big5', skiprows=1)
# 假設df是您的DataFrame，並且'地震時間'是其中的一個列
df['地震時間'] = pd.to_datetime(df['地震時間'])  # 將'地震時間'轉換為datetime格式
df = df.sort_values('地震時間')  # 根據'地震時間'對數據進行排序

# 讀取'經度'和'緯度'列
longitude = df['經度']
latitude = df['緯度']

# 創建一個地圖對象
m = folium.Map(location=[latitude.mean(), longitude.mean()], zoom_start=6)

# 創建一個用於存儲地點的列表
locations = []

# 將地點添加到列表中
for index, row in df.iterrows():
    locations.append({
        'coordinates': [row['緯度'], row['經度']],
        'time': row['地震時間'].isoformat(),
        'properties': {
            'popup': f"Time: {row['地震時間']}<br>Latitude: {row['緯度']}<br>Longitude: {row['經度']}<br>Magnitude: {row['規模']}",
            'icon': 'circle',
            'iconstyle': {
                'fillColor': 'red' if row['規模'] >= 6 else 'orange' if row['規模'] == 5 else 'yellow' if row['規模'] == 4 else 'lightgreen' if row['規模'] == 3 else 'blue',
                'fillOpacity': 0.6,
                'stroke': 'false',
                'radius': row['規模']
            }
        }
    })

# 將地點添加到地圖上
TimestampedGeoJson(locations, period='PT1H', add_last_point=True).add_to(m)

# 將地圖保存為HTML，並將其保存到指定的路徑
m.save('D:\\File\\cycu_ai2024\\20240409\\earthquake_locations8.html')