moyenne=float(input("Entrez la moyenne : "))
if (moyenne>=0) and (moyenne<=20) :
    if (moyenne<10) :
        print("Médiocre, récalé")
    elif (moyenne<12) :
        print("Passable")
    elif (moyenne<14) :
        print("Assez-bien")
    elif (moyenne<16) :
        print("Bien")
    elif (moyenne<18) :
        print("Très bien")
    else :
        print("Les félicitations du jury")
else :
    print("Erreur, refait la saisie")