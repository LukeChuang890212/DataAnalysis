import pandas as pd 
import datetime

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
    #for資料視覺化
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
def get_client_host(row):
    teams = row[4:12]
    play_teams = teams[teams.values == 1].index
    client_host = [play_teams[1].split('_')[1],play_teams[0].split('_')[1]]
    return client_host
def add_game_res(data):
    #紀錄各隊逐場勝負結果
    b = []
    l = []
    m = []
    g = []
    for i in range(data.shape[0]):
        client_host = get_client_host(data.iloc[i,:])
        row = data.iloc[i,:]
        client_host = get_client_host(row)
        # teams = row[4:12]
        # # print(type(teams))
        # play_teams = teams[teams.values == 1].index
        # client_host = [play_teams[1].split('_')[1],play_teams[0].split('_')[1]]
        scores = row[34:36].values #[client_score,host_score]
        # print(host)
        # print(client)
        print(scores)
        if scores[0] > scores[1]:#客勝
            res = [1,0]
        elif scores[0] < scores[1]:#客敗
            res = [0,1]
        else:
            res = [2,2]#和局
        for t,t_res in zip(client_host,res):
            if t == "中信兄弟":
                b.append(t_res)
            elif t == "統一7-ELEVEn獅":
                l.append(t_res)
            elif t == "LAMIGO桃猿":
                m.append(t_res)
            elif t == "富邦悍將":
                g.append(t_res) 
    for l in [b,l,m,g]:
        l = [0 if x == 2 else x for x in l]
        print(l,len(l))

    split_dates = [datetime.datetime.strptime("2018-03-24", "%Y-%m-%d"),datetime.datetime.strptime("2019-03-23", "%Y-%m-%d")]
    split_indices = data[(data.DATE == split_dates[0]) | (data.DATE == split_dates[1])].index.tolist()
    print(split_indices)

    client_wins = []
    host_wins = [] 

    open_game_index = [0]
    open_game_index.extend(split_indices)
    print(open_game_index)
    for i in range(data.shape[0]):
        if i in open_game_index:
            for l in [client_wins,host_wins]:
                l.append(0.5)
                continue
            print(i,client_wins,host_wins)
        else:
            row = data.iloc[i,:]
            client_host = get_client_host(row)

            def mean(l):
                print('l',l)
                try:
                    mu = sum(l)/len(l)
                except:
                    mu = 0.5
                return mu
            for t,wins in zip(client_host,[client_wins,host_wins]):
                game_num = data[["CLIENT_"+t,"HOST_"+t]].iloc[int(i//240*240):i].values.sum()
                print("game_num",game_num)
                if t == "中信兄弟":
                    print("id",i,int(i//240*240))
                    wins.append(mean(b[int(i//240*120):int(i//240*120+game_num)]))
                elif t == "統一7-ELEVEn獅":
                    print("id",i,int(i//240*240))
                    wins.append(mean(l[int(i//240*120):int(i//240*120+game_num)]))
                elif t == "LAMIGO桃猿":
                    print("id",i,int(i//240*240))
                    wins.append(mean(m[int(i//240*120):int(i//240*120+game_num)]))
                elif t == "富邦悍將":
                    print("id",i,int(i//240*240))
                    wins.append(mean(g[int(i//240*120):int(i//240*120+game_num)]))
        # input("continue") 
    for l in [client_wins,host_wins]:
        print(l,len(l))

    wins_df = pd.DataFrame({"client_wins":client_wins,"host_wins":host_wins})
    data = pd.concat([data,wins_df],axis=1)
    data.to_excel("temp.xlsx")
    print(data)
    return data

# data = pd.read_excel("")
# for i,col in enumerate(analysis_data.columns):
#     print(i,col)
   