import geopandas as gpd

# 設定檔案路徑
file_path = "C:\\Users\\User\\Desktop\\cycu_ai2024\\20240402\\mapdata202301070205\\COUNTY_MOI_1090820.shp"

# 讀取Shapefile檔案
data = gpd.read_file(file_path)



# 印出DataFrame的內容
print(data)

