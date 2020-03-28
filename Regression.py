import pandas as pd
from sklearn.linear_model import Lasso 
from sklearn.linear_model import LinearRegression
import numpy as np

#讀進分析資料
analysis_data = pd.read_excel("時間序列分析資料.xlsx")
analysis_data.drop("Unnamed: 0",axis=1,inplace=True)

class Regression:
    def __init__(self,x_train,y_train,x_test,y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
    def lasso_reg(self,alpha,itr):
        print("lasso regression")

        lasso = Lasso(alpha=alpha, max_iter=itr) 
        lasso.fit(self.x_train,self.y_train) 

        train_score=lasso.score(self.x_train,self.y_train) 
        test_score=lasso.score(self.x_test,self.y_test) 
        coeff_used = np.sum(lasso.coef_!=0)

        print("training score:", train_score) 
        print("test score: ", test_score)
        print("number of features used: ", coeff_used)

        #將使用到的變數印出其係數
        for var,coef in zip(self.x_train,lasso.coef_):
            if(coef == 0):
                continue 
            print(var+":",coef)
    def raw_reg(self):
        print("regression with no regularization")

        reg = LinearRegression()
        reg.fit(self.x_train, self.y_train)

        train_score=reg.score(self.x_train,self.y_train) 
        test_score=reg.score(self.x_test,self.y_test) 
        coeff_used = np.sum(reg.coef_!=0)

        print("training score:", train_score) 
        print("test score: ", test_score)
        print("number of features used: ", coeff_used)




