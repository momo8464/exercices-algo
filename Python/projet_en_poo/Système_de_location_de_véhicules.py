from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, marque, immatriculation, kilometrage, statut='disponible'):
        self.__marque = marque
        self.__immatriculation = immatriculation
        self.__kilometrage = kilometrage
        self.__statut = statut

    def get_marque(self):
        return self.__marque

    def get_kilometrage(self):
        return self.__kilometrage

    @abstractmethod
    def tarif_location(self):
        pass

    def louer(self, nombre_jours):
        if self.__statut == 'disponible':
            self.__statut = 'loue'
            total_tarif = self.tarif_location() * nombre_jours
            print(f"{self.__marque} louée : {total_tarif:.2f} fcfa pour {nombre_jours} jour(s).")
            return total_tarif
        else:
            print(f"{self.__marque} n'est pas disponible (statut : {self.__statut}).")
            return 0

    def restituer(self, km):
        self.__statut = 'disponible'
        self.__kilometrage += km
        print(f"{self.__marque} restituée. Nouveau kilométrage : {self.__kilometrage}")

    def afficher_info(self):
        print(f"{type(self).__name__} -> Marque: {self.__marque}; Immatriculation: {self.__immatriculation}; "
              f"Kilométrage: {self.__kilometrage}; Statut: {self.__statut}")


class Voiture(Vehicule):
    def __init__(self, marque, immatriculation, kilometrage, tarif_base, nombre_porte=4, statut='disponible'):
        super().__init__(marque, immatriculation, kilometrage, statut)
        self.__tarif_base = tarif_base
        self.__nombre_porte = nombre_porte

    def tarif_location(self):
        if self.__nombre_porte > 4:
            return self.__tarif_base + 5000
        else:
            return self.__tarif_base


class Utilitaire(Vehicule):
    def __init__(self, marque, immatriculation, kilometrage, tarif_base, capacite_charge, permis=True, statut='disponible'):
        super().__init__(marque, immatriculation, kilometrage, statut)
        self.__tarif_base = tarif_base
        self.__capacite_charge = capacite_charge
        self.__permis = permis

    def tarif_location(self):
        if self.__capacite_charge > 5000:
            return self.__tarif_base + 7000
        else:
            return self.__tarif_base

    def louer(self, nombre_jours):
        if self.__permis:
            return super().louer(nombre_jours)
        else:
            print(f"{self.get_marque()} ne peut pas être louée : permis requis manquant.")
            return 0


class Moto(Vehicule):
    def __init__(self, marque, immatriculation, kilometrage, tarif_base, cylindree, statut='disponible'):
        super().__init__(marque, immatriculation, kilometrage, statut)
        self.__tarif_base = tarif_base
        self.__cylindree = cylindree

    def tarif_location(self):
        if self.__cylindree > 800:
            return self.__tarif_base - 7000
        else:
            return self.__tarif_base

    def louer(self, nombre_jours):
        if self.get_kilometrage() > 50000:
            print(f"{self.get_marque()} ne peut pas être louée : kilométrage trop élevé.")
            return 0
        else:
            return super().louer(nombre_jours)


def revenue_total(liste_vehicule, nombre_jours):
    total = 0
    for vehicule in liste_vehicule:
        total += vehicule.louer(nombre_jours)
    return total


# --- Tests ---
voiture1 = Voiture("Toyota", "AB-123-CD", 15000, 26000, 4)
voiture2 = Voiture("Peugeot", "EF-456-GH", 8000, 26000, 5)
utilitaire1 = Utilitaire("Renault", "IJ-789-KL", 40000, 30000, 1200, permis=True)
utilitaire2 = Utilitaire("Renault", "IP-789-KL", 30000, 50000, 1700, permis=False)
moto1 = Moto("Yamaha", "MN-012-OP", 3000, 67000, 600)
moto2 = Moto("Honda", "QR-345-ST", 55000, 67666, 125)

vehicules = [voiture1, voiture2, utilitaire1, utilitaire2, moto1, moto2]

print("--- État initial ---")
for v in vehicules:
    v.afficher_info()

print("\n--- Locations ---")
voiture1.louer(3)
voiture1.louer(2)        # refusé, déjà louée
utilitaire1.louer(5)
utilitaire2.louer(5)     # refusé, pas de permis
moto1.louer(1)
moto2.louer(1)           # refusé, kilométrage trop élevé

print("\n--- Restitution ---")
voiture1.restituer(450)

print("\n--- Revenu total pour 2 jours ---")
revenu = revenue_total(vehicules, 2)
print(f"Revenu total : {revenu:.2f} fcfa")

print("\n--- État final ---")
for v in vehicules:
    v.afficher_info()