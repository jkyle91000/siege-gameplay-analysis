import pandas as pd

data=pd.read_csv('/home/josh/Desktop/Personal Projects/siege stats - Y8S2 - Dread Factor.csv')
data=data.dropna()
        
#%%
   
def winLoss(mapName):

    wins = len(data[(data["Map"]==mapName) & (data["Outcome"]=="win")])
    losses = len(data[(data["Map"]==mapName) & (data["Outcome"]=="loss")])

    if losses == 0 and wins != 0:
        return wins
    elif wins == 0:
        losses = losses * -1
        return losses
    else:
        WL = wins/losses
        return WL
    
#%%

    
def killDeath(mapName):
    
    kills = data.loc[data["Map"]==mapName, "Kills"].sum()
    deaths = data.loc[data["Map"]==mapName, "Deaths"].sum()
    
    if deaths == 0 and kills != 0:
        return kills
    elif kills == 0:
        deaths = deaths * -1
        return deaths
    else:
        KD = kills/deaths
        return KD

#%%
        
def squadWL(size):
    
    squadWins = len(data[(data["Squad Size"]==size) & (data["Outcome"]=="win")])
    squadLosses = len(data[(data["Squad Size"]==size) & (data["Outcome"]=="loss")])

    if squadLosses == 0 and squadWins != 0:
        return squadWins
    elif squadWins == 0:
        squadLosses = squadLosses * -1
        return squadLosses
    else:
        squadWinLoss = squadWins/squadLosses
        return squadWinLoss
    
#%%

def squadKD(size):
    
    squadKills = data.loc[data["Squad Size"]==size, "Kills"].sum()
    squadDeaths = data.loc[data["Squad Size"]==size, "Deaths"].sum()
    
    if squadDeaths == 0 and squadKills != 0:
        return squadKills
    elif squadDeaths == 0 and squadKills == 0:
        squadDeaths = squadDeaths * -1
        return squadDeaths
    else:
        squadKillDeath = squadKills/squadDeaths
        return squadKillDeath

#%%

def attack(mapName):
    
    attackWins = data.loc[data["Map"]==mapName, "ATK Wins"].sum()
    attackLosses = data.loc[data["Map"]==mapName, "ATK Losses"].sum()
    
    if attackLosses == 0 and attackWins != 0:
        return attackWins
    elif attackWins == 0:
        attackLosses = attackLosses * -1
        return attackLosses
    else:
        attackWinRatio = attackWins/attackLosses
        return attackWinRatio

#%%

def defense(mapName):
    
    defenseWins = data.loc[data["Map"]==mapName, "DEF Wins"].sum()
    defenseLosses = data.loc[data["Map"]==mapName, "DEF Losses"].sum()
    
    if defenseLosses == 0 and defenseWins != 0:
        return defenseWins
    elif defenseWins == 0:
        defenseLosses = defenseLosses * -1
        return defenseLosses
    else:
        defenseWinRatio = defenseWins/defenseLosses
        return defenseWinRatio

#%%

def matches(mapName):
    
    games = len(data[(data["Map"]==mapName)])
    
    return games

#%%

def squadMatches(size):
    
    squadGames = len(data[(data["Squad Size"]==size)])
    
    return squadGames

#%%

def attackCount(mapName):
    
    attackWins = data.loc[data["Map"]==mapName, "ATK Wins"].sum()
    attackLosses = data.loc[data["Map"]==mapName, "ATK Losses"].sum()
    
    attackRounds = attackWins + attackLosses
    
    return attackRounds

#%%

def defenseCount(mapName):
    
    defenseWins = data.loc[data["Map"]==mapName, "DEF Wins"].sum()
    defenseLosses = data.loc[data["Map"]==mapName, "DEF Losses"].sum()
    
    defenseRounds = defenseWins + defenseLosses
    
    return defenseRounds

#%%

d={'Map':['Bank',
          'Border',
          'Chalet',
          'Club House',
          'Coastline',
          'Consulate',
          'Emerald Plains',
          'Kafe Dostoyevsky',
          'Kanal',
          'Nighthaven Labs',
          'Oregon',
          'Outback',
          'Skyscraper',
          'Stadium Bravo',
          'Theme Park',
          'Villa']}
df=pd.DataFrame(data=d)
df

#%%

d_KD=[round(killDeath('Bank'),2),
      round(killDeath('Border'),2),
      round(killDeath('Chalet'),2),
      round(killDeath('Club House'),2),
      round(killDeath('Coastline'),2),
      round(killDeath('Consulate'),2),
      round(killDeath('Emerald Plains'),2),
      round(killDeath('Kafe Dostoyevsky'),2),
      round(killDeath('Kanal'),2),
      round(killDeath('Nighthaven Labs'),2),
      round(killDeath('Oregon'),2),
      round(killDeath('Outback'),2),
      round(killDeath('Skyscraper'),2),
      round(killDeath('Stadium Bravo'),2),
      round(killDeath('Theme Park'),2),
      round(killDeath('Villa'),2)]

d_WL=[round(winLoss('Bank'),2),
      round(winLoss('Border'),2),
      round(winLoss('Chalet'),2),
      round(winLoss('Club House'),2),
      round(winLoss('Coastline'),2),
      round(winLoss('Consulate'),2),
      round(winLoss('Emerald Plains'),2),
      round(winLoss('Kafe Dostoyevsky'),2),
      round(winLoss('Kanal'),2),
      round(winLoss('Nighthaven Labs'),2),
      round(winLoss('Oregon'),2),
      round(winLoss('Outback'),2),
      round(winLoss('Skyscraper'),2),
      round(winLoss('Stadium Bravo'),2),
      round(winLoss('Theme Park'),2),
      round(winLoss('Villa'),2)]
    
d_ATK = [round(attack('Bank'),2),
         round(attack('Border'),2),
         round(attack('Chalet'),2),
         round(attack('Club House'),2),
         round(attack('Coastline'),2),
         round(attack('Consulate'),2),
         round(attack('Emerald Plains'),2),
         round(attack('Kafe Dostoyevsky'),2),
         round(attack('Kanal'),2),
         round(attack('Nighthaven Labs'),2),
         round(attack('Oregon'),2),
         round(attack('Outback'),2),
         round(attack('Skyscraper'),2),
         round(attack('Stadium Bravo'),2),
         round(attack('Theme Park'),2),
         round(attack('Villa'),2)]

d_DEF = [round(defense('Bank'),2),
         round(defense('Border'),2),
         round(defense('Chalet'),2),
         round(defense('Club House'),2),
         round(defense('Coastline'),2),
         round(defense('Consulate'),2),
         round(defense('Emerald Plains'),2),
         round(defense('Kafe Dostoyevsky'),2),
         round(defense('Kanal'),2),
         round(defense('Nighthaven Labs'),2),
         round(defense('Oregon'),2),
         round(defense('Outback'),2),
         round(defense('Skyscraper'),2),
         round(defense('Stadium Bravo'),2),
         round(defense('Theme Park'),2),
         round(defense('Villa'),2)]

d_matchCount = [matches("Bank"),
                matches("Border"),
                matches("Chalet"),
                matches("Club House"),
                matches("Coastline"),
                matches("Consulate"),
                matches("Emerald Plains"),
                matches("Kafe Dostoyevsky"),
                matches("Kanal"),
                matches("Nighthaven Labs"),
                matches("Oregon"),
                matches("Outback"),
                matches("Skyscraper"),
                matches("Stadium Bravo"),
                matches("Theme Park"),
                matches("Villa")]

d_roundCountATK = [attackCount("Bank"),
                   attackCount("Border"),
                   attackCount("Chalet"),
                   attackCount("Club House"),
                   attackCount("Coastline"),
                   attackCount("Consulate"),
                   attackCount("Emerald Plains"),
                   attackCount("Kafe Dostoyevsky"),
                   attackCount("Kanal"),
                   attackCount("Nighthaven Labs"),
                   attackCount("Oregon"),
                   attackCount("Outback"),
                   attackCount("Skyscraper"),
                   attackCount("Stadium Bravo"),
                   attackCount("Theme Park"),
                   attackCount("Villa")]

d_roundCountDEF = [defenseCount("Bank"),
                   defenseCount("Border"),
                   defenseCount("Chalet"),
                   defenseCount("Club House"),
                   defenseCount("Coastline"),
                   defenseCount("Consulate"),
                   defenseCount("Emerald Plains"),
                   defenseCount("Kafe Dostoyevsky"),
                   defenseCount("Kanal"),
                   defenseCount("Nighthaven Labs"),
                   defenseCount("Oregon"),
                   defenseCount("Outback"),
                   defenseCount("Skyscraper"),
                   defenseCount("Stadium Bravo"),
                   defenseCount("Theme Park"),
                   defenseCount("Villa")]

df["Matches"] = d_matchCount
df['Win/Loss']=d_WL
df['Kill/Death']=d_KD
df['Attack'] = d_ATK
df["Attack Rounds"] = d_roundCountATK
df['Defense'] = d_DEF
df["Defense Rounds"] = d_roundCountDEF

print(df)

df.to_excel('/home/josh/Desktop/Personal Projects/Dread Factor Map Stats.xlsx')

d_SKD=[round(squadKD(1),2),round(squadKD(2),2),round(squadKD(3),2),round(squadKD(4),2),round(squadKD(5),2)]

d_SWL=[round(squadWL(1),2),round(squadWL(2),2),round(squadWL(3),2),round(squadWL(4),2),round(squadWL(5),2)]

d_countSquad = [squadMatches(1),
                squadMatches(2),
                squadMatches(3),
                squadMatches(4),
                squadMatches(5)]

d_S={'Squad Size':[1,2,3,4,5]}
df1=pd.DataFrame(data=d_S)
df1["Matches"] = d_countSquad
df1['Win/Loss']=d_SWL
df1['Kill/Death']=d_SKD

df1.to_excel('/home/josh/Desktop/Personal Projects/Dread Factor Squad Stats.xlsx')

#%%




