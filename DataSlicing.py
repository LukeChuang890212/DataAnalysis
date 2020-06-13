import pandas as pd 
from DataProcess import get_source

data = pd.read_excel("時間序列分析資料.xlsx")
data.drop("Unnamed: 0",axis=1,inplace=True)

for i,c in enumerate(data.columns):
    print(i,c)

x = []  
for l in [[2],[i for i in range(3,11)],[i for i in range(20,26)],[i for i in range(56,63)],[65,69,70,74,83,87,88,92]]:
    x[len(x):len(x)] = l
y = 0
category_s = 11
category_e = 19
source = get_source(y,x,category_s,category_e,"Stadium",data)
print("source",source)

#將票房從數量改成百分比
max_capacity = {"台南":12000,"嘉義市":10000,"天母":10000,"斗六":15000,"新莊":12150,"桃園":20000,"洲際":20000,"澄清湖":20000,"花蓮":5500}
capacity = source.Stadium.map(max_capacity)
source.insert(1,"BOX_OFFICE(prob)",source.BOX_OFFICE/capacity)
# source["BOX_OFFICE(prob)"] = source.BOX_OFFICE/capacity
print(source)

# data = pd.concat([data.iloc[:,[0,2,65,69,70,74,83,87,88,92]],data.iloc[:,3:26],data.iloc[:,56:63]],axis=1)

data = source
print(data)
data.to_csv("data for decision tree(update).csv")
print(data.columns)