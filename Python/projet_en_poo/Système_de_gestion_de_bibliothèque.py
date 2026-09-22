from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, titre, identifiant_unique, statut='disponible'):
        self.__titre = titre
        self.__identifiant_unique = identifiant_unique
        self.__statut = statut

    def get_titre(self):
        return self.__titre

    @abstractmethod
    def duree_emprunt(self):
        pass

    def emprunter(self, date_retour):
        if self.__statut == 'disponible':
            self.__statut = 'emprunte'
            print(f"'{self.__titre}' emprunté. À rendre avant le : {date_retour}")
        else:
            print(f"'{self.__titre}' est déjà emprunté, impossible de l'emprunter.")

    def rendre(self):
        if self.__statut == 'emprunte':
            self.__statut = 'disponible'
            print(f"'{self.__titre}' a été rendu.")
        else:
            print(f"'{self.__titre}' n'était pas emprunté.")

    def affiche_info(self):
        print(f"{type(self).__name__} -> Titre: {self.__titre} ; ID: {self.__identifiant_unique} ; "
              f"Statut: {self.__statut} ; Durée d'emprunt: {self.duree_emprunt()} jours")


class Livre(Document):
    def __init__(self, titre, identifiant_unique, nombre_pages, statut='disponible'):
        super().__init__(titre, identifiant_unique, statut)
        self.__nombre_pages = nombre_pages

    def duree_emprunt(self):
        return 21


class DVD(Document):
    def __init__(self, titre, identifiant_unique, duree_film, statut='disponible'):
        super().__init__(titre, identifiant_unique, statut)
        self.__duree_film = duree_film

    def duree_emprunt(self):
        return 7


class Magazine(Document):
    def __init__(self, titre, identifiant_unique, edition_speciale=False, statut='disponible'):
        super().__init__(titre, identifiant_unique, statut)
        self.__edition_speciale = edition_speciale

    def duree_emprunt(self):
        return 3

    def emprunter(self, date_retour):
        if self.__edition_speciale:
            print(f"'{self.get_titre()}' est une édition spéciale, non empruntable.")
        else:
            super().emprunter(date_retour)


def afficher_tous(documents):
    for doc in documents:
        doc.affiche_info()


# --- Tests ---
livre1 = Livre("Le Petit Prince", "L001", 96)
dvd1 = DVD("Inception", "D001", 148)
mag1 = Magazine("Sciences & Vie", "M001", edition_speciale=False)
mag2 = Magazine("Hors-Série Espace", "M002", edition_speciale=True)

afficher_tous([livre1, dvd1, mag1, mag2])
print()

livre1.emprunter("2026-10-20")
livre1.emprunter("2026-10-25")     # refusé, déjà emprunté
dvd1.emprunter("2026-09-28")
mag1.emprunter("2026-09-24")
mag2.emprunter("2026-09-24")       # refusé, édition spéciale

print()
livre1.rendre()
mag2.rendre()                       # n'était pas emprunté

print()
afficher_tous([livre1, dvd1, mag1, mag2])