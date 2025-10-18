class Libro:
    def __init__(self, titolo: str, autore: str, anno: int):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
    
class Romanzo(Libro):
    def __init__(self, titolo:str, autore:str, anno:int, genere:str):
        super().__init__(titolo, autore, anno)
        self.genere = genere
    def __str__(self):
        return f"R;{self.titolo};{self.autore};{self.anno};{self.genere}"

class Saggio(Libro):
    def __init__(self, titolo:str, autore:str, anno:int, tema:str):
        super().__init__(titolo, autore, anno)
        self.tema = tema
    def __str__(self):
        return f"S;{self.titolo};{self.autore};{self.anno};{self.tema}"
    
class Biblioteca:
    def __init__(self):
        self.libri = [] #lista vuota pronta per contenere libri
    
    def aggiungiLibro(self, libro:Libro):
        self.libri.append(libro)

    def visualizzaLibri(self):
        for libro in self.libri:
            print(libro)

    def salvaLibri(self):
        with open("Ereditarietà_polimorfismo\\Esercizi in classe\\lista_libri.txt", "a") as file:
            for libro in self.libri:
                file.write(libro.__str__()+"\n")

    def caricaLibri(self):
        with open("Ereditarietà_polimorfismo\\Esercizi in classe\\lista_libri.txt", "r") as file:
            contenuto = file.read()
            """
            titolo;autore;anno;genere/tema\n
            """
            righe = contenuto.split("\n") #tutte le righe
            for riga in righe:
                if riga != "": #controllo che la riga non sia vuota (problema comune con l'ultima riga del file)
                    elementi = riga.split(";")
                    if elementi[0] == "R":
                        romanzo = Romanzo(elementi[1], elementi[2], elementi[3], elementi[4])
                        self.libri.append(romanzo)
                    else:
                        saggio = Saggio(elementi[1], elementi[2], elementi[3], elementi[4])
                        self.libri.append(saggio)


#main
#libro1 = Romanzo("Il signore degli anelli", "J.R.R. Tolkien", 1970, "Fantasy")
#saggio1 = Saggio("Entropia ed entalpia", "Mario Rossi", 2023, "Fisica")

bib = Biblioteca()

#bib.aggiungiLibro(libro1)
#bib.aggiungiLibro(saggio1)

bib.caricaLibri()
bib.visualizzaLibri()

#bib.salvaLibri()