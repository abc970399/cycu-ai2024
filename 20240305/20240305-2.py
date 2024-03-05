import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib.font_manager import FontProperties

# 獲取網頁內容
url1 = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
response1 = requests.get(url1)

url2 = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx"
response2 = requests.get(url2)

# 解析網頁內容
soup1 = BeautifulSoup(response1.content, "html.parser")
soup2 = BeautifulSoup(response2.content, "html.parser")

# 找到表格元素
tables1 = soup1.find_all("table")
tables2 = soup2.find_all("table")
tables = tables1 + tables2


# 將HTML格轉換為DataFrame
dfs = []
for table in tables:
    df = pd.read_html(str(table))[0]
    dfs.append(df)

df = pd.concat(dfs)

#印出 DataFrame
print(df)

df.to_csv("C:/Users/USER/Desktop/oil2.csv", index=False)


df = df.iloc[:, :5]

#去除油價中沒有值的欄位
df = df.dropna(subset=[df.columns[1]])

#把第一欄的資料型態轉換成datetime
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
# 將第二欄到第五欄的資料型態轉換成數值型態
for i in range(1, 5):
    df[df.columns[i]] = pd.to_numeric(df[df.columns[i]], errors='coerce')

# 使用matplotlib繪製折線圖，X軸式日期、Y軸是油價
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # 設定字體為系統的宋體

plt.plot(df[df.columns[0]], df[df.columns[1]], label='92無鉛汽油')
plt.plot(df[df.columns[0]], df[df.columns[2]], label='95無鉛汽油')
plt.plot(df[df.columns[0]], df[df.columns[3]], label='98無鉛汽油')
plt.plot(df[df.columns[0]], df[df.columns[4]], label='超級柴油')
plt.xlabel('日期', fontproperties=font)
plt.ylabel('油價', fontproperties=font)
plt.title('歷年油價曲線', fontproperties=font)
plt.legend(prop=font)
plt.show()