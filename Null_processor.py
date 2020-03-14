import pandas as pd
import numpy as np

import datetime 
import time

import math

#讀進球場與觀測站對應資料
station_stadium_df = pd.read_excel("新各球場對應觀測站.xlsx")
station_list = list(station_stadium_df["station"])

#處理空值時，找前後兩天的非空值資料然後算平均填補空值
def find_all_not_null_date_and_data(weather_data_df,col_name,station,is_null_date,deltadays,dates,datas,date0_found=False,try_times=0):
    near_date = is_null_date + datetime.timedelta(days= deltadays)
    # print(weather_data_df.index)
    data = weather_data_df.loc[(str(near_date)[0:10],station),col_name].tolist()[0]
    if(not math.isnan(data)):
        # print(data)
        print("data found!!!!")
        print("data:",data)
        dates.append(near_date) 
        datas.append(data)
        if(date0_found):
            pass
        else:
            find_all_not_null_date_and_data(weather_data_df,col_name,station,near_date,deltadays,dates,datas,date0_found=True,try_times=7) 
    else:
        print("data not found QQ")
        #七次內找不到的話就算了
        if(try_times<=7):
            print("date:",near_date)
            print("try_times",try_times)
            find_all_not_null_date_and_data(weather_data_df,col_name,station,near_date,deltadays,dates,datas,date0_found=False,try_times=try_times+1)
def find_station_in_whole_data(whole_data):
    #處理station_stadium_df
    try:
        station_stadium_df.drop("Unnamed: 0",axis=1,inplace=True)
    except:
        pass
    station_stadium_df.set_index("stadium",inplace=True)
    print(station_stadium_df)

    stadiums = list(whole_data["STADIUM"])
    stations = []
    for stadium in enumerate(stadiums,start=0):
        station = station_stadium_df.loc[stadium[1]]
        play_time = whole_data.iloc[stadium[0],2]
        if isinstance(station,pd.Series):
            start_time = station["start_time"]
            end_time = station["end_time"]
            print("play_time",play_time)
            print("\n","station",station,"\n")
            print("start_time:",start_time)
            print("end_time",end_time)
            print("found_station:",station["station"])
            stations.append(station["station"])
        else:
            print("\n","station",station,"\n")
            print("play_time",play_time)
            for station_id in range(station.shape[0]):
                start_time = station.iloc[station_id]["start_time"]
                end_time = station.iloc[station_id]["end_time"]
                print("start_time",start_time)
                print("end_time",end_time)
                if(start_time <= play_time and play_time <= end_time):
                    print("found_station:",station.iloc[station_id]["station"])
                    stations.append(station.iloc[station_id]["station"])
                    # print("station",station[station.start_time == start_time]["station"])
                    break
                else:
                    continue
    print(len(stations))
    return stations
    # input("continue")

def fill_null(whole_data):
    #紀錄有沒有發生錯誤
    error = []

    #讀進天氣資料
    weather_data_df = pd.read_excel("需要的天氣資料.xlsx")

    #將station併入每一筆資料
    station_in_whole_data = find_station_in_whole_data(whole_data)
    whole_data.insert(0,"station",station_in_whole_data)
    print(whole_data)
    # input("continue")

    #找出有空值的欄位
    any_null_cols = whole_data.isnull().any()[whole_data.isnull().any().values == True].index
    print(any_null_cols)
    

    #將有空值的欄位弄成is_null_table
    is_null_table = whole_data[any_null_cols].isnull()
    print(is_null_table)
    # input("continue")

    #將同一天各觀測站的資料排在一起以利後續查找資料
    weather_data_df.set_index(["DATE","STATION",],drop=False,append=False,inplace=True)
    weather_data_df.sort_index(level=0,inplace=True)
    print(weather_data_df)
    print(weather_data_df.index)
    # input("continue")

    #紀錄有多少空值
    null_num = 0
    for col in any_null_cols:
        print("正在處理空值的欄位:",col)

        #找有空值的列
        null_data = is_null_table[is_null_table[col].isin([True])]
        null_num += null_data.shape[0]
        print(null_data)

        #找有空值的格及對應的觀測站和日期
        for data_index in null_data.index:
            station = whole_data.iloc[data_index]["station"]
            print("處理空值的觀測站:",station)
            date = whole_data.iloc[data_index]["DATE"]
            print("有空值的日期:",date)
            # input("continue")

            dates=[]
            datas=[]
            #分往前和往後找非Null的值(利用deltadays=-1 or +1)，收集前後七天內找的到的資料
            for deltadays in [-1,1]:
                #先找離is_null_date近的再找遠的
                find_all_not_null_date_and_data(weather_data_df,col,station,date,deltadays,dates,datas,date0_found=False,try_times=0)
            try:
                print("上上一次無空值的日期",dates[1],"數值",datas[1],"\n")
                print("上一次無空值的日期",dates[0],"數值",datas[0],"\n")
                print("下一次無空值的日期",dates[2],"數值",datas[2],"\n")
                print("下下一次無空值的日期",dates[3],"數值",datas[3],"\n")
            except Exception as e:
                error.append(e)
            average = sum(datas)/len(datas)
            print("平均值:",average)

            #將找到的平均值用來填補空值
            whole_data.loc[data_index,col] = average

    for e in error:
        print(e)
    print("以上是錯誤訊息")
    print("空值數目:",null_num)
    input("continue")

    whole_data.drop("station",axis=1,inplace=True)
    return whole_data