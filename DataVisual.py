import altair as alt
import pandas as pd
import numpy as np

from IPython.display import display

analysis_data = pd.read_excel("時間序列分析資料.xlsx")
analysis_data.drop("Unnamed: 0",axis=1,inplace=True)
for col,i in enumerate(analysis_data.columns):
    print(col,i)

# np.random.seed(42)
# source = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0).round(2),
#                     columns=['A', 'B', 'C'], index=pd.RangeIndex(100, name='x'))
# print(source)
# source = source.reset_index().melt('x', var_name='category', value_name='y')
# print(source)

# 整理要畫圖用的資料
y = int(input("y column:"))
x = int(input("x column:"))
category_s = int(input("category start column:"))
category_e = int(input("category end column:"))
category = input("category name:")

source = pd.concat([analysis_data.iloc[:,y],analysis_data.iloc[:,x],analysis_data.iloc[:,category_s:category_e+1]],axis=1)
source.insert(0,"index",range(0,source.shape[0]))
# source = source.set_index(list(source.columns[0:3]))
source = source.reset_index().melt(list(source.columns[0:3]), var_name=category, value_name='y')
# source = pd.wide_to_long(source, stubnames='s',i=list(source.columns[0:3]), j=category)
# print(categories)
print(source.head())
source = source[source['y']  == 1].reset_index()
source.drop(["level_0","index",'y'],axis = 1,inplace=True)  
source.drop(0,inplace=True)
source = source[[source.columns[1],source.columns[2],source.columns[0]]].sort_values(source.columns[1]).reset_index()
source.drop(["index"],axis = 1,inplace=True)
print(source)

# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=[source.columns[0]], empty='none')

# The basic line
line = alt.Chart(source).mark_line(interpolate='basis').encode(
    x=source.columns[0]+':Q',
    y=source.columns[2]+':Q',
    color=source.columns[1]+':N'
)

# Transparent selectors across the chart. This is what tells us
# the x-value of the cursor
selectors = alt.Chart(source).mark_point().encode(
    x=source.columns[0]+':Q',
    opacity=alt.value(0),
).add_selection(
    nearest
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw text labels near the points, and highlight based on selection
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, source.columns[2]+':Q', alt.value(' '))
)

# Draw a rule at the location of the selection
rules = alt.Chart(source).mark_rule(color='gray').encode(
    x=source.columns[0]+':Q',
).transform_filter(
    nearest
)

# Put the five layers into a chart and bind the data
alt.layer(
    line, selectors, points, rules, text
).properties(
    width=600, height=300
).save("圖表\chart.html")


