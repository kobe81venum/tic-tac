#%%
class kot:
    def __init__(self): #konstruktor klasy włącza się jako pierwszy
        self.imie = 0
        self.kol_oczu = 0
        self.kol_siersc = 0
        self.dlugosc = 0        
        self.wysokosc = 0        
        self.wiek = 0        
        self.waga = 0        

    def miauczenie(self):
        return "Miauuu"
    def jedzenie(self):
        return "jedz"
    def spanie(self):
        return "spij"
    def drapanie(self):
        return "drap"
    def mruczenie(self):
        return "mrucz"        

kot1 = kot(15,25,44,45,30,5,25)
print(kot1)
# %%
