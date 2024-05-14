import os
import pandas as pd

# 指定目錄
dir_path = 'D:\\File\\cycu_ai2024\\20240514\\dataframe\\'
save_path = 'D:\\File\\cycu_ai2024\\20240514\\'

# 獲取目錄下的所有檔案名稱
filenames = os.listdir(dir_path)

# 讀取和組合所有的 CSV 檔案
df_list = []
for filename in filenames:
    if filename.startswith('TDCS_M05A_') and filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(dir_path, filename), names=['time', 'way1', 'way2', 'car', 'speed', 'num'])
        df_list.append(df)
combined_df = pd.concat(df_list)

# 保存組合後的 DataFrame 為新的 CSV 檔案
combined_df.to_csv(os.path.join(save_path, 'combined.csv'), index=False)