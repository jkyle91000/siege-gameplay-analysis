import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%

data = pd.read_csv("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\siege stats - everything.csv")

#%%

# standardizing "Outcome" observations
outcomes = list(data["Outcome"])
outcomes_new = []
for i in range(len(outcomes)):
    outcomes_new.append(outcomes[i].lower())
data["Outcome"] = outcomes_new

#%%

# dropping ALL nan values
data_dropped = data.dropna()

#%%

# filling all nan values with 0

data_filled = data.fillna(0)

#%%

# preparing data for mean score and standardizing scores for wins and losses
data_scores = data.dropna(subset = ["Score"])
data_scores.fillna(0)
data_scores["Adjusted Score"] = data_scores.loc[data_scores["Outcome"] == "win", "Score"] - 2000
data_scores["Adjusted Score"] = data_scores["Adjusted Score"].fillna(data_scores.loc[data_scores["Outcome"] == "loss", "Score"])


#%%

# lists i need
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

squad_map_table = pd.DataFrame(columns = ["Map",
                                          "Squad Size",
                                          "K/D",
                                          "KA/D"])

#%%

def kill_death_map_squad(map_name, squad_size):
    
    global kd, kda
    
    data_filtered = data_filled[data_filled["Map"] == map_name]
        
    kills = data_filtered.loc[data_filtered["Squad Size"] == squad_size, "Kills"].sum()
    deaths = data_filtered.loc[data_filtered["Squad Size"] == squad_size, "Deaths"].sum()
    assists = data_filtered.loc[data_filtered["Squad Size"] == squad_size, "Assists"].sum() * 1/3
    
    if deaths == 0:
        kd = kills
        kda = kills + assists
    else:
        kd = kills/deaths
        kda = (kills + assists)/deaths

    return map_name, squad_size, kd, kda
    

#%%

maps_for_table = []
squad_sizes_for_table = []
kd_ratios_for_table = []
kd_assists_for_table = []

for i in maps:
    for j in sizes:
        kill_death_map_squad(i, j)
        maps_for_table.append(i)
        squad_sizes_for_table.append(j)
        kd_ratios_for_table.append(kd)
        kd_assists_for_table.append(kda)


#%%

squad_map_table["Map"] = maps_for_table
squad_map_table["Squad Size"] = squad_sizes_for_table
squad_map_table["K/D"] = kd_ratios_for_table
squad_map_table["KA/D"] = kd_assists_for_table

squad_map_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\kd by map and squad size.xlsx")

#%%

def win_loss_map_squad(map_name, squad_size):
    
    global wl
    
    data_filtered = data_filled[data_filled["Map"] == map_name]
    
    wins = len(data_filtered[(data_filtered["Squad Size"] == squad_size) & (data_filtered["Outcome"] == "win")])
    losses = len(data_filtered[(data_filtered["Squad Size"] == squad_size) & (data_filtered["Outcome"] == "loss")])
    
    if losses == 0:
        wl = wins
    else:
        wl = wins/losses
        
    return wl
        
#%%

levels = []
squad_sizes = []
ratios = []

for i in maps:
    for j in sizes:
        win_loss_map_squad(i, j)
        levels.append(i)
        squad_sizes.append(j)
        ratios.append(wl)

#%%

win_loss_table = pd.DataFrame(columns = ["Map", "Squad Size", "W/L"])

win_loss_table["Map"] = levels
win_loss_table["Squad Size"] = squad_sizes
win_loss_table["W/L"] = ratios

win_loss_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\win_loss_table.xlsx")

#%%

def score_stuff(map_name, squad_size):
    
    global average_score

    data_filtered = data_scores[data_scores["Map"] == map_name]
    data_filtered = data_filtered[data_filtered["Squad Size"] == squad_size]
    
    score = data_filtered.loc[data_filtered["Squad Size"] == squad_size, "Adjusted Score"].sum()
    count = len(data_filtered)
    
    if count == 0:
        average_score = 0
    else:
        average_score = score/count
    
    return average_score

#%%

levels = []
squads = []
scores = []

for i in maps:
    for j in sizes:
        score_stuff(i, j)
        levels.append(i)
        squads.append(j)
        scores.append(average_score)
        
#%%
scores_table = pd.DataFrame(columns = ["Map",
                                       "Squad Size",
                                       "Average Score"])
scores_table["Map"] = levels
scores_table["Squad Size"] = squads
scores_table["Average Score"] = scores

scores_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\scores table.xlsx")

#%%

def atk_def_breakdown(map_name, squad_size):
    
    global atk_ratio, def_ratio
    
    data_filtered = data_filled[data_filled["Map"] == map_name]
    data_filtered = data_filtered[data_filtered["Squad Size"] == squad_size]
    
    atk_wins = data_filtered["ATK Wins"].sum()
    atk_losses = data_filtered["ATK Losses"].sum()
    def_wins = data_filtered["DEF Wins"].sum()
    def_losses = data_filtered["DEF Losses"].sum()
    
    if atk_losses == 0:
        atk_ratio = atk_wins
    else:
        atk_ratio = atk_wins/atk_losses
        
    if def_losses == 0:
        def_ratio = def_wins
    else:
        def_ratio = def_wins/def_losses
    
    return atk_ratio, def_ratio


#%%

atk_def_table = pd.DataFrame(columns = ["Map",
                                        "Squad Size",
                                        "ATK Win/Loss",
                                        "DEF Win/Loss"])

#%%

levels = []
squads = []
atk_ratios = []
def_ratios = []

for i in maps:
    for j in sizes:
        atk_def_breakdown(i, j)
        levels.append(i)
        squads.append(j)
        atk_ratios.append(atk_ratio)
        def_ratios.append(def_ratio)
    
#%%

atk_def_table["Map"] = levels
atk_def_table["Squad Size"] = squads
atk_def_table["ATK Win/Loss"] = atk_ratios
atk_def_table["DEF Win/Loss"] = def_ratios

atk_def_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\atk_def_table.xlsx")

#%%

#%%

def all_the_damn_data(level_name, squad_size):

    win_loss_map_squad(level_name, squad_size)
    kill_death_map_squad(level_name, squad_size)
    score_stuff(level_name, squad_size)
    atk_def_breakdown(level_name, squad_size)
    
#%%

levels = []
squads = []
kd_ratios = []
kda_ratios = []
scores = []
wl_ratios = []
atk_ratios = []
def_ratios = []

for i in maps:
    for j in sizes:
        all_the_damn_data(i, j)
        levels.append(i)
        squads.append(j)
        kd_ratios.append(kd)
        kda_ratios.append(kda)
        scores.append(average_score)
        wl_ratios.append(wl)
        atk_ratios.append(atk_ratio)
        def_ratios.append(def_ratio)
        
#%%

big_fucking_table = pd.DataFrame(columns = ["Map",
                                            "Squad Size",
                                            "K/D",
                                            "KA/D",
                                            "Average Score",
                                            "ATK Win/Loss",
                                            "DEF Win/Loss",
                                            "W/L"])
big_fucking_table["Map"] = levels
big_fucking_table["Squad Size"] = squads
big_fucking_table["K/D"] = kd_ratios
big_fucking_table["KA/D"] = kda_ratios
big_fucking_table["Average Score"] = scores
big_fucking_table["ATK Win/Loss"] = atk_ratios
big_fucking_table["DEF Win/Loss"] = def_ratios
big_fucking_table["W/L"] = wl_ratios

big_fucking_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\big_fucking_table.xlsx")