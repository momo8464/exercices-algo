from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass

    def afficher_infos(self):
        print(f"{type(self).__name__} -> Aire: {self.aire():.2f}, Périmètre: {self.perimetre():.2f}")

class Rectangle(Forme):
    def __init__(self,largeur, hauteur):
        super().__init__()
        self.largeur=largeur
        self.hauteur=hauteur

    def aire(self):
        return self.largeur*self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

class Cercle(Forme):
    def __init__(self,rayon):
        super().__init__()
        self.rayon=rayon

    def aire(self):
        return 3.14159 * self.rayon ** 2

    def perimetre(self):
        return 2 * 3.14159 * self.rayon

class Triangle(Forme):
    def __init__(self,base, hauteur,cote1, cote2, cote3):
        super().__init__()
        self.base=base
        self.hauteur=hauteur
        self.cote1=cote1
        self.cote2=cote2
        self.cote3=cote3

    def aire(self):
        return (self.base * self.hauteur) / 2

    def perimetre(self):
        return self.cote1 + self.cote2 + self.cote3

def aire_totale(liste_formes):
    total = 0
    for forme in liste_formes:
        total += forme.aire()
    return total

formes = [
    Rectangle(4, 5),
    Cercle(3),
    Triangle(6, 4, 5, 6, 7)
]

for f in formes:
    f.afficher_infos()

print(f"Aire totale : {aire_totale(formes):.2f}")

# forme_test = Forme()   # doit lever une erreur si tu décommentes cette ligne