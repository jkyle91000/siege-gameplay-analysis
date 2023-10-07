import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%

# preparing multiple forms of the data
data = pd.read_csv("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\siege stats - everything.csv")

outcomes = list(data["Outcome"])

outcomes_new = []

for i in range(len(outcomes)):
    outcomes_new.append(outcomes[i].lower())

data["Outcomes"] = outcomes_new

data_dropped = data.dropna()

data_filled = data.fillna(0)

#%%

def kill_death(map_name):

    global kd, kda

    kills = data_filled.loc[data_filled["Map"] == map_name, "Kills"].sum()
    deaths = data_filled.loc[data_filled["Map"] == map_name, "Deaths"].sum()
    assists = 1/3 * data_filled.loc[data_filled["Map"] == map_name, "Assists"].sum()
    
    if deaths == 0:
        kd = kills
        kda = kills + assists
    else:
        kd = kills/deaths
        kda = (kills + assists)/deaths
        
    return kd, kda

#%%

maps = ["Bank",
        "Border",
        "Chalet",
        "Club House",
        "Coastline",
        "Consulate",
        "Emerald Plains",
        "Kafe Dostoyevsky",
        "Kanal",
        "Nighthaven Labs",
        "Oregon",
        "Outback",
        "Skyscraper",
        "Stadium Bravo",
        "Theme Park",
        "Villa"]

sizes = [1, 2, 3, 4, 5]


#%%

kd_ratios = []
kd_assists = []

for i in maps:
    kill_death(i)
    kd_ratios.append(kd)
    kd_assists.append(kda)

#%%

maps_table = pd.DataFrame(data = maps)
maps_table["K/D"] = kd_ratios
maps_table["K/DA"] = kd_assists

maps_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\Ranked 2 KD by Maps.xlsx")

#%%

def kill_death_squad(size):

    global kd, kda

    kills = data_filled.loc[data_filled["Squad Size"] == size, "Kills"].sum()
    deaths = data_filled.loc[data_filled["Squad Size"] == size, "Deaths"].sum()
    assists = 1/3 * data_filled.loc[data_filled["Squad Size"] == size, "Assists"].sum()
    
    if deaths == 0:
        kd = kills
        kda = kills + assists
    else:
        kd = kills/deaths
        kda = (kills + assists)/deaths
        
    return kd, kda

#%%

kd_ratios_squad = []
kd_assists_squad = []

for i in sizes:
    kill_death_squad(i)
    kd_ratios_squad.append(kd)
    kd_assists_squad.append(kda)
    
#%%

squads_table = pd.DataFrame(data = sizes)
squads_table["K/D"] = kd_ratios_squad
squads_table["K/DA"] = kd_assists_squad
squads_table.to_excel("C:\\Users\\aethe\OneDrive\\Desktop\\stats\\Ranked 2 KD by Squad.xlsx")

#%%

for i in data_filled:
   break 