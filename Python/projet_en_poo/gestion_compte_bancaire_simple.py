class comptbanque:
    def __init__(self,proprietaire,solde=0):
        self.proprietaire=proprietaire
        self.solde=solde

    def deposer(self,montant):
        self.solde+=montant
        print(f"Montant deposer: {montant}; solde du compte: {self.solde}")

    def retirer(self,montant):
        if montant>self.solde :
            print("Solde insuffisant")
        else:
            self.solde-=montant
            print(f"Retrait de {montant} ;Solde du compte: {self.solde}")

#Creation d'objet
compte1=comptbanque(proprietaire="Mohamed",solde=500)
compte2=comptbanque(proprietaire="Bamba",solde=200)

compte1.deposer(1000)
compte1.retirer(200)