import os
import requests
import shutil
import tarfile
import datetime
import urllib.request

def url_exists(url):
    response = requests.head(url)
    return response.status_code == 200

def download_and_save(url, save_dir, filename):
    if os.path.exists(os.path.join(save_dir, filename)):
        print(f"{filename} already exists. Skipping download.")
        return
    if url_exists(url):
        os.makedirs(save_dir, exist_ok=True)
        urllib.request.urlretrieve(url, os.path.join(save_dir, filename))
        if filename.endswith('.tar.gz'):
            with tarfile.open(os.path.join(save_dir, filename), 'r:gz') as tar:
                tar.extractall(path=save_dir)
            os.remove(os.path.join(save_dir, filename))

base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/"

start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 4, 30)

current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y%m%d")
    tar_url = f"{base_url}M05A_{date_str}.tar.gz"
    tar_filename = f"M05A_{date_str}.tar.gz"
    download_and_save(tar_url, 'D:\\File\\cycu_ai2024\\20240521\\dataframe\\', tar_filename)
    if not os.path.exists(os.path.join('D:\\File\\cycu_ai2024\\20240521\\dataframe\\', tar_filename)):
        for hour in range(24):
            for minute in range(0, 60, 5):
                csv_url = f"{base_url}{date_str}/{str(hour).zfill(2)}/TDCS_M05A_{date_str}_{str(hour).zfill(2)}{str(minute).zfill(2)}00.csv"
                csv_filename = f"M05A_{date_str}_{str(hour).zfill(2)}{str(minute).zfill(2)}00.csv"
                csv_save_dir = os.path.join('D:\\File\\cycu_ai2024\\20240521\\dataframe\\', date_str, str(hour).zfill(2))
                download_and_save(csv_url, csv_save_dir, csv_filename)
    current_date += datetime.timedelta(days=1)