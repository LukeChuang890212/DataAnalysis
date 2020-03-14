import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_corr_matrix(df):
    dfData = df.corr()
    plt.subplots(figsize=(50, 50)) # 設定畫面大小
    sns.heatmap(dfData, annot=False, vmax=1, square=True, cmap="Blues")
    plt.savefig('相關係數矩陣.png')
    plt.show()

analysis_data = pd.read_excel("時間序列分析資料.xlsx")
analysis_data.drop("Unnamed: 0",axis=1,inplace=True)
print(analysis_data.info())
# plot_corr_matrix(analysis_data.iloc[:,3:])
num_corr_matrix = analysis_data.corr()
print(num_corr_matrix)
print("畫好相關係數矩陣了!")