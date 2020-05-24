import altair as alt
import pandas as pd
import numpy as np

import Visualizer as vs
from vega_datasets import data

import datetime

analysis_data = pd.read_excel("時間序列分析資料.xlsx")
analysis_data.drop("Unnamed: 0",axis=1,inplace=True)
for col,i in enumerate(analysis_data.columns):
    print(col,i)

#將資料切成一年一年
split_date = datetime.datetime.strptime("2018-03-24", "%Y-%m-%d")
split_index = analysis_data[analysis_data.DATE == split_date].index.tolist()[0]
analysis_data = analysis_data.iloc[0:split_index,:]
print(analysis_data.tail())

#寫成get_source()
def get_source(y,x,category_s,category_e,category,analysis_data):
    source = pd.concat([analysis_data.iloc[:,y],analysis_data.iloc[:,x],analysis_data.iloc[:,category_s:category_e+1]],axis=1)
    source.insert(0,"index",range(0,source.shape[0]))
    # source = source.set_index(list(source.columns[0:3]))
    source = source.reset_index().melt(list(source.columns[0:3]), var_name=category, value_name='y')
    print(source.head())
    source = source[source['y']  == 1].reset_index()
    source.drop(["level_0","index",'y'],axis = 1,inplace=True)  
    source.drop(0,inplace=True)
    source = source[[source.columns[1],source.columns[2],source.columns[0]]].sort_values(source.columns[1]).reset_index()
    source.drop(["index"],axis = 1,inplace=True)
    # source[source.columns[0]] =source[source.columns[0]].astype("int64")
    print(source)
    return source

# 整理要畫圖用的資料
y = int(input("y column:"))
x = int(input("x column:"))
# category_s = int(input("category start column:"))
# category_e = int(input("category end column:"))
category = input("category name:")

for i in range(11,20):
    category_s = i
    category_e = i

    source = get_source(y,x,category_s,category_e,category,analysis_data)

    #將票房從數量改成百分比
    max_capacity = {"台南":12000,"嘉義市":10000,"天母":10000,"斗六":15000,"新莊":12150,"桃園":20000,"洲際":20000,"澄清湖":20000,"花蓮":5500}
    capacity = source[source.columns[1]].map(max_capacity)
    source[source.columns[2]] = source[source.columns[2]]/capacity
    print(source)

    # vs.plot_line_graph(source)
    vs.plot_line_graph_by_date(source)
