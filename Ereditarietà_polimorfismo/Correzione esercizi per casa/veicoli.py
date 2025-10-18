class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrizione(self):
        return f"{self.marca}, {self.modello}, {self.anno}"
    
    def costo_manutenzione(self):
        pass

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, porte):
        super().__init__(marca, modello, anno)
        self.porte = porte
    #override
    def costo_manutenzione(self):
        costo = 1000+100*self.porte
        return costo
    
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, cilindrata):
        super().__init__(marca, modello, anno)
        self.cilindrata = cilindrata
    #override
    def costo_manutenzione(self):
        costo = 500+0.2*self.cilindrata
        return costo

class Camion(Veicolo):
    def __init__(self, marca, modello, anno, carico):
        super().__init__(marca, modello, anno)
        self.carico = carico
    #override
    def costo_manutenzione(self):
        costo = 2000+10*self.carico
        return costo
    
def stampa_costi(lista: list[Veicolo]):
    for mezzo in lista:
        mezzo = mezzo
        print(mezzo.costo_manutenzione())

#main
a1 = Auto("Audi", "A3", "2023", 5)
m1 = Moto("Kawasaki", "Ninja", "2019", 1000)
c1 = Camion("Mercedes", "B50", "2025", 1000)

lista_mezzi = [a1, m1, c1]

stampa_costi(lista_mezzi)