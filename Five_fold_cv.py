# from sklearn.cross_validation import cross_val_score
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
# from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

analysis_data = pd.read_excel("時間序列分析資料.xlsx")
analysis_data.drop("Unnamed: 0",axis=1,inplace=True)
print(analysis_data.info())

x = analysis_data.iloc[:,3:]
y = analysis_data["BOX_OFFICE"] 

reg = LinearRegression().fit(x, y)
print(reg.score(x, y))

