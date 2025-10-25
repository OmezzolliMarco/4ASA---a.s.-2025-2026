"""
Utilizzando le relazioni di ereditarietà realizza la classe Armadio sapendo che:

    Un armadio è composto da cassetti e ante
    Un cassetto eredita da parallelepipedo e possiede un certo numero di pomelli e un bordo di un certo spessore (che si aggiugne al volume)
    Un'anta eredita da parallelepipedo ed è composta da un certo numero di pomelli e un bordo di un certo spessore (che si aggiugne al volume)
    Parallelepipedo è una classe che al suo interno possiede attributi quali altezza, larghezza e profondità
    Tutte le classi devono avere un metodo calcola volume che sovrascrive il metodo di parallelepipedo (ad eccezione della classe Armadio)

Crea inoltre un menù che permette di creare un nuovo armadio chiedendo all'utente di 
inserire quanti cassetti lo compongono creando le loro istanze 
(ogni armadio deve sempre avere solo due ante, ma un numero non definito di cassetti). 
Crea inoltre un metodo nella classe armadio che permetta di prendere le misure di tutti i 
cassetti e delle ante e ritorni il volume totale occupato dal mobile (in cm o metri).
"""