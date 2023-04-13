import pandas as pd

# data=pd.read_csv("C:/Users/aethe/OneDrive/Desktop/personal projects/stats/siege stats - Y7S4 - Solar Raid.csv")
data=pd.read_csv('/home/josh/Desktop/Personal Projects/siege stats - Y8S1 - Commanding Force.csv')
        
#%%

def winLoss(x):
    wins=len(data[(data['Map']==x)&(data['Outcome']=='win')])
    losses=len(data[(data['Map']==x)&(data['Outcome']=='loss')])
    
    if losses==0:
        if wins!=0:
            print(f'You have {wins} wins and 0 losses on {x}. Hats off!')
        else:
            print(f'You have not played {x} yet, or it does not exist.')
    else:
        WL=wins/losses
        print(f'Your win/loss ratio on {x} is {WL:.2}')

def killDeath(x):
    kills=data.loc[data['Map']==x,'Kills'].sum()
    deaths=data.loc[data['Map']==x,'Deaths'].sum()
    
    if deaths==0:
        if kills!=0:
            print(f'You have {kills} kills and 0 deaths on {x}. Hats off!')
        else:
            print(f'You have not played {x} yet, or it does not exist.')
    else:
        KD=kills/deaths
        print(f'Your kill/death ratio on {x} is {KD:.2}')

def killDeathAssist(x):
    kills=data.loc[data['Map']==x,'Kills'].sum()
    deaths=data.loc[data['Map']==x,'Deaths'].sum()
    assists=data.loc[data['Map']==x,'Assists'].sum()
    KDA=((kills+(0.33*assists))/deaths)
    if deaths==0:
        if kills!=0:
            print('You have ',kills,'kill(s), 0 deaths, and',assists,f'assist(s) on {x}.')
        else:
            print(f'{x} does not exist or you have not yet played it.')
    else:
        print(f'Your KDA on {x} is {KDA:.4f}.')
        
def squadWL(x):

    wins=len(data[(data['Squad Size']==x)&(data['Outcome']=='WIN')])
    losses=len(data[(data['Squad Size']==x)&(data['Outcome']=='LOSS')])
   
    if losses==0 & wins!=0:
        print(f'You have {wins} wins in a {x}-stack and 0 losses. Hats off!')
    elif wins==0:
        print(f'You have not played in a {x}-stack before.')
    else:
        squad_WL=wins/losses
        print(f'Your win/loss ratio in a {x}-stack is {squad_WL:.2f}')

def squadKD(x):
    
    kills=data.loc[data['Squad Size']==x,'Kills'].sum()
    deaths=data.loc[data['Squad Size']==x,'Deaths'].sum()
    
    if deaths==0 and kills!=0:
        print(f'You have {kills} kills and 0 deaths in a {x}-stack.  Hats off!')
    elif kills==0:
        print(f'You have not played in a {x}-stack before.')
    else:
        squad_KD=kills/deaths
        print(f'Your kill/death ratio in a {x}-stack is {squad_KD:.2f}')
        
def summary(x):
    winLoss(x)
    killDeath(x)

def summarySquad(x):
    squadWL(x)
    squadKD(x)
        

#%%

def attack(x):
    attackWins=data.loc[data['Map']==x,'ATK Wins'].sum()
    attackLosses=data.loc[data['Map']==x,'ATK Losses'].sum()
    print(f'You have {attackWins} wins and {attackLosses} losses when attacking on {x}.')
    
    while True:
        if attackLosses==0:
            break
        elif attackWins==0:
            break
        else:
            attackWinRatio=attackWins/attackLosses
            print(f'This is a a win/loss of {attackWinRatio} on attack.')
            break

def defense(x):
    defenseWins=data.loc[data['Map']==x,'DEF Wins'].sum()
    defenseLosses=data.loc[data['Map']==x,'DEF Losses'].sum()
    print(f'You have {defenseWins} wins and {defenseLosses} losses when defending on {x}.')
    
    while True:
        if defenseLosses==0:
            break
        elif defenseWins==0:
            break
        else:
            defenseWinRatio=defenseWins/defenseLosses
            print(f"This is a win/loss ratio of {defenseWinRatio}  on defense.")
            break

def attackDefense(x):
    attack(x)
    defense(x)
#%%

attackDefense('Bank')
attackDefense('Border')
attackDefense('Coastline')
attackDefense('Consulate')
attackDefense('Chalet')
attackDefense('Club House')
attackDefense('Emerald Plains')
attackDefense('Kafe Dostoyevsky')
attackDefense('Kanal')
attackDefense('Nighthaven Labs')
attackDefense('Oregon')
attackDefense('Outback')
attackDefense('Skyscraper')
attackDefense('Stadium Bravo')
attackDefense('Theme Park')
attackDefense('Villa')





#%%
'''Win/Loss Ratio'''

winLoss('Bank')
winLoss('Border')
winLoss('Coastline')
winLoss('Consulate')
winLoss('Chalet')
winLoss('Club House')
winLoss('Emerald Plains')
winLoss('Kafe Dostoyevsky')
winLoss('Kanal')
winLoss('Nighthaven Labs')
winLoss('Oregon')
winLoss('Outback')
winLoss('Skyscraper')
winLoss('Stadium Bravo')
winLoss('Theme Park')
winLoss('Villa')

#%%
'''Kill/Death Ratio'''

killDeath('Bank')
killDeath('Border')
killDeath('Coastline')
killDeath('Consulate')
killDeath('Chalet')
killDeath('Club House')
killDeath('Emerald Plains') # Played once during Y7S4
killDeath('Kafe Dostoyevsky')
killDeath('Kanal')
killDeath('Nighthaven Labs')
killDeath('Oregon')
killDeath('Outback')
killDeath('Skyscraper')
killDeath('Stadium Bravo')
killDeath('Theme Park')
killDeath('Villa')

#%%
'''Kill/Death & Assist Ratio'''
killDeathAssist('Bank')
killDeathAssist('Border')
killDeathAssist('Coastline')
killDeathAssist('Consulate')
killDeathAssist('Chalet')
killDeathAssist('Club House')

killDeathAssist('Emerald Plains')

killDeathAssist('Kafe Dostoyevsky')
killDeathAssist('Kanal')
killDeathAssist('Nighthaven Labs')
killDeathAssist('Oregon')
killDeathAssist('Outback')
killDeathAssist('Skyscraper')
killDeathAssist('Stadium Bravo')
killDeathAssist('Theme Park')
killDeathAssist('Villa')

#%%
'''Squad Information'''

summarySquad(1)
summarySquad(2)
summarySquad(3)
summarySquad(4)
summarySquad(5)

#%%







#%%
'''
Archive v1



WIN/LOSS

def winLoss(x):
    if len(df[(df['Outcome']=='LOSS') & (df['Map']==x)])==0:
        if len(df[(df['Outcome']=='WIN') & (df['Map']==x)])!=0:
               print('You have',len(df[(df['Outcome']=='WIN') & (df['Map']==x)]),f'win(s), 0 losses on {x}.')
        else:
            print(f'{x} does not exist or you have not yet played it.')
    else:
        WL=(len(df[(df['Outcome']=='WIN') & (df['Map']==x)])/len(df[(df['Outcome']=='LOSS') & (df['Map']==x)])) # Sums the number of wins and losses on a map and divides
        print(f"Your win/loss ratio on {x} is {WL:.2f}.")



KILL/DEATH

def killDeath(x):
    if df.loc[df['Map']==x,'Deaths'].sum()==0:
        if df.loc[df['Map']==x,'Kills'].sum()!=0:
            print('You have ',df.loc[df['Map']==x,'Kills'].sum(),f'kill(s), 0 deaths on {x}.')
        else:
            print(f'{x} does not exist or you have not yet played it.')
    else:
        KD=(df.loc[df['Map']==x,'Kills'].sum()/df.loc[df['Map']==x,'Deaths'].sum())
        print(f'Your kill/death ratio on {x} is {KD:.2f}.
'''
#%%
'''
Archive v2

Changelog:
    cleaned up winLoss and killDeath
        assigned variables replace raw code
        return format changed
    added killDeathAssist

def winLoss(x):
    loss=len(df[(df['Outcome']=='LOSS') & (df['Map']==x)])
    win=len(df[(df['Outcome']=='WIN') & (df['Map']==x)])
    if loss==0:
        if win!=0:
               print('You have',win,f'win(s), 0 losses on {x}.')
        else:
            print(f'{x} does not exist or you have not yet played it.')
    else:
        win_loss=win/loss
        print(f"Your win/loss ratio on {x} is {win_loss:.2f}.")


def killDeath(x):
    kill=df.loc[df['Map']==x,'Kills'].sum()
    death=df.loc[df['Map']==x,'Deaths'].sum()
    if death==0:
        if kill!=0:
            print('You have ',kill,f'kill(s), 0 deaths on {x}.')
        else:
            print(f'{x} does not exist or you have not yet played it.')
    else:
        KD=kill/death
        print(f'Your kill/death ratio on {x} is {KD:.2f}.')
'''

#%%

'''
v3 Changelog:
    data now assigned to 'data', was 'stats'
        functions updated to match
    winLoss, killDeath, killDeathAssist updated
        kill, death, win, loss, assist variables renamed to plural forms
        output changed
    summary added
    squadWL added
    squadKD added
    summarySquad added
    reorganized
        functions now are all contained in one cell and all listed before any calls
'''