import StatTesting as stat
import pandas as pd 
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) 

analysis_data = pd.read_excel("時間序列分析資料.xlsx")
analysis_data.drop("Unnamed: 0",axis=1,inplace=True)
for col,i in enumerate(analysis_data.columns):
    print(col,i)

print(analysis_data)

teams = []
mean1s = []
mean2s = []
mod_std1s = []
mod_std2s = []
t_scores = []
ps = []
for team in analysis_data.columns[3:7]:
    team_data = analysis_data[analysis_data[team] == 1]
    print(team_data)

    week_day = team_data[(team_data.Sat == 0) & (team_data.Sun == 0)].BOX_OFFICE
    weekend = team_data[(team_data.Sat == 1) | (team_data.Sun == 1)].BOX_OFFICE
    
    mean1, mean2, mod_std1, mod_std2, t_score, p = stat.t_test(week_day,weekend)

    teams.append(team)
    mean1s.append(mean1)
    mean2s.append(mean2)
    mod_std1s.append(mod_std1)
    mod_std2s.append(mod_std2)
    t_scores.append(t_score)
    ps.append(p)

res = {"Team":teams,"Week Day Mean":mean1s,"Weekend Mean":mean2s,"Week Day SE":mod_std1s,"Weekend SE":mod_std2s,"T Score":t_scores,"P Value":ps}
res_table = pd.DataFrame(res).round(4)
print(res_table)


    


