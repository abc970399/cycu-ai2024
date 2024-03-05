import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib.font_manager import FontProperties

# 獲取網頁內容
url = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
response = requests.get(url)

# 解析網頁內容
soup = BeautifulSoup(response.content, "html.parser")

# 找到表格元素
tables = soup.find_all("table")

# 將HTML格轉換為DataFrame
df1= pd.read_html(str(tables[0]))[0]
df2= pd.read_html(str(tables[1]))[0]


#印出 DataFrame
print(df1)
print(df2)


df2 = df2.iloc[:, :2]

#去除油價中沒有值的欄位
df2 = df2.dropna(subset=[df2.columns[1]])


#把第一欄的資料型態轉換成datetime
df2[df2.columns[0]] = pd.to_datetime(df2[df2.columns[0]])



#使用matplotlib繪製折線圖，X軸式日期、Y軸是油價
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # 設定字體為系統的宋體

plt.plot(df2[df2.columns[0]], df2[df2.columns[1]], label='95無鉛汽油')
plt.xlabel('日期', fontproperties=font)
plt.ylabel('油價', fontproperties=font)
plt.title('歷年油價曲線', fontproperties=font)
plt.legend(prop=font)
plt.show()
plt.xlabel('日期')
plt.ylabel('油價')
plt.title('歷年油價曲線')
plt.legend()
plt.show()