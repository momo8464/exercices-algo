from abc import ABC, abstractmethod
class Personne(ABC):
    def __init__(self,nom,age):
        self.__nom=nom
        self.__age=age

    def get_nom(self):
        return self.__nom

    @abstractmethod
    def role(self):
        pass

    def afficher_info(self):
        print(f"{type(self).__name__} ->  Nom: {self.__nom}; Age: {self.__age}; Role: {self.role()}")

class Eleve(Personne):
    def __init__(self, nom, age,classe, notes):
        super().__init__(nom, age)
        self.__classe=str(classe)
        self.__notes=list(notes)
        
    def role(self):
        roles="Élève"
        return roles

    def ajouter_note(self, note):
        for n in note:
            if n>0 and n<=20:
                self.__notes+=[n]
            else:
                print("Impossible a prendre en compte, une des notes est superieur a 20 ou inferieur a 0")

    def moyenne(self):
        somme=0
        if self.__notes==[]:
            return 0
        else:
            for n in self.__notes:
                somme+=n
        Moyenne=somme/len(self.__notes)
        print(f"Moyenne = {Moyenne}")
        return Moyenne

    def afficher_bulletin(self):
        print(f"Nom: {self.get_nom()} ; Classe: {self.__classe}; Notes: {self.__notes}; Moyenne: {self.moyenne()}")

class Enseignant(Personne):
    def __init__(self, nom, age,matiere,salaire_horaire,heures_travaillees=0):
        super().__init__(nom, age)
        self.__matiere=matiere
        self.__salaire_horaire=salaire_horaire
        self.__heures_travaillees=heures_travaillees

    def role(self):
        roles="Enseignant"
        return roles

    def ajouter_heures(self, heures):
        if heures>=0:
            self.__heures_travaillees+=heures
            return self.__heures_travaillees
        else:
            print("Pas d'heure de travaille")
            return 0

    def calculer_paie(self):
        salaire= self.__salaire_horaire * self.__heures_travaillees
        print(f"Salaire de {self.get_nom()} : {salaire}; Matiere: {self.__matiere}")
        return salaire

def afficher_tous(liste_personnes): #Liste pouvant etre mix
    for liste in liste_personnes:
        liste.afficher_info()

def liste_bulletin(liste_eleves):
    for bulletin in liste_eleves:
        bulletin.afficher_bulletin()
def liste_paie(liste_enseignants):
    for liste in liste_enseignants:
        liste.calculer_paie()

#---test---
#---creation d'objet---
eleve1=Eleve(nom="Kone",age=23,classe="Terminal D",notes=[14,17,19,20])
eleve2=Eleve(nom="Adam's",age=30,classe="Terminal C",notes=[19,20,18])
eleve3=Eleve(nom="Koffi",age=30,classe="Terminal C",notes=[])

enseignant1=Enseignant(nom="M.Kone",age=30,matiere="Mathematiques",salaire_horaire=600,heures_travaillees=12)
enseignant2=Enseignant(nom="M.Adam's",age=50,matiere="Physique-chimie",salaire_horaire=500,heures_travaillees=10)

print()
#---liste des etudiants et des enseignants
print("1: ")
afficher_tous([
    eleve1,eleve2,eleve3,enseignant1,enseignant2
])

print()
#liste des bulletins de chaque eleves
print("2:Liste des bulletin avant l'ajout des nouvelles notes: ")
liste_bulletin([
    eleve1,eleve2,eleve3
])

print()
#test sur les moyennes et l'ajout des notes
print("3: ")
eleve1.ajouter_note([10])
print("4: ")
eleve1.moyenne()

print("5: ")
eleve2.ajouter_note([-10])
print("6: ")
eleve2.moyenne()

print("7: ")
eleve3.ajouter_note([20,13])
print("8: ")
eleve3.moyenne()

print()
#test sur l'ajout de l'heure et sur la paie de chaques enseignants
print("9: ")
enseignant1.ajouter_heures(20)
print("10: ")
enseignant2.ajouter_heures(-2)

print("11: ")
liste_paie([
    enseignant1,enseignant2
])

print()
#liste des bulletins de chaque eleves apres modifications des notes
print("12:Liste des bulletin apres l'ajout des nouvelles notes: ")
liste_bulletin([
    eleve1,eleve2,eleve3
])