import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D


df = pd.read_csv('D:/File/cycu_ai2024/20240507/data/TDCS_M05A_20240430_processed2.csv')


def speed_to_color(speed):
    if speed < 20:
        return 'purple'
    elif 20 <= speed < 40:
        return 'red'
    elif 40 <= speed < 60:
        return 'orange'
    elif 60 <= speed < 80:
        return 'yellow'
    else:
        return 'green'

df['color'] = df['SpaceMeanSpeed'].apply(speed_to_color)


# 創建 3D 圖形
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
# 繪製南向的 3D 散點圖
ax1.scatter(df['TimeInterval'], df['GantryFrom'], df['TrafficVolume'], c=df['color'], s=10)
# 設定軸標籤軸標籤
ax1.set_xlabel('Time')
ax1.set_ylabel('Mileage')
ax1.set_zlabel('Number of cars')

# 顯示圖表
plt.show()

plt.show()
#下載圖片
fig.savefig('D:/File/cycu_ai2024/20240507/data/01.png')