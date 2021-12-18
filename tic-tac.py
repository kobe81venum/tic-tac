#%%
#main game section

# %%
plansza_do_gry = {'7':' ','8':' ','9':' ',
                  '4':' ','5':' ','6':' ',
                  '1':' ','2':' ','3':' '}

klawisze_gry=[]

for key in plansza_do_gry:
    klawisze_gry.append(key)

print(klawisze_gry)

def drukuj_plansze():
    print(' ' + '|' + ' ' + '|')
    print('-+-+-')
    print(' ' + '|' + ' ' + '|')
    print('-+-+-')
    print(' ' + '|' + ' ' + '|')
    print('-+-+-')
    
drukuj_plansze()

# %%
