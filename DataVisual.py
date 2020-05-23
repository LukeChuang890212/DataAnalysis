import altair as alt
import pandas as pd
import numpy as np
from vega_datasets import data

analysis_data = pd.read_excel("時間序列分析資料.xlsx")
analysis_data.drop("Unnamed: 0",axis=1,inplace=True)
for col,i in enumerate(analysis_data.columns):
    print(col,i)

print(data.cars().columns)

