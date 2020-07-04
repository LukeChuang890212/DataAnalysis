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

#anova for box_office~host_team*day
value_vars = list(analysis_data.columns[3:7])
value_vars.extend(list(analysis_data.columns[20:26]))
# print(value_vars)

aov_data = pd.melt(analysis_data, id_vars=["DATE"],value_vars=value_vars)
# print(aov_data)
host_team_data = aov_data[aov_data.value == 1].reset_index().iloc[0:719,1:3].rename(columns={"variable":"HostTeam"})
# print(host_team_data)

day_data = aov_data[aov_data.value == 1].reset_index().iloc[719:,2].to_frame().rename(columns={"variable":"Day"}).reset_index()
day_data.drop("index",axis=1,inplace=True)
# print(day_data)

aov_data = pd.concat([host_team_data.join(day_data),analysis_data["BOX_OFFICE"]],axis=1)
# print(aov_data)

stat.anova(aov_data,"BOX_OFFICE~C(HostTeam)*C(Day)")

    


