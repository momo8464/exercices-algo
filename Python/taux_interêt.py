capital=float(input("Entrez le capital de départ: "))
interet=float(input("Entrez le taux d'interêt en pourcentage: "))
annees=int(input("Entrez le nombre d'années: "))
for i in range(annees) :
    capital=capital + capital*(interet/100)
    print(f"Année {i+1} : {round(capital,5)} fcfa")