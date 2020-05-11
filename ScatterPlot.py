import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

analysis_data = pd.read_excel("時間序列分析資料.xlsx")
analysis_data.drop("Unnamed: 0",axis=1,inplace=True)
for col,i in enumerate(analysis_data.columns):
    print(col,i)

days = ["Tue","Wed","Thu","Fri","Sat","Sun"]
average_boxes = []
for day in days:
    average_boxes.append(analysis_data[analysis_data[day] == 1]["BOX_OFFICE"].mean())
for box in average_boxes:
    print(box)   

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.plot(days,average_boxes,'s-',color = 'darkgreen', label="Box office")
plt.title("以週為單位的票房變化")
# 標示x軸(labelpad代表與圖片的距離)
plt.xlabel("星期")
# 標示y軸(labelpad代表與圖片的距離)
plt.ylabel("票房")
# 顯示出線條標記位置
plt.legend()
plt.savefig("以週為單位的票房變化.png")
# 畫出圖片
plt.show()

wheather_datas = ["氣溫(℃)","相對溼度(%)","降水量(mm)"]
for wheather_data in wheather_datas:
    x = analysis_data[wheather_data]
    y = analysis_data["BOX_OFFICE"]
    plt.scatter(x, y, s=75, alpha=.5)
    plt.title(wheather_data+"對票房關係")
    # 標示x軸(labelpad代表與圖片的距離)
    plt.xlabel(wheather_data)
    # 標示y軸(labelpad代表與圖片的距離)
    plt.ylabel("票房")
    # plt.xlim(-1.5, 1.5)
    # plt.xticks(())  # ignore xticks
    # plt.ylim(-1.5, 1.5)
    # plt.yticks(())  # ignore yticks
    plt.savefig("天氣對票房關係散佈圖/"+wheather_data+"對票房關係.png")
    plt.show()
