import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
# from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn import preprocessing
import numpy as np
import math
import re

def scale_x(df):
    print(df)
    cols = df.columns
    print(cols)
    input("continue")
    for col in cols:
        # re.search("氣溫(℃)",col) or re.search("相對溼度(%)",col)
        col_list = ["氣溫(℃)","相對溼度(%)","Previous_氣溫(℃)","Previous_相對溼度(%)"]
        if(col in col_list):
            print(df[col])
            df[col] = df[col]/10
            print(df[col])
        if(col == "Previous_TIME"):
            print(df[col])
            df[col] = df[col]/60
            print(df[col])
        if(col == "Previous_BOX_OFFICE"):
            print(df[col])
            df[col] = df[col]/1000
            print(df[col])
    return df
def scale_y(s):
    print(s)
    s = s/1000
    print(s)
    return s



