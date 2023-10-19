import pandas as pd

#%%

def prepare_season_data(title):
    
    global season, season_dropped, season_filled, season_scores
    
    season = pd.read_csv(f"C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\siege stats - {title}.csv")
    season = season.drop(["Game #", "Quick Notes"], axis = 1)
    season = season.drop(91) # remove for final review

    # standardizing "Outcome" observations
    outcomes = list(season["Outcome"])
    outcomes_new = []
    for i in range(len(outcomes)):
        outcomes_new.append(outcomes[i].lower())
    season["Outcome"] = outcomes_new
    
    # dropping ALL nan values
    season_dropped = season.dropna()
    
    # filling all nan values with 0
    season_filled = season.fillna(0)
    
    # preparing data for mean score and standardizing scores for wins and losses
    # this section might be its own function starting y8s4
    season_scores = season.dropna(subset = ["Josh Score"])
    season_scores.fillna(0)
    season_scores["Adjusted Score"] = season_scores.loc[season_scores["Outcome"] == "win", "Josh Score"] - 2000
    season_scores["Adjusted Score"] = season_scores["Adjusted Score"].fillna(season_scores.loc[season_scores["Outcome"] == "loss", "Josh Score"])
    
    return season, season_dropped, season_filled, season_scores

def prepare_lifetime_data():
    
    global lifetime, lifetime_dropped, lifetime_filled, lifetime_scores
    
    lifetime = pd.read_csv(f"C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\siege stats - everything.csv")
    lifetime = lifetime.drop("Game #", axis = 1)

    # standardizing "Outcome" observations
    outcomes = list(lifetime["Outcome"])
    outcomes_new = []
    for i in range(len(outcomes)):
        outcomes_new.append(outcomes[i].lower())
    lifetime["Outcome"] = outcomes_new
    
    # dropping ALL nan values
    lifetime_dropped = lifetime.dropna()
    
    # filling all nan values with 0
    lifetime_filled = lifetime.fillna(0)
    
    # preparing data for mean score and standardizing scores for wins and losses
    lifetime_scores = lifetime.dropna(subset = ["Score"])
    lifetime_scores.fillna(0)
    lifetime_scores["Adjusted Score"] = lifetime_scores.loc[lifetime_scores["Outcome"] == "win", "Score"] - 2000
    lifetime_scores["Adjusted Score"] = lifetime_scores["Adjusted Score"].fillna(lifetime_scores.loc[lifetime_scores["Outcome"] == "loss", "Score"])
    
    return lifetime, lifetime_dropped, lifetime_filled, lifetime_scores

#%%

prepare_season_data("Y8S3 - Heavy Mettle") #update for current season
prepare_lifetime_data()

#%%

# future proof lists :)
levels = list(season["Map"].unique())
levels = sorted(levels)

sizes = list(season["Squad Size"].unique())
sizes = sorted(sizes)

#%%

season_kills = season["Kills"].sum()
season_assists = season["Assists"].sum() * (1/3)
season_deaths = season["Deaths"].sum()
season_wins = len(season[(season["Outcome"] == "win")])
season_losses = len(season[(season["Outcome"] == "loss")])

lifetime_kills = lifetime["Kills"].sum()
lifetime_assists = lifetime["Assists"].sum() * 1/3
lifetime_deaths = lifetime["Deaths"].sum()
lifetime_wins = len(lifetime[(lifetime["Outcome"] == "win")])
lifetime_losses = len(lifetime[(lifetime["Outcome"] == "loss")])

avg_season_kd = season_kills/season_deaths
avg_season_kda = (season_kills + season_assists)/season_deaths
avg_season_wl = season_wins/season_losses
avg_season_score = season_score = season_scores["Adjusted Score"].sum()/len(season_scores)

avg_lifetime_kd = lifetime_kills/lifetime_deaths
avg_lifetime_kda = (lifetime_kills + lifetime_assists)/lifetime_deaths
avg_lifetime_wl = lifetime_wins/lifetime_losses
avg_lifetime_score = lifetime_scores["Adjusted Score"].sum()/len(lifetime_scores)

#%%

def win_loss_level(level_name):
    
    global season_level_wl, lifetime_level_wl
    
    season_filtered = season[season["Map"] == level_name]
    lifetime_filtered = lifetime[lifetime["Map"] == level_name]
    
    season_wins = len(season_filtered[(season_filtered["Outcome"] == "win")])
    season_losses = len(season_filtered[(season_filtered["Outcome"] == "loss")])
    lifetime_wins = len(lifetime_filtered[(lifetime_filtered["Outcome"] == "win")])
    lifetime_losses = len(lifetime_filtered[(lifetime_filtered["Outcome"] == "loss")])
    
    if season_losses == 0:
        season_level_wl = season_wins
    else:
        season_level_wl = season_wins/season_losses
    
    if lifetime_losses == 0:
        lifetime_level_wl = lifetime_wins
    else:
        lifetime_level_wl = lifetime_wins/lifetime_losses
    
    return season_level_wl, lifetime_level_wl

def win_loss_squad(squad_size):
    
    global season_squad_wl, lifetime_squad_wl
    
    season_filtered = season[season["Squad Size"] == squad_size]
    lifetime_filtered = lifetime_dropped[lifetime_dropped["Squad Size"] == squad_size]
    
    season_wins = len(season_filtered[(season_filtered["Outcome"] == "win")])
    season_losses = len(season_filtered[(season_filtered["Outcome"] == "loss")])
    lifetime_wins = len(lifetime_filtered[(lifetime_filtered["Outcome"] == "win")])
    lifetime_losses = len(lifetime_filtered[(lifetime_filtered["Outcome"] == "loss")])
    
    if season_losses == 0:
        season_squad_wl = season_wins
    else:
        season_squad_wl = season_wins/season_losses
    
    if lifetime_losses == 0:
        lifetime_squad_wl = lifetime_wins
    else:
        lifetime_squad_wl = lifetime_wins/lifetime_losses
        
    return season_squad_wl, lifetime_squad_wl

#%%

def win_loss_comparator():
    
    global season_wl_level_table, season_wl_squad_table, lifetime_wl_level_table, lifetime_wl_squad_table
    
    season_levels = ["Average Season W/L"]
    season_level_wl_ratios = [avg_season_wl]
    lifetime_levels = ["Lifetime W/L"]
    lifetime_level_wl_ratios = [avg_lifetime_wl]
    
    season_squads = ["Average Season W/L"]
    season_squad_wl_ratios = [avg_season_wl]
    lifetime_squads = ["Lifetime W/L"]
    lifetime_squad_wl_ratios = [avg_lifetime_wl]
    
    for level in levels:
        win_loss_level(level)
        season_levels.append(level)
        season_level_wl_ratios.append(season_level_wl)
        lifetime_levels.append(level)
        lifetime_level_wl_ratios.append(lifetime_level_wl)
        
    for size in sizes:
        win_loss_squad(size)
        season_squads.append(size)
        season_squad_wl_ratios.append(season_squad_wl)
        lifetime_squads.append(size)
        lifetime_squad_wl_ratios.append(lifetime_squad_wl)
    
    season_wl_level_table = pd.DataFrame({"Map": season_levels, "Season W/L": season_level_wl_ratios, })
    season_wl_squad_table = pd.DataFrame({"Squad Size": season_squads, "W/L": season_squad_wl_ratios})
    lifetime_wl_level_table = pd.DataFrame({"Map": lifetime_levels, "W/L": lifetime_level_wl_ratios})
    lifetime_wl_squad_table = pd.DataFrame({"Squad Size": lifetime_squads, "W/L": lifetime_squad_wl_ratios})
    
    return season_wl_level_table, season_wl_squad_table, lifetime_wl_level_table, lifetime_wl_squad_table

#%%

def kill_death_level(level_name):
    
    global season_level_kd, season_level_kda, lifetime_level_kd, lifetime_level_kda
    
    season_filtered = season[season["Map"] == level_name]
    lifetime_filtered = lifetime[lifetime["Map"] == level_name]
    
    season_kills = season_filtered["Kills"].sum()
    season_assists = season_filtered["Assists"].sum() * (1/3)
    season_deaths = season_filtered["Deaths"].sum()
    
    lifetime_kills = lifetime_filtered["Kills"].sum()
    lifetime_assists = lifetime_filtered["Assists"].sum() * (1/3)
    lifetime_deaths = lifetime_filtered["Deaths"].sum()
    
    if season_deaths == 0:
        season_level_kd = season_kills
        season_level_kda = season_kills + season_assists
    else:
        season_level_kd = season_kills/season_deaths
        season_level_kda = (season_kills + season_assists)/season_deaths
        
    if lifetime_deaths == 0:
        lifetime_level_kd = lifetime_kills
        lifetime_level_kda = lifetime_kills + lifetime_assists
    else:
        lifetime_level_kd = lifetime_kills/lifetime_deaths
        lifetime_level_kda = (lifetime_kills + lifetime_assists)/lifetime_deaths
        
    return season_level_kd, season_level_kda, lifetime_level_kd, lifetime_level_kda
    
def kill_death_squad(squad_size):
    
    global season_squad_kd, season_squad_kda, lifetime_squad_kd, lifetime_squad_kda
    
    season_filtered = season[season["Squad Size"] == squad_size]
    lifetime_filtered = lifetime[lifetime["Squad Size"] == squad_size]
    
    season_kills = season_filtered["Kills"].sum()
    season_assists = season_filtered["Assists"].sum() * (1/3)
    season_deaths = season_filtered["Deaths"].sum()
    
    lifetime_kills = lifetime_filtered["Kills"].sum()
    lifetime_assists = lifetime_filtered["Assists"].sum() * (1/3)
    lifetime_deaths = lifetime_filtered["Deaths"].sum()
    
    if season_deaths == 0:
        season_squad_kd = season_kills
        season_squad_kda = season_kills + season_assists
    else:
        season_squad_kd = season_kills/season_deaths
        season_squad_kda = (season_kills + season_assists)/season_deaths
        
    if lifetime_deaths == 0:
        lifetime_squad_kd = lifetime_kills
        lifetime_squad_kda = lifetime_kills + lifetime_assists
    else:
        lifetime_squad_kd = lifetime_kills/lifetime_deaths
        lifetime_squad_kda = (lifetime_kills + lifetime_assists)/lifetime_deaths

    return season_squad_kd, season_squad_kda, lifetime_squad_kd, lifetime_squad_kda

#%%
def kill_death_comparator():
    
    global season_kd_level_table, season_kd_squad_table, lifetime_kd_level_table, lifetime_kd_squad_table
    
    season_levels = ["Average Season K/D"]
    season_level_kd_ratios = [avg_season_kd]
    season_level_kda_ratios = [avg_season_kda]
    lifetime_levels = ["Lifetime K/D"]
    lifetime_level_kd_ratios = [avg_lifetime_kd]
    lifetime_level_kda_ratios = [avg_lifetime_kda]
    
    season_squads = ["Average Season K/D"]
    season_squad_kd_ratios = [avg_season_kd]
    season_squad_kda_ratios = [avg_season_kda]
    lifetime_squads = ["Lifetime K/D"]
    lifetime_squad_kd_ratios = [avg_lifetime_kd]
    lifetime_squad_kda_ratios = [avg_lifetime_kda]
    
    for level in levels:
        kill_death_level(level)
        season_levels.append(level)
        season_level_kd_ratios.append(season_level_kd)
        season_level_kda_ratios.append(season_level_kda)
        lifetime_levels.append(level)
        lifetime_level_kd_ratios.append(lifetime_level_kd)
        lifetime_level_kda_ratios.append(lifetime_level_kda)
        
    for size in sizes:
        kill_death_squad(size)
        season_squads.append(size)
        season_squad_kd_ratios.append(season_squad_kd)
        season_squad_kda_ratios.append(season_squad_kda)
        lifetime_squads.append(size)
        lifetime_squad_kd_ratios.append(lifetime_squad_kd)
        lifetime_squad_kda_ratios.append(lifetime_squad_kda)
    
    season_kd_level_table = pd.DataFrame({"Map": season_levels, "K/D": season_level_kd_ratios, "KA/D": season_level_kda_ratios})
    season_kd_squad_table = pd.DataFrame({"Squad Size": season_squads, "K/D": season_squad_kd_ratios, "KA/D": season_squad_kda_ratios})
    lifetime_kd_level_table = pd.DataFrame({"Map": lifetime_levels, "K/D": lifetime_level_kd_ratios, "KA/D": lifetime_level_kda_ratios})
    lifetime_kd_squad_table = pd.DataFrame({"Squad Size": lifetime_squads, "K/D": lifetime_squad_kd_ratios, "KA/D": lifetime_squad_kda_ratios})
    
    return season_kd_level_table, season_kd_squad_table, lifetime_kd_level_table, lifetime_kd_squad_table

#%%

win_loss_comparator()
kill_death_comparator()

#%%


