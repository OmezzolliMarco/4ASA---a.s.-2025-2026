"""
Utilizzando le relazioni di ereditarietà realizza la classe Armadio sapendo che:

    Un armadio è composto da cassetti e ante
    
    Un cassetto eredita da parallelepipedo e possiede un certo numero di pomelli 
    e un bordo di un certo spessore (che si aggiugne al volume)
    
    Un'anta eredita da parallelepipedo ed è composta da un certo numero di 
    pomelli e un bordo di un certo spessore (che si aggiugne al volume)
    
    Parallelepipedo è una classe che al suo interno possiede attributi 
    quali altezza, larghezza e profondità
    
    Tutte le classi devono avere un metodo calcola volume che sovrascrive 
    il metodo di parallelepipedo (ad eccezione della classe Armadio)

Crea inoltre un menù che permette di creare un nuovo armadio chiedendo all'utente di 
inserire quanti cassetti lo compongono creando le loro istanze 
(ogni armadio deve sempre avere solo due ante, ma un numero non definito di cassetti). 
Crea inoltre un metodo nella classe armadio che permetta di prendere le misure di tutti i 
cassetti e delle ante e ritorni il volume totale occupato dal mobile (in cm o metri).
"""

class Parallelepipedo:
    def __init__(self, l:float, h:float, p:float):
        self.l = l
        self.h = h
        self.p = p
    def volume(self):
        return self.l * self.h * self.p
    
class Cassetto(Parallelepipedo):
    def __init__(self, l:float, h:float, p:float, bordo: float, pomelli: int):
        super().__init__(l, h, p)
        self.bordo = bordo
        self.h = self.h + self.bordo
        self.l += self.bordo
        self.p += self.bordo
        self.pomelli = pomelli
    def volume(self):
        volume_finale = super().volume() #richiamo al volume di parallelepipedo
        return volume_finale

class Anta(Parallelepipedo):
    def __init__(self, l:float, h:float, p:float, bordo: float, pomelli: int):
        super().__init__(l, h, p)
        self.bordo = bordo
        self.h = self.h + self.bordo
        self.l += self.bordo
        self.p += self.bordo
        self.pomelli = pomelli
    def volume(self):
        volume_finale = super().volume() #richiamo al volume di parallelepipedo
        return volume_finale

class Armadio:
    def __init__(self):
        self.cassetti = []
        self.ante = []

#main
armadio = Armadio()

volume_totale = 0

anta1 = Anta(5,5,5,0,1)
anta2 = Anta(5,5,5,0,1)

armadio.ante.append(anta1)
armadio.ante.append(anta2)

volume_totale += anta1.volume()
volume_totale += anta2.volume()

cassetti = int(input("Inserisci il numero di cassetti: "))
for i in range(cassetti):
    #creo i cassetti da aggiungere al mio armadio
    dati = input("Dammi altezza, larghezza e profondità del cassetto e bordo (separati da virgola): ")
    dati2 = dati.strip().split(",")
    pomelli = int(input("Inserisci il numero di pomelli: "))
    cassetto = Cassetto(int(dati2[0]), int(dati2[1]), int(dati2[2]), int(dati2[3]), pomelli)
    armadio.cassetti.append(cassetto)
    volume_totale += cassetto.volume()

#stampare il volume totale occupato
print(f"Il volume totale dell'armadio è: {volume_totale}")

