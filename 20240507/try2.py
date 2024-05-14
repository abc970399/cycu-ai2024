import pandas as pd
import datetime

# 讀取 CSV 檔案
df = pd.read_csv('D:/File/cycu_ai2024/20240507/data/TDCS_M05A_20240430.csv')

# 特徵化每一欄
df['TimeInterval'] = df['TimeInterval'].apply(lambda x: (datetime.datetime.strptime(x, '%Y/%m/%d %H:%M').hour * 60 + datetime.datetime.strptime(x, '%Y/%m/%d %H:%M').minute) // 5 + 1)
df['GantryFrom'] = df['GantryFrom'].apply(lambda x: int(''.join([c for c in x[2:7] if not c.isalpha()])) if x[:2] == '01' else x)
df['GantryTo'] = df['GantryTo'].apply(lambda x: 1 if x == 'N' else 2)
df.drop(columns=['GantryTo'], inplace=True)

# 車種特徵
vehicle_features = pd.DataFrame(df['VehicleType'].apply(lambda x: [1 if x == i else 0 for i in [31, 32, 41, 42, 5]]).tolist(), columns=['tv31', 'tv32', 'tv41', 'tv42', 'tv5'])
df = pd.concat([df, vehicle_features], axis=1)

df = df[df['GantryFrom'].apply(lambda x: len(str(x)) <= 5)]
df.drop(columns=['VehicleType'], inplace=True)

# 儲存到新的 CSV 檔案
df.to_csv('D:/File/cycu_ai2024/20240507/data/TDCS_M05A_20240430_processed2.csv', index=False)