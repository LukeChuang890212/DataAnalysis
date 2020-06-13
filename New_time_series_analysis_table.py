import pandas as pd
import Null_processor
import DataProcess

shift_days = int(input("shift_days:"))

whole_data = pd.read_excel("temp.xlsx")
whole_data.drop("Unnamed: 0",axis=1,inplace=True)
print(whole_data)

#填補空值
whole_data = Null_processor.fill_null(whole_data)
#輸出確認有沒有真的填補了空值
whole_data.to_excel("whole_data with no null.xlsx")
input("continue")

#將欄位位置稍作調整以利時間序列之處理
cols = whole_data.columns
col_list = list(cols)
col_list = col_list[0:4]+col_list[cols.get_loc("HOST_LAMIGO桃猿"):]+col_list[4:cols.get_loc("HOST_LAMIGO桃猿")]
whole_data = whole_data[col_list]
print(whole_data)

for i,c in enumerate(whole_data.columns):
    print(i,c)
whole_data = DataProcess.add_game_res(whole_data)

#準備時間序列分析用的資料格式
cols = whole_data.columns 
previous_data = whole_data.iloc[:,cols.get_loc("HOST_LAMIGO桃猿"):].add_prefix("Previous_")
box_office_the_day = whole_data["BOX_OFFICE"]
previous_data.insert(0,"Previous_BOX_OFFICE",box_office_the_day)
previous_data = previous_data.shift(shift_days)
analysis_data = pd.concat([whole_data.iloc[:,0:cols.get_loc("降水量(mm)")+1],previous_data],axis=1).iloc[shift_days:,:].reset_index(drop=True)
analysis_data.drop(["Previous_index.1","STADIUM"],axis=1,inplace=True)
print(analysis_data.columns)
analysis_data.to_excel("時間序列分析資料.xlsx")

