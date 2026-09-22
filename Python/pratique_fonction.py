#Méthode brut pour retourner le plus grand nombre d'une liste

#Fonction servant a récuper le plus grand nombre d'une liste(tableau)
def mon_max(nombres) :
    plus_grand=nombres[0]
    for nombre in nombres:
        if nombre > plus_grand:
            plus_grand=nombre
    return plus_grand

#initialisation de la liste
list_nombre=[]
print("Entrez 5 nombres")

#La boucle utiliser ici pour remplir la liste initialisée
for i in range(5):
    list_nombre.append(float(input(f"Entrez le nombre {i+1}: "))) #remplissage de la list

#affichage du resultat de la fonction
print(f"Le plus grand nombre de la liste est : {mon_max(list_nombre)}")

#Méthode simple avec une fonction spécifique [max()] pour retourner le plus grand nombre d'une list
print(f"Le plus grand nombre de la liste est: {max(list_nombre)}")

#Fonction pour inverser une liste: list( reversed(nom_liste) ) ou bien nom_liste[::-1]
#Avec cette fonction, on obtient une toutes nouvelles listes sans modification définitive de l'originale
list_inverser=list(reversed(list_nombre))
print(f"La liste inverser est: {list_inverser}")
list_inverser2= list_nombre[::-1]
print(f"La liste inverser est: {list_inverser2}")

#Fonction pour inverser une liste: nom_liste.reverse()
#Avec cette fonction, la liste original se fait définitivement modifier 
list_nombre.reverse()
print(f"La liste inverser est la suivante: {list_nombre}")