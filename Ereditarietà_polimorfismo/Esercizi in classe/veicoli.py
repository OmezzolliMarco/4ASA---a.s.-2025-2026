#classe padre
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def __str__(self):
        return f"Veicolo di marca {self.marca} e modello {self.modello}"
    
class Auto(Veicolo):
    def __init__(self, marca, modello, nPorte=3):
        super().__init__(marca, modello)
        self.nPorte = nPorte
    def __str__(self): #override del metodo del padre
        return f"Veicolo di marca {self.marca} e modello {self.modello} e n. porte {self.nPorte}"

class Moto(Veicolo):
    def __init__(self, marca, modello, tipo):
        super().__init__(marca, modello)
        self.tipo = tipo
    
    def stampaMoto(self):
        primaStampa=super().__str__()
        print(f"{primaStampa} e di tipo {self.tipo}")


#main
a1 = Auto("Minicooper", "Mini")
m1 = Moto("Kawasaki", "Ninja", "Corsa")

print(a1)
print(m1)
m1.stampaMoto()