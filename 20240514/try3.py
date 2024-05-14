from datetime import date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# 讀取 CSV 檔案
df = pd.read_csv('D://File//cycu_ai2024//20240514//combined.csv')
# 刪除第一行資料
#df = df.iloc[1:]
# 只保留 GantryFrom 前兩個字元為 '01' 的列
df = df[df.iloc[:, 1].str[:2] == '01']

# 分成 '北上' 和 '南下' 兩個 DataFrame
df_north = df[df.iloc[:, 1].str[-1] == 'N']
df_south = df[df.iloc[:, 1].str[-1] == 'S']

# 建立處理資料並畫圖的函數
def process_and_plot(df, title):
    # 建立新的 DataFrame
    new_df = pd.DataFrame()

    # 將 GantryFrom 的第4~7個字元作為新的 X 軸
    new_df['Y'] = df.iloc[:, 1].apply(lambda x: int(x[3:7]))
    new_df['Y'] = pd.to_numeric(new_df['Y'], errors='coerce').fillna(0)

    # 確保 'Y' 資料是數字型態
    new_df['Y'] = pd.to_numeric(new_df['Y'], errors='coerce')

    # 移除重複的 'Y' 資料
    new_df = new_df.drop_duplicates(subset='Y')

    # 將 'Y' 資料排序
    new_df = new_df.sort_values('Y')


    # 將每五行的 TrafficVolume 作為新的 Z 軸
    new_df['Z'] = df.iloc[:, 5]
    # 將資料中不是數字的部分替換成0
    new_df['Z'] = pd.to_numeric(new_df['Z'], errors='coerce').fillna(0)
    # 重設索引
    new_df.reset_index(drop=True, inplace=True)

    # 將時間欄位作為新的 X 軸
    new_df['X'] = pd.to_datetime(df.iloc[:, 0])
    new_df = new_df.sort_values('X')
    # 確保 'X' 資料是數字型態
    new_df['X'] = pd.to_numeric(new_df['Y'], errors='coerce')

    # 移除重複的 'X' 資料
    new_df = new_df.drop_duplicates(subset='X')

    # 將 'X' 資料排序
    new_df = new_df.sort_values('X')
    # 創建一個 X 變數來存儲你的 x 座標
    X = np.linspace(new_df['X'].min(), new_df['X'].max(), num=100)
    
    print (df_north)
# 創建一個新的圖形 
# 畫出多視角圖形  重 111, 110, 101, 100
# add four subplots to the figure
# subplot(111) is subplot(111,portjection='3d')

# 對時間和里程數據進行網格化
# 假設 x (時間) 和 y (里程) 已經是規則的網格數據
x = np.linspace(df_north.iloc[:, 0].min(), df_north.iloc[:, 0].max(), num=50)  # 調整 num 以匹配數據點的密度  # 調整 num 以匹配數據點的密度
y = np.linspace(df_north.iloc[:, 1].min(), df_north.iloc[:, 1].max(), num=50)  # 調整 num 以匹配數據點的密度
x, y = np.meshgrid(x, y)

# 插值找到每個 (x, y) 點對應的 z (車流量)
from scipy.interpolate import griddata
z = griddata((df_north[:, 0], df_north[:, 1]), df_north[:, 2], (x, y), method='cubic')


fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
# 繪製曲面圖
surf = ax.plot_surface(x, y, z, cmap='viridis')

# 添加顏色條
#fig.colorbar(surf)

# 設置坐標軸標籤
ax.set_xlabel('Time')
ax.set_ylabel('Mileage')
ax.set_zlabel('Traffic Volume')


ax1 = fig.add_subplot(122, projection='3d')
# 繪製曲面圖
surf = ax1.plot_surface(x, y, z, cmap='viridis')
# 設置坐標軸標籤
ax1.set_xlabel('Time')
ax1.set_ylabel('Mileage')
ax1.set_zlabel('Traffic Volume')
ax1.view_init(elev=45, azim=60)

plt.tight_layout()
# 顯示圖形
plt.savefig('cubicspline_2v.png')
print(df_north)