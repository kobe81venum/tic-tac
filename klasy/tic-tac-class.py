#%%

# class moja_klasa:
#     def wyswietl(x):
#         return 'Witaj swiecie'

# x = moja_klasa()
# print(x.wyswietl())
# %%

class prostopadloscian:
    def __init__(self): #konstruktor klasy włącza się jako pierwszy
        self.podstawa_a = 0 #domyslnie ustawiamy wartosc
        self.podstawa_b = 0
        self.wysokosc_h = 0

    def objetosc(self):
        return self.podstawa_a * self.podstawa_b * self.wysokosc_h

wtc = prostopadloscian()
wtc.podstawa_a = 100
wtc.podstawa_b = 200
wtc.wysokosc_h = 400
print(wtc.objetosc())


# %%
class prostopadloscian:
    def __init__(self): #konstruktor klasy włącza się jako pierwszy
        self.podstawa_a = 0 #domyslnie ustawiamy wartosc
        self.podstawa_b = 0
        self.wysokosc_h = 0

    def objetosc(self):
        return self.podstawa_a * self.podstawa_b * self.wysokosc_h