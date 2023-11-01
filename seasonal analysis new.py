#%%

import pandas as pd
import openpyxl

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

# %%

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

def wl_comparator():
    
    global wl_levels_table, wl_squads_table
    
    wl_levels = ["Average W/L"]
    wl_ratios = [avg_season_wl]
    lifetime_wl_ratios = [avg_lifetime_wl]
    
    wl_squads = ["Average W/l"]
    wl_ratios_squad = [avg_season_wl]
    lifetime_wl_ratios_squad = [avg_lifetime_wl]
    
    for level in levels:
        win_loss_level(level)
        wl_levels.append(level)
        wl_ratios.append(season_level_wl)
        lifetime_wl_ratios.append(lifetime_level_wl)
    
    for size in sizes:
        win_loss_squad(size)
        wl_squads.append(size)
        wl_ratios_squad.append(season_squad_wl)
        lifetime_wl_ratios_squad.append(lifetime_squad_wl)
        
    wl_levels_table = pd.DataFrame({"Map": wl_levels, "Season W/L": wl_ratios, "Lifetime W/L": lifetime_wl_ratios})
    wl_squads_table = pd.DataFrame({"Squad Size": wl_squads, "Season W/L": wl_ratios_squad, "Lifetime W/L": lifetime_wl_ratios_squad})
    
    return wl_levels_table, wl_squads_table

def kd_comparator():
    
    global kd_levels_table, kd_squads_table
    
    kd_levels = ["Average K/D"]
    kd_ratios = [avg_season_kd]
    kda_ratios = [avg_season_kda]
    lifetime_kd_ratios = [avg_lifetime_kd]
    lifetime_kda_ratios = [avg_lifetime_kda]
    
    kd_squads = ["Average K/D"]
    kd_ratios_squad = [avg_season_kd]
    kda_ratios_squad = [avg_season_kda]
    lifetime_kd_ratios_squad = [avg_lifetime_kd]
    lifetime_kda_ratios_squad = [avg_lifetime_kda]
    
    for level in levels:
        kill_death_level(level)
        kd_levels.append(level)
        kd_ratios.append(season_level_kd)
        kda_ratios.append(season_level_kda)
        lifetime_kd_ratios.append(lifetime_level_kd)
        lifetime_kda_ratios.append(lifetime_level_kda)
        
    for size in sizes:
        kill_death_squad(size)
        kd_squads.append(size)
        kd_ratios_squad.append(season_squad_kd)
        kda_ratios_squad.append(season_squad_kda)
        lifetime_kd_ratios_squad.append(lifetime_squad_kd)
        lifetime_kda_ratios_squad.append(lifetime_squad_kda)
        
    kd_levels_table = pd.DataFrame({"Map": kd_levels,
                                    "Season K/D": kd_ratios,
                                    "Season KA/D": kda_ratios,
                                    "Lifetime K/D": lifetime_kd_ratios,
                                    "Lifetime KA/D": lifetime_kda_ratios})
    kd_squads_table = pd.DataFrame({"Squad Size": kd_squads,
                                    "Season K/D": kd_ratios_squad,
                                    "Season KA/D": kda_ratios_squad,
                                    "Lifetime K/D": lifetime_kd_ratios_squad,
                                    "Lifetime KA/D": lifetime_kda_ratios_squad})
    
    return kd_levels_table, kd_squads_table

#%%

def get_scores_levels(level_name):
    
    global season_avg_score, lifetime_avg_score
    
    season_filtered = season_scores[season_scores["Map"] == level_name]
    lifetime_filtered = lifetime_scores[lifetime_scores["Map"] == level_name]
    season_count = len(season_filtered)
    lifetime_count = len(lifetime_filtered)
    
    season_total_score = season_filtered["Adjusted Score"].sum()
    lifetime_total_score = lifetime_filtered["Adjusted Score"].sum()
    
    if season_count == 0:
        season_avg_score = 0
    else:
        season_avg_score = season_total_score/season_count
    
    if lifetime_count == 0:
        lifetime_avg_score = 0
    else:
        lifetime_avg_score = lifetime_total_score/lifetime_count
    
    return level_name, season_avg_score, lifetime_avg_score

def get_scores_squads(squad_size):
    
    global season_avg_score, lifetime_avg_score
    
    season_scores_filtered = season_scores[season_scores["Squad Size"] == squad_size]
    lifetime_scores_filtered = lifetime_scores[lifetime_scores["Squad Size"] == squad_size]
    season_count = len(season_scores_filtered)
    lifetime_count = len(lifetime_scores_filtered)
    
    season_total_score = season_scores_filtered["Adjusted Score"].sum()
    lifetime_total_score = lifetime_scores_filtered["Adjusted Score"].sum()
    
    if season_count == 0:
        season_avg_score = 0
    else:
        season_avg_score = season_total_score/season_count
    
    if lifetime_count == 0:
        lifetime_avg_score = 0
    else:
        lifetime_avg_score = lifetime_total_score/season_count
    
    return squad_size, season_avg_score, lifetime_avg_score

#%%

def score_comparator():
    
    global score_levels_table, score_squads_table
    
    score_levels = ["Average Score"]
    season_level_scores = [avg_season_score]
    lifetime_level_scores = [avg_lifetime_score]
    
    score_squads = ["Average Score"]
    season_squad_scores = [avg_season_score]
    lifetime_squad_scores = [avg_lifetime_score]
    
    for level in levels:
        get_scores_levels(level)
        score_levels.append(level)
        season_level_scores.append(season_avg_score)
        lifetime_level_scores.append(lifetime_avg_score)
        
    for size in sizes:
        get_scores_squads(size)
        score_squads.append(size)
        season_squad_scores.append(season_avg_score)
        lifetime_squad_scores.append(lifetime_avg_score)
        
    score_levels_table = pd.DataFrame({"Map": score_levels,
                                       "Season Score": season_level_scores,
                                       "Lifetime Score": lifetime_level_scores})
    score_squads_table = pd.DataFrame({"Squad Size": score_squads,
                                       "Season Score": season_squad_scores,
                                       "Lifetime Score": lifetime_squad_scores})
    
    return score_levels_table, score_squads_table

#%%

josh_scores = season.dropna(subset = ["Josh Score"])
josh_scores.fillna(0)
josh_scores["Adjusted Score"] = josh_scores.loc[josh_scores["Outcome"] == "win", "Josh Score"] - 2000
josh_scores["Adjusted Score"] = josh_scores["Adjusted Score"].fillna(josh_scores.loc[josh_scores["Outcome"] == "loss", "Josh Score"])

josh_total = josh_scores["Adjusted Score"].sum()
josh_count_season = len(josh_scores)
josh_all_levels_avg = josh_total/josh_count_season

asa_scores = season.dropna(subset = ["Asa Score"])
asa_scores.fillna(0)
asa_scores["Adjusted Score"] = asa_scores.loc[asa_scores["Outcome"] == "win", "Asa Score"] - 2000
asa_scores["Adjusted Score"] = asa_scores["Adjusted Score"].fillna(asa_scores.loc[asa_scores["Outcome"] == "loss", "Asa Score"])

asa_total = asa_scores["Adjusted Score"].sum()
asa_count_season = len(asa_scores)
asa_all_levels_avg = asa_total/asa_count_season

ed_scores = season.dropna(subset = ["Ed Score"])
ed_scores.fillna(0)
ed_scores["Adjusted Score"] = ed_scores.loc[ed_scores["Outcome"] == "win", "Ed Score"] - 2000
ed_scores["Adjusted Score"] = ed_scores["Adjusted Score"].fillna(ed_scores.loc[ed_scores["Outcome"] == "loss", "Ed Score"])

ed_total = ed_scores["Adjusted Score"].sum()
ed_count_season = len(ed_scores)
ed_all_levels_avg = ed_total/ed_count_season

luke_scores = season.dropna(subset = ["Luke Score"])
luke_scores.fillna(0)
luke_scores["Adjusted Score"] = luke_scores.loc[luke_scores["Outcome"] == "win", "Luke Score"] - 2000
luke_scores["Adjusted Score"] = luke_scores["Adjusted Score"].fillna(luke_scores.loc[luke_scores["Outcome"] == "loss", "Luke Score"])

luke_total = luke_scores["Adjusted Score"].sum()
luke_count_season = len(luke_scores)
luke_all_levels_avg = luke_total/luke_count_season

#%%

def individual_performance_calculator(level_name):
    
    global josh_avg, asa_avg, ed_avg, luke_avg, josh_count, asa_count, ed_count, luke_count


    josh_filtered = josh_scores[josh_scores["Map"] == level_name]
    asa_filtered = asa_scores[asa_scores["Map"] == level_name]
    ed_filtered = ed_scores[ed_scores["Map"] == level_name]
    luke_filtered = luke_scores[luke_scores["Map"] == level_name]
    
    josh_count = len(josh_filtered)
    asa_count = len(asa_filtered)
    ed_count = len(ed_filtered)
    luke_count = len(luke_filtered)
    
    josh_total = josh_filtered["Adjusted Score"].sum()
    asa_total = asa_filtered["Adjusted Score"].sum()
    ed_total = ed_filtered["Adjusted Score"].sum()
    luke_total = luke_filtered["Adjusted Score"].sum()
    
    if josh_count == 0:
        josh_avg = 0
    else:
        josh_avg = josh_total/josh_count

    if asa_count == 0:
        asa_avg = 0
    else:
        asa_avg = asa_total/asa_count
        
    if ed_count == 0:
        ed_avg = 0
    else:
        ed_avg = ed_total/ed_count
        
    if luke_count == 0:
        luke_avg = 0
    else:
        luke_avg = luke_total/luke_count
    
    return level_name, josh_avg, asa_avg, ed_avg, luke_avg, josh_count, asa_count, ed_count, luke_count

#%%

def individual_perforamnce_constructor():
    
    global ip_table
    
    ip_score_levels = ["Average Score"]
    ip_josh_scores = [josh_all_levels_avg]
    ip_josh_games = [josh_count_season]
    ip_asa_scores = [asa_all_levels_avg]
    ip_asa_games = [asa_count_season]
    ip_ed_scores = [ed_all_levels_avg]
    ip_ed_games = [ed_count_season]
    ip_luke_scores = [luke_all_levels_avg]
    ip_luke_games = [luke_count_season]
    
    for level in levels:
        individual_performance_calculator(level)
        ip_score_levels.append(level)
        ip_josh_scores.append(josh_avg)
        ip_josh_games.append(josh_count)
        ip_asa_scores.append(asa_avg)
        ip_asa_games.append(asa_count)
        ip_ed_scores.append(ed_avg)
        ip_ed_games.append(ed_count)
        ip_luke_scores.append(luke_avg)
        ip_luke_games.append(luke_count)
        
    ip_table = pd.DataFrame({"Map": ip_score_levels,
                             "Josh Score": ip_josh_scores,
                             "Josh Games": ip_josh_games,
                             "Asa Score": ip_asa_scores,
                             "Asa Games": ip_asa_games,
                             "Ed Score": ip_ed_scores,
                             "Ed Games": ip_ed_games,
                             "Luke Score": ip_luke_scores,
                             "Luke Games": ip_luke_games})
    
    return ip_table

#%%

wl_comparator()

#%%

kd_comparator()

#%%

score_comparator()

#%%

individual_perforamnce_constructor()

#%%

wl_levels_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\win_loss_maps.xlsx")
wl_squads_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\win_loss_squads.xlsx")
kd_levels_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\kill_death_maps.xlsx")
kd_squads_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\kill_death_squads.xlsx")
score_levels_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\score_maps.xlsx")
score_squads_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\score_squads.xlsx")
ip_table.to_excel("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\individual_performance.xlsx")

#%%
