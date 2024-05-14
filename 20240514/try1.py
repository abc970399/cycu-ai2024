import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 讀取 CSV 檔案
df = pd.read_csv('D:/File/cycu_ai2024/20240514/TDCS_M05A_20240429_180000.csv')

# 只保留 GantryFrom 前兩個字元為 '01' 的列
df = df[df.iloc[:, 1].str[:2] == '01']

# 建立新的 DataFrame
new_df = pd.DataFrame()

# 將 GantryFrom 的第4~7個字元作為新的 X 軸
new_df['X'] = df.iloc[:, 1].apply(lambda x: int(x[3:7]))
new_df['X'] = pd.to_numeric(new_df['X'], errors='coerce').fillna(0)

# 確保 'X' 資料是數字型態
new_df['X'] = pd.to_numeric(new_df['X'], errors='coerce')

# 移除重複的 'X' 資料
new_df = new_df.drop_duplicates(subset='X')

# 將 'X' 資料排序
new_df = new_df.sort_values('X')

# 重設索引
new_df.reset_index(drop=True, inplace=True)


# 將每五行的 TrafficVolume 作為新的 Y 軸
new_df['Y'] = df.iloc[:, 5].iloc[::5]
# 將資料中不是數字的部分替換成0
new_df['Y'] = pd.to_numeric(new_df['Y'], errors='coerce').fillna(0)
# 重設索引
new_df.reset_index(drop=True, inplace=True)

# 使用 CubicSpline 來擬合資料
cs = CubicSpline(new_df['X'], new_df['Y'])

# 繪製擬合曲線
xs = np.arange(min(new_df['X']), max(new_df['X']), 0.1)
plt.plot(xs, cs(xs))
plt.show()