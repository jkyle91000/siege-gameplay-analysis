import pandas as pd

data=pd.read_csv('/home/josh/Desktop/Personal Projects/siege stats - Y8S2 - Dread Factor.csv')
data = data.dropna()
     
#%%

def matches(mapName):
    
    games = len(data[(data["Map"]==mapName)])
    
    print(f"You have played {games} matches on {mapName}.")


def winLoss(mapName):

    wins = len(data[(data["Map"]==mapName) & (data["Outcome"]=="win")])
    losses = len(data[(data["Map"]==mapName) & (data["Outcome"]=="loss")])

    if (losses == 0 and wins != 0) or (losses != 0 and wins == 0):
        print(f"You have {wins} wins and {losses} losses on {mapName}.")
    elif losses == 0 and wins == 0:
        print(f"{mapName} does not exist or you have not played it.")
    else:
        WL = wins/losses
        print(f"You have {wins} wins and {losses} losses on {mapName}, a win/loss ratio of {WL}.")


def killDeath(mapName):
    
    kills = data.loc[data["Map"]==mapName, "Kills"].sum()
    deaths = data.loc[data["Map"]==mapName, "Deaths"].sum()
    
    if (deaths == 0 and kills != 0) or (deaths != 0 and kills == 0):
        print(f"You have {kills} kills and {deaths} deaths on {mapName}.")
    elif deaths == 0 and kills == 0:
        print(f"{mapName} does not exist or you have not played it.")
    else:
        KD = kills/deaths
        print(f"You have {kills} kills and {deaths} deaths on {mapName}, a kill/death ratio of {KD}.")


def squadWL(size):
    
    squadWins = len(data[(data["Squad Size"]==size) & (data["Outcome"]=="win")])
    squadLosses = len(data[(data["Squad Size"]==size) & (data["Outcome"]=="loss")])

    if (squadLosses == 0 and squadWins != 0) or (squadLosses != 0 and squadWins == 0):
        print(f"{squadWins} wins, {squadLosses} losses")
    elif squadLosses == 0 and squadWins == 0:
        print(f"{size}-stack unplayed or nonexistent")
    else:
        squadWinLoss = squadWins/squadLosses
        print(f"{size}-stack w/l: {squadWinLoss}")


def squadKD(size):
    
    squadKills = data.loc[data["Squad Size"]==size, "Kills"].sum()
    squadDeaths = data.loc[data["Squad Size"]==size, "Deaths"].sum()
    
    if (squadDeaths == 0 and squadKills != 0) or (squadDeaths != 0 and squadKills == 0):
        print(f"{squadKills} kills, {squadDeaths} deaths")
    elif squadDeaths == 0 and squadKills == 0:
        print(f"{size}-stack unplayed or nonexistent")
    else:
        squadKillDeath = squadKills/squadDeaths
        print(f"{size}-stack k/d: {squadKillDeath}")
        

def attack(mapName):
    
    attackWins = data.loc[data["Map"]==mapName, "ATK Wins"].sum()
    attackLosses = data.loc[data["Map"]==mapName, "ATK Losses"].sum()
    
    attackRounds = attackWins + attackLosses
    print(f"You have played {attackRounds} rounds while attacking on {mapName}.")
    
    if (attackLosses == 0 and attackWins != 0) or (attackLosses != 0 and attackWins == 0):
        print(f"You have {attackWins} wins and {attackLosses} losses when attacking on {mapName}.")
    elif attackLosses == 0 and attackWins == 0:
        print(f"{mapName} does not exist or you have not played it.")
    else:
        attackWinRatio = attackWins/attackLosses
        print(f"You have {attackWins} wins and {attackLosses} losses when attacking on {mapName}. This is a win/loss ratio of {attackWinRatio}.")


def defense(mapName):
    
    defenseWins = data.loc[data["Map"]==mapName, "DEF Wins"].sum()
    defenseLosses = data.loc[data["Map"]==mapName, "DEF Losses"].sum()
    
    defenseRounds = defenseWins + defenseLosses
    print(f"You have played {defenseRounds} rounds while defending on {mapName}.")
    
    if (defenseLosses == 0 and defenseWins != 0) or (defenseLosses != 0 and defenseWins == 0):
        print(f"You have {defenseWins} wins and {defenseLosses} losses when attacking on {mapName}.")
    elif defenseLosses == 0 and defenseWins == 0:
        print(f"{mapName} does not exist or you have not played it.")
    else:
        defenseWinRatio = defenseWins/defenseLosses
        print(f"You have {defenseWins} wins and {defenseLosses} losses when attacking on {mapName}. This is a win/loss ratio of {defenseWinRatio}.")
        

def attackDefense(mapName):
    attack(mapName)
    defense(mapName)
    

def summary(mapName):
    matches(mapName)
    winLoss(mapName)
    killDeath(mapName)
    attackDefense(mapName)


def summarySquad(size):
    squadWL(size)
    squadKD(size)

#%%

maps = ["Bank",
        "Border",
        "Chalet",
        "Club House",
        "Coastline",
        "Counslate",
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

squadSizes = [1, 2, 3, 4, 5]

#%%

for mapName in maps:
    matches(mapName)
    
#%%

for mapName in maps:
    winLoss(mapName)

#%%

for mapName in maps:
    killDeath(mapName)

#%%
    
for mapName in maps:
    attack(mapName)

#%%

for mapName in maps:
    defense(mapName)

#%%

for size in squadSizes:
    summarySquad(size)
    

#%%

for mapName in maps:
    summary(mapName)