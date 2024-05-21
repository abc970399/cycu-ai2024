import os
import pandas as pd

directory = 'C:/Users/User/Desktop/cycu_ai2024/20240430/data/'
filename = 'TDCS_M03A_20240429_000000.csv'
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


# 印出結果
print(grouped_data)