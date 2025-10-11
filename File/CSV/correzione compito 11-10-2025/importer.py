import csv

class Studente:
    def __init__(self, nome, cognome, eta, voto_medio):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.voto_medio = voto_medio
    
    def __str__(self):
        return f"{self.nome}, {self.cognome}"

#main
lista_stud = []
with open("File\\CSV\\correzione compito 11-10-2025\\studenti.csv") as elenco:
    reader = csv.reader(elenco, delimiter=",") #crea una lista di righe partendo dal file
    ##[
    ##["Mario", "Rossi", ...] -> riga
    ##["Anna", "Verdi", ...] -> riga
    ##]
    for riga in reader:
        nome, cognome, eta, voto_medio = riga 
        stud = Studente(nome, cognome, eta, voto_medio)
        lista_stud.append(stud)

for s in lista_stud:
    print(s)
