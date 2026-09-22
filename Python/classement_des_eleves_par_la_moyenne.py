#Liste contenant les données des apprenants
students=[
    {
        "name":'John',
        "notes":[1,20,18,19,12]
    },
    {
        "name":'Jane',
        "notes":[17,18,20,13,15]
    },
    {
        "name":'Sophie',
        "notes":[17,12,14,15,13]
    },
    {
        "name":'Marc',
        "notes":[2,3,5,8,9]
    },
    {
        "name":'Manon',
        "notes":[18,17,18,19,12]
    }
]
#Fonction contenant le calcul des moyennes, fonction reuitilisable
def moyenne(notes):
    sum=int(0)
    for note in notes:
        sum+=note
    return sum/len(notes)

#Ajout de la clée moyenne dans la liste contenant le dictionnaire(élève)
for student in students:
    student["moyenne"]= moyenne(student["notes"])

#Trie par ordre décroissante les apprenants a partie de leurs moyennes
top_etudiants = sorted(students, key=lambda student: student["moyenne"], reverse=True)

#Affichage du top 3 des apprenants
for student in top_etudiants[:3]:
    print(f"{student['name']} : {student['moyenne']}")