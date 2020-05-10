import pandas as pd
from sklearn.linear_model import Lasso 
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
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
        record = []
        max_test_score = -100
        while(alpha != 0):
            print("During computation...")
            lasso = Lasso(alpha=alpha, max_iter=itr) 
            lasso.fit(self.x_train,self.y_train) 

            train_score=lasso.score(self.x_train,self.y_train) 
            test_score=lasso.score(self.x_test,self.y_test) 
            coeff_used = np.sum(lasso.coef_!=0)

            record.append([alpha,train_score,test_score,coeff_used,lasso.coef_])    
            if(test_score > max_test_score):
                max_test_score = test_score
            alpha = round(alpha-0.001,3)

        record = pd.DataFrame(record, columns=['alpha', 'train_score','test_score','coeff_used','lasso.coef_']) 
        # print(record)
        # print(record[record["test_score"] == max_test_score])
        record = record[record["test_score"] == max_test_score].iloc[0,:]

        print("lasso regression with alpha="+str(record["alpha"]),"\n")
        print("training score:", record["train_score"]) 
        print("test score: ", record["test_score"])
        print("number of features used: ", record["coeff_used"])

        #將使用到的變數印出其係數
        print("Selected variables:")
        for var,coef in zip(self.x_train,record["lasso.coef_"]):
            if(coef == 0):
                continue 
            print(var+":",coef)
        print("-------------------------------------------------------")
    def raw_reg(self):
        print("regression with no regularization","\n")

        reg = LinearRegression()
        reg.fit(self.x_train, self.y_train)

        train_score=reg.score(self.x_train,self.y_train) 
        test_score=reg.score(self.x_test,self.y_test) 
        coeff_used = np.sum(reg.coef_!=0)

        print("training score:", train_score) 
        print("test score: ", test_score)
        print("number of features used: ", coeff_used)
        print("-------------------------------------------------------")
    def reg_with_rfe(self):
        print("regression after RFE","\n")

        reg = LinearRegression()
        selector = RFE(reg)
        selector.fit(self.x_train, self.y_train)

        train_score=selector.score(self.x_train,self.y_train) 
        test_score=selector.score(self.x_test,self.y_test) 
        coeff_used = selector.n_features_

        print("training score:", train_score) 
        print("test score: ", test_score)
        print("number of features used: ", coeff_used)

        #將使用到的變數印出其係數
        # for var in selector.estimator_.coef_:
        print("Selected variables:")    
        for var,coef in zip(self.x_train.columns,selector.estimator_.coef_):
            if(coef == 0):
                continue 
            print(str(var)+":",coef)
        print("-------------------------------------------------------")



