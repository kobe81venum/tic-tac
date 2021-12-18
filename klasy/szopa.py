#%%
class szopa:
    # pomalowanebudynki = 0
    def __init__(self,bok_a,bok_b,wys_h): #konstruktor klasy włącza się jako pierwszy
        self.podstawa_a = bok_a #domyslnie ustawiamy wartosc
        self.podstawa_b = bok_b
        self.wysokosc_h = wys_h

    # pomalowanebudynki += 1

    def pomaluj(self):
        #self.wysokosc_h = 20 # możemu=y nadpisac
        return 2*(self.podstawa_a + self.podstawa_b) * self.wysokosc_h

szopa1=szopa(2,3,5)
print(szopa1.pomaluj())
szopa2=szopa(5,1,2)
print(szopa2.pomaluj())
# print(szopa1.pomalowanebudynki)
# print(szopa1.pomalowanebudynki)

# %%
