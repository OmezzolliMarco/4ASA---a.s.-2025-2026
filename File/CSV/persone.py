'''
Nome,Cognome,Eta,Citta
Mario,Rossi,16,Arco
Luigi,Bianchi,17,Riva del Garda
Anna,Verdi,16,Dro
'''

import csv #importare la libreria per la gestione di csv in Python

class Persona:
    def __init__(self, nome, cognome, eta, citta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta

    
#main
persone = []
#file=open("elenco.csv")
with open("C:\\Users\\marco\\Documents\\GitHub\\4ASA---a.s.-2025-2026\\File\\CSV\\elenco.csv") as file:
    reader = csv.reader(file, delimiter=",")
    for riga in reader:
        #riga=["Mario", "Rossi", "16", "Arco"]
        persona = Persona(riga[0], riga[1], int(riga[2]), riga[3])
        #oppure
        nome,cognome,eta,citta=riga
        persona = Persona(nome, cognome, eta, citta)

        #aggiungo la persona appena creata alla lista
        persone.append(persona)