ventes_du_jour=[45.0, 120.5, 19.99, 250.0, 85.40]
chiffre_affaires=0
#incrementation du chiffre d'affaire
for i in ventes_du_jour :
    chiffre_affaires+=i
    print(f"Vente enregistrer: {i} fcfa")
print(f"Le chiffre d'affaire total est : {chiffre_affaires} fcfa")