def muovi_veicoli(listaVeicoli:list):
    for veicolo in listaVeicoli:
        veicolo.spostati()

class Veicolo:
    def __init__(self, nome):
        self.nome = nome
    def spostati(self):
        pass

class Auto(Veicolo):
    def __init__(self, nome):
        super().__init__(nome)
    #override
    def spostati(self):
        print("Viaggio su strada")

class Bici(Veicolo):
    def __init__(self, nome):
        super().__init__(nome)
    #override
    def spostati(self):
        print("Pedala!")

class Aereo(Veicolo):
    def __init__(self, nome):
        super().__init__(nome)
    #override
    def spostati(self):
        print("Volo!")

#main
a1 = Auto("A1")
a2 = Auto("A2")

b1 = Bici("B1")

ar1 = Aereo("Aereo1")

listaVeicoli = []
listaVeicoli.append(a1)
listaVeicoli.append(a2)
listaVeicoli.append(b1)
listaVeicoli.append(ar1)

muovi_veicoli(listaVeicoli)