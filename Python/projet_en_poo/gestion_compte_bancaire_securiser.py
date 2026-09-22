class CompteBancaire:
    def __init__(self, proprietaire, solde):
        self.__proprietaire = proprietaire
        self.__solde = float(solde)

    def get_solde(self):
        return self.__solde

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
        else:
            print("Montant invalide.")

    def retirer(self, montant, limite=0):
        if montant > 0 and (self.__solde - montant) >= -limite:
            self.__solde -= montant
        else:
            print("Solde insuffisant.")

    def afficher_fiche(self):
        print(f"Proprietaire: {self.__proprietaire}, Solde du compte: {self.__solde}")


class CompteEpargne(CompteBancaire):
    def __init__(self, proprietaire, solde, taux_interet):
        super().__init__(proprietaire, solde)
        self.__taux_interet = taux_interet

    def retirer(self, montant):
        solde_apres_retrait = self.get_solde() - montant
        if solde_apres_retrait < 1000:
            print("Retrait refusé : le solde ne peut pas descendre sous 1000.")
        else:
            super().retirer(montant)

    def appliquer_interet(self):
        interets = self.get_solde() * self.__taux_interet
        self.deposer(interets)


class CompteCourant(CompteBancaire):
    def __init__(self, proprietaire, solde, decouvert_autorise):
        super().__init__(proprietaire, solde)
        self.__decouvert_autorise = decouvert_autorise

    def retirer(self, montant):
        super().retirer(montant, self.__decouvert_autorise)


# --- Tests ---
epargne = CompteEpargne("Awa", 1500, 0.03)
courant = CompteCourant("Mohamed", 200, 500)

print("Test 1:")
epargne.retirer(600)
print("Test 2:")
epargne.retirer(400)
print("Test 3:")
epargne.appliquer_interet()

print("Test 4:")
courant.retirer(500)
print("Test 5:")
courant.retirer(300)

print("Test 6:")
epargne.afficher_fiche()
print("Test 7:")
courant.afficher_fiche()

print(isinstance(epargne, CompteBancaire))
print(isinstance(courant, CompteEpargne))