import pandas as pd 

#寫成get_source()
#(練習寫polymorphism)
def get_source(y,x,category_s,category_e,category,analysis_data):
    source = pd.concat([analysis_data.iloc[:,y],analysis_data.iloc[:,x],analysis_data.iloc[:,category_s:category_e+1]],axis=1)
    source.insert(0,"index",range(0,source.shape[0]))
    source = source.reset_index().melt(list(source.columns[0:len(source.columns)-(category_e-category_s+1)]), var_name=category, value_name='y')
    source = source[source['y']  == 1].reset_index()
    source.drop(["level_0","index",'y'],axis = 1,inplace=True)  
    source.drop(0,inplace=True)
    print(source.head())
    # source = source[[source.columns[1],source.columns[2],source.columns[0]]].sort_values(source.columns[1]).reset_index()
    source = source.sort_values(source.columns[1]).reset_index()    
    source.drop(["index"],axis = 1,inplace=True)
    print(source)
    return source
# def get_source(y,x_s,x_e,category_s,category_e,category,analysis_data):
#     source = pd.concat([analysis_data.iloc[:,y],analysis_data.iloc[:,x_s:x_e+1],analysis_data.iloc[:,category_s:category_e+1]],axis=1)
#     source.insert(0,"index",range(0,source.shape[0]))
 
#     source = source.reset_index().melt(list(source.columns[0:2+(x_e-x_s+1)]), var_name=category, value_name='y')
#     source = source[source['y']  == 1].reset_index()
#     source.drop(["level_0","index",'y'],axis = 1,inplace=True)  
#     source.drop(0,inplace=True)
#     print(source.head())
#     input("continue")

#     source = source[["BOX_OFFICE","Tue","Wed","Thu","Fri","Sat","Sun",category]]
#     print(source.head())
#     source = source.reset_index().melt(list(source.columns[0:8:7]), var_name="DAY", value_name='y')
#     source = source[source['y']  == 1].reset_index()
#     source.drop(["index",'y'],axis = 1,inplace=True)  
#     source.drop(0,inplace=True)
#     print(source.head())
#     input("continue")

#     # source = source[[source.columns[1],source.columns[2],source.columns[0]]].sort_values(source.columns[1]).reset_index()
#     # source.drop(["index"],axis = 1,inplace=True)
#     # print(source)
#     return source
def add_game_res(data):
    b = []
    l = []
    m = []
    g = []
    for i in range(data.shape[0]):
        row = data.iloc[i,:]
        teams = row[4:12]
        # print(type(teams))
        play_teams = teams[teams.values == 1].index
        client_host = [play_teams[1].split('_')[1],play_teams[0].split('_')[1]]
        scores = row[34:36].values #[client_score,host_score]
        # print(host)
        # print(client)
        print(scores)
        if scores[0] > scores[1]:
            res = [1,0]
        elif scores[0] < scores[1]:
            res = [0,1]
        else:
            res = [2,2]
        for t,t_res in zip(client_host,res):
            if t == "中信兄弟":
                b.append(t_res)
            elif t == "統一7-ELEVEn獅":
                l.append(t_res)
            elif t == "LAMIGO桃猿":
                m.append(t_res)
            elif t == "富邦悍將":
                g.append(t_res) 

        # input("continue")
        # teams =
    for i in [b,l,m,g]:
        print(i,len(i))
    input("continue") 
    return data
   