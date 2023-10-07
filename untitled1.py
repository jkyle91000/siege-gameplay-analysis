import pandas as pd
import seaborn as sns


data = pd.read_csv("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\kd by session.csv")

#%%

print(data)
print(type(data))

#%%

def proof_of_concept(session_num):
    kills = data.loc[data["session"] == session_num , "kills"].sum()
    deaths = data.loc[data["session"] == session_num, "deaths"].sum()
    
    print(session_num, kills, deaths)
    
#%%

proof_of_concept(1)

#%%

for i in range(1,max(data["session"]+1)):
    proof_of_concept(i)
    
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

kill_death(1)

#%%

for i in range(1, max(data["session"]+1)):
    kill_death(i)
    
#%%

print(sessions)
print(ratios)

#%%

df = pd.DataFrame(data = ratios)

#%%

print(df)

#%%

df.to_csv("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\kd ratios.csv")

#%%

sns.regplot(x = sessions, y = ratios, ci = None)

sns.lmplot(x = sessions, y = ratios, ci = None, robust = True)

#%%

