import pandas as pd 
from DataProcess import get_source

data = pd.read_excel("data for decision tree(update).xlsx")
data.drop("Unnamed: 0",axis=1,inplace=True)

for i,c in enumerate(data.columns):
    print(i,c)
input("continue")

x = []  
for l in [[2],[i for i in range(9,31)]]:
    x[len(x):len(x)] = l
y = [0,1]
category_s = 3
category_e = 8
source = get_source(y,x,category_s,category_e,"Day",data)
print("source",source)

#將票房從數量改成百分比
# max_capacity = {"台南":12000,"嘉義市":10000,"天母":10000,"斗六":15000,"新莊":12150,"桃園":20000,"洲際":20000,"澄清湖":20000,"花蓮":5500}
# capacity = source.Stadium.map(max_capacity)
# source.insert(1,"BOX_OFFICE(prob)",source.BOX_OFFICE/capacity)
# source["BOX_OFFICE(prob)"] = source.BOX_OFFICE/capacity
print(source)

# data = pd.concat([data.iloc[:,[0,2,65,69,70,74,83,87,88,92]],data.iloc[:,3:26],data.iloc[:,56:63]],axis=1)

data = source
print(data)
data.to_excel("data for decision tree(update).xlsx")
print(data.columns)