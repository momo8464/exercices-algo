class Produit:
    def __init__(self, nom, prix=0, quantite_stock=0, seuil_alerte=0):
        self.__nom = nom
        if prix <= 0:
            print("Prix invalide, le prix a été fixé à 0.")
            self.__prix = 0.0
        else:
            self.__prix = float(prix)
        self.__quantite_stock = int(quantite_stock)
        self.__seuil_alerte = int(seuil_alerte)

    def vendre(self, quantite):
        if quantite<=0:
            print("Impossible a vendre, quantite insuffisante")
            return

        if quantite>self.__quantite_stock:
            print("Quantite insuffisante")
            return

        self.__quantite_stock-=quantite
        vendre=(quantite*self.__prix)
        print(f"Montant total de vente: {vendre}")

        if self.__quantite_stock < self.__seuil_alerte:
            print("Stock faible, pensez à réapprovisionner")

    def reapprovisionner(self, quantite):
        if quantite<=0:
            print("quantite insuffisante")
            return
        self.__quantite_stock+=quantite

    def changer_prix(self, nouveau_prix):
        if nouveau_prix<=0:
            print("Changement prix impossible")
        else:
            ancien_prix=self.__prix
            self.__prix=nouveau_prix
            print(f"Ancient prix: {ancien_prix}, Nouveau prix: {nouveau_prix}")

    def afficher_fiche(self):
        print(f"Nom du produit: {self.__nom}")
        print(f"Prix du produit: {self.__prix}")
        print(f"Quantite en stock: {self.__quantite_stock}")

#creation produit
produit1 = Produit(nom="Gommage", prix=2000, quantite_stock=50, seuil_alerte=25)

produit1.vendre(30)
produit1.vendre(60)
produit1.vendre(-2)
produit1.reapprovisionner(50)
produit1.reapprovisionner(-1)
produit1.changer_prix(-4000)
produit1.changer_prix(4000)
produit1.afficher_fiche()