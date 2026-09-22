class Employe:
    def __init__(self, nom, salaire_base):
        self.__nom=nom
        self.__salaire_base=float(salaire_base)

    def get_nom(self):
        return self.__nom
    
    def calculer_salaire(self):
        return self.__salaire_base

    def afficher_fiche(self):
        print(f"Nom: {self.__nom}, Salaire de base: {self.calculer_salaire()}")

class Manager(Employe):
    def __init__(self, nom, salaire_base, prime):
        super().__init__(nom, salaire_base)
        self.__prime=float(prime)

    def calculer_salaire(self):
        return super().calculer_salaire() + self.__prime

    def gerer_equipe(self):
        print(f"{self.get_nom()} gère son équipe.")

class Developpeur(Employe) :
    def __init__(self, nom, salaire_base, nb_projets):
        super().__init__(nom, salaire_base)
        self.__nb_projets=int(nb_projets)

    def calculer_salaire(self):
        return super().calculer_salaire()+ (10000*self.__nb_projets)

    def coder(self):
        print(f"{self.get_nom()} code sur {self.__nb_projets} projet(s).")

manager = Manager("Awa", 300000, 50000)
dev = Developpeur("Mohamed", 250000, 3)

manager.afficher_fiche()   # doit utiliser calculer_salaire() -> inclut la prime
dev.afficher_fiche()       # doit utiliser calculer_salaire() -> inclut le bonus projets

manager.gerer_equipe()
dev.coder()

print(isinstance(manager, Employe))     # True
print(isinstance(dev, Manager))         # False