import pandas as pd
import folium

# 讀取CSV文件，使用'big5'編碼，跳過第一行
df = pd.read_csv('C:\\Users\\User\\Desktop\\cycu_ai2024\\20240409\\地震活動彙整_638482849776798722.csv', encoding='big5', skiprows=1)

# 提取需要的列
df = df[['地震時間', '經度', '緯度', '規模']]

# 將列名轉換為英文
df.columns = ['time', 'longitude', 'latitude', 'magnitude']

# 將經度和緯度轉換為數值型
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')

# 過濾掉缺失值
df = df.dropna(subset=['time', 'longitude', 'latitude', 'magnitude'])

# 提取經度和緯度的平均值
latitude = df['latitude']
longitude = df['longitude']

# 創建一個地圖對象
m = folium.Map(location=[latitude.mean(), longitude.mean()], zoom_start=6)
# 將點添加到地圖上，並包含時間、座標、規模，點位圖例依照規模大小改變，規模小於等於2為藍色，規模3為綠色，規模4為黃色，規模5為橘色，規模6及以上為紅色，且規模越大圖例越大，每個圖例大小相差一倍
for index, row in df.iterrows():
    folium.CircleMarker(location=[row['latitude'], row['longitude']],
                        radius=row['magnitude'],
                        color='red' if row['magnitude'] >= 6 else 'orange' if row['magnitude'] == 5 else 'yellow' if row['magnitude'] == 4 else 'lightgreen' if row['magnitude'] == 3 else 'blue',
                        fill=True,
                        fill_color='red' if row['magnitude'] >= 6 else 'orange' if row['magnitude'] == 5 else 'yellow' if row['magnitude'] == 4 else 'lightgreen' if row['magnitude'] == 3 else 'blue',
                        fill_opacity=0.6,
                        popup=f"Time: {row['time']}<br>Latitude: {row['latitude']}<br>Longitude: {row['longitude']}<br>Magnitude: {row['magnitude']}").add_to(m)
# 將地圖保存為HTML
m.save('C:\\Users\\User\\Desktop\\cycu_ai2024\\20240409\\earthquake_locations4.html')
