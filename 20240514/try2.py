import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 讀取 CSV 檔案
df = pd.read_csv('D:/File/cycu_ai2024/20240514/TDCS_M05A_20240429_180000.csv')

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
    new_df['X'] = df.iloc[:, 1].apply(lambda x: int(x[3:7]))
    new_df['X'] = pd.to_numeric(new_df['X'], errors='coerce').fillna(0)

    # 確保 'X' 資料是數字型態
    new_df['X'] = pd.to_numeric(new_df['X'], errors='coerce')

    # 移除重複的 'X' 資料
    new_df = new_df.drop_duplicates(subset='X')

    # 將 'X' 資料排序
    new_df = new_df.sort_values('X')


    # 將每五行的 TrafficVolume 作為新的 Y 軸
    new_df['Y'] = df.iloc[:, 5]
    # 將資料中不是數字的部分替換成0
    new_df['Y'] = pd.to_numeric(new_df['Y'], errors='coerce').fillna(0)
    # 重設索引
    new_df.reset_index(drop=True, inplace=True)


    # 使用 CubicSpline 函數
    cs = CubicSpline(new_df['X'], new_df['Y'])

    # 畫圖
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.figure()
    plt.plot(new_df['X'], new_df['Y'], 'o', label='data')
    plt.plot(new_df['X'], cs(new_df['X']), label="Spline")
    plt.title(title)
    plt.legend()
    plt.show()

    # 將整理好的數值分別存成兩個csv檔
    df_north.to_csv('D:/File/cycu_ai2024/20240514/df_north.csv', index=False)
    df_south.to_csv('D:/File/cycu_ai2024/20240514/df_south.csv', index=False)
# 處理資料並畫圖
process_and_plot(df_north, 'NORTH')
process_and_plot(df_south, 'SOUTH')