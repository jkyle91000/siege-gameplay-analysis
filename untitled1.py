import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\kd by session.csv")
kd_data = pd.read_csv("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\siege stats - just kd.csv")

''' kd by session '''
#%%

sessions = []
ratios = []

#%%

def kill_death(session_num):
    
    kills = data.loc[data["session"] == session_num, "kills"].sum()
    deaths = data.loc[data["session"] == session_num, "deaths"].sum()
    
    if deaths == 0:
        kd_ratio = kills
    else:
        kd_ratio = round(kills/deaths, 2)
        
    sessions.append(session_num)
    ratios.append(kd_ratio)

#%%

for i in range(1, max(data["session"]+1)):
    kill_death(i)
    
#%%

df = pd.DataFrame(data = ratios)

#%%

df.to_csv("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\kd ratios.csv")

#%%

plt.figure(figsize = (8, 8),
           dpi = 1000)
sns.regplot(x = sessions,
            y = ratios,
            ci = None,
            scatter_kws = {"color": "gray"},
            line_kws = {"color": "cyan"})

#%%

''' kd data from all games '''

kd_data_new = kd_data.fillna(0)

kills = kd_data_new["Kills"]
deaths = kd_data_new["Deaths"]
assists = kd_data_new["Assists"]
games = kd_data_new["Game"]

ratios_all = []

#%%

for i in range(len(kd_data_new)):
    if kd_data_new["Deaths"][i] == 0:
        ratio = kd_data_new["Kills"][i]
    else:
        ratio = kd_data_new["Kills"][i]/kd_data_new["Deaths"][i]
    ratios_all.append(ratio)
        
#%%

plt.figure(figsize = (8, 8),
           dpi = 1000)
sns.regplot(x = games,
            y = ratios_all,
            ci = None,
            scatter_kws = {"color": "gray"},
            line_kws = {"color": "cyan"})

#%%

''' actual mathematical regression '''

