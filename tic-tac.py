#main game section

# %%
plansza_do_gry = {'7':' ','8':' ','9':' ',
                  '4':' ','5':' ','6':' ',
                  '1':' ','2':' ','3':' '}

klawisze_gry=[]

for key in plansza_do_gry:
    klawisze_gry.append(key)

# print(klawisze_gry)

def drukuj_plansze(pole):
    print(f"{pole['7']} | {pole['8']} | {pole['9']}")
    print('- + - + -')
    print(f"{pole['4']} | {pole['5']} | {pole['6']}")
    print('- + - + -')
    print(f"{pole['1']} | {pole['2']} | {pole['3']}")

# drukuj_plansze(plansza_do_gry)

def gra():

    gracz = 'X'
    licznik=0

    for i in range(10):
        drukuj_plansze(plansza_do_gry)

        move=input(f"To jest ruch, {gracz}. Wybierz gdzie chcesz postawić znak")

        if plansza_do_gry[move] == ' ':
            plansza_do_gry[move] = gracz
            licznik += 1
        else:
            print('miejsce zajęte\nwstaw znak w inne pole')
            continue

        if licznik >=5:  #i
            if plansza_do_gry['7'] == plansza_do_gry['8'] == plansza_do_gry['9'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print("\nKoniec Gry")
                print(f"Wygrał gracz: {gracz}")
                break
            elif plansza_do_gry['4'] == plansza_do_gry['5'] == plansza_do_gry['6'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print("\nKoniec Gry")
                print(f"Wygrał gracz: {gracz}")
                break
            elif plansza_do_gry['1'] == plansza_do_gry['2'] == plansza_do_gry['3'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print("\nKoniec Gry")
                print(f"Wygrał gracz: {gracz}")
                break
            elif plansza_do_gry['1'] == plansza_do_gry['4'] == plansza_do_gry['7'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print("\nKoniec Gry")
                print(f"Wygrał gracz: {gracz}")
                break
            elif plansza_do_gry['2'] == plansza_do_gry['5'] == plansza_do_gry['8'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print("\nKoniec Gry")
                print(f"Wygrał gracz: {gracz}")
                break
            elif plansza_do_gry['3'] == plansza_do_gry['6'] == plansza_do_gry['9'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print("\nKoniec Gry")
                print(f"Wygrał gracz: {gracz}")
                break
            elif plansza_do_gry['1'] == plansza_do_gry['5'] == plansza_do_gry['9'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print("\nKoniec Gry")
                print(f"Wygrał gracz: {gracz}")
                break
            elif plansza_do_gry['3'] == plansza_do_gry['5'] == plansza_do_gry['7'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print("\nKoniec Gry")
                print(f"Wygrał gracz: {gracz}")
                break

            if licznik == 9:
                print("\nKoniec Gry")
                print("remis")

        if gracz == 'X':
            gracz = 'O'
        else:
            gracz = 'X'

    restart = input('grasz ponownie?/n(t/n')
    if restart == 't' or restart == 'T':
        for key in klawisze_gry:
            plansza_do_gry[key] = ' '

        gra()   #wywołanie rekurencyjne
#superfunkcja
if __name__ == '__main__': #dotyczy pakietów i pakowania do pakietu
    gra()

# %%
