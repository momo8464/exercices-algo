panier=float(input("Entrez le montant de votre panier: "))
if (panier>=50) :
    print(f"Livraison offerte ! Le montant total de la commande est : {panier} £")
else :
    panier_avec_frais= panier + 4.90
    print(f"Le montant total de la commande est : {panier_avec_frais} £")