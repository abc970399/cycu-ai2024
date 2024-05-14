#!/bin/python
import io
import requests
import datetime
import requests
import pandas as pd



# M03A : TimeInterval、GantryID、Direction、VehicleType、交通量
# M04A : TimeInterval、GantryFrom、GantryTo、VehicleType、TravelTime、交通量
# M05A : TimeInterval、GantryFrom、GantryTo、VehicleType、SpaceMeanSpeed、交通量
# M06A : VehicleType、DetectionTime_O、GantryID_O、DetectionTime_D、GantryID_D、TripLength、TripEnd、TripInformation

data_columns = {
    'M03A':['TimeInterval','GantryID','Direction','VehicleType','TrafficVolume'],
    'M04A':['TimeInterval','GantryFrom','GantryTo','VehicleType','TravelTime','TrafficVolume'],
    'M05A':['TimeInterval','GantryFrom','GantryTo','VehicleType','SpaceMeanSpeed','TrafficVolume']
    }

#define a function to get one day data
def get_one_day_data(year, month, day, data_type):

    today = datetime.datetime(year, month, day, 0, 0, 0)

    if data_type not in data_columns:
        raise ValueError('data_type should be one of M03A, M04A, M05A, M06A')
       
    df_columns = data_columns[data_type]

    target_df = pd.DataFrame(columns=df_columns)

    # sample url https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/00/TDCS_M05A_20240430_005500.csv
    for i in range(0, 288):
        timestep = today + datetime.timedelta(minutes=5*i)
        timestep_str_d = timestep.strftime('%Y%m%d')
        timestep_str_h = timestep.strftime('%H')
        timestep_str_m = timestep.strftime('%H%M00')

        filename = 'TDCS_' + data_type + '_' + timestep_str_d + '_' + timestep_str_m + '.csv'

        url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/' + data_type + '/' + timestep_str_d + '/' + timestep_str_h + '/' + filename

        print(url)
        r = requests.get(url)

        # convert r to dataframe without column names in the first row
        # specify header=None to avoid the first row being treated as column names
        # column names will be {'t','g','d','vtype','num'}
        df = pd.read_csv(io.StringIO(r.text), header=None)
        df.columns = df_columns
        
        target_df = pd.concat([target_df, df], ignore_index=True)
        print (target_df.head(), target_df.tail(), target_df.shape)


        output_dir = 'D:/File/cycu_ai2024/20240507/data/'
        output_filename = output_dir + 'TDCS_' + data_type + '_' + timestep_str_d + '.csv'


    # Specify the directory where the file will be saved
    output_dir = 'D:/File/cycu_ai2024/20240507/data/'
    output_filename = output_dir + 'TDCS_' + data_type + '_' + timestep_str_d + '.csv'
    target_df.to_csv(output_filename, index=False)

    return target_df



if __name__ == '__main__':
    # Get data for April 30, 2024
    df = get_one_day_data(2024, 4, 30, 'M05A')

    print(df.head(), df.tail(), df.shape)

    df_31 = df [df['VehicleType'] == 31]
    df_32 = df [df['VehicleType'] == 32]
    df_41 = df [df['VehicleType'] == 41]
    df_42 = df [df['VehicleType'] == 42]
    df_5  = df [df['VehicleType'] == 5]

    df_31.reset_index(drop=True, inplace=True)
    df_32.reset_index(drop=True, inplace=True)
    df_41.reset_index(drop=True, inplace=True)
    df_42.reset_index(drop=True, inplace=True)
    df_5.reset_index(drop=True, inplace=True)

    df_5['tv31']    = df_31['TrafficVolume']
    df_5['tv32']    = df_32['TrafficVolume']
    df_5['tv41']    = df_41['TrafficVolume']
    df_5['tv42']    = df_42['TrafficVolume']
    df_5['tv5']     = df_5['TrafficVolume']

    # drop columns VehicleType and TrafficVolume
    df_5 = df_5.drop(columns=['VehicleType', 'TrafficVolume'])

    print(df_5.head(), df_5.tail(), df_5.shape)
