class CompteUtilisateur:
    def __init__(self, nom_utilisateur, email, mot_de_passe):
        self.__nom_utilisateur = nom_utilisateur
        self.__email = email
        self.__mot_de_passe = mot_de_passe
        self.__tentatives_echouees = 0
        self.__verrouille = False

    def se_connecter(self, mot_de_passe_saisi):
        if self.__verrouille:
            print("Compte verrouillé. Connexion impossible.")
            return

        if mot_de_passe_saisi == self.__mot_de_passe:
            self.__tentatives_echouees = 0
            print("Connexion réussie.")
        else:
            self.__tentatives_echouees += 1
            print(f"Mot de passe incorrect. Tentative {self.__tentatives_echouees}/3.")

            if self.__tentatives_echouees >= 3:
                self.__verrouille = True
                print("Compte verrouillé.")

    def changer_email(self, nouvel_email):
        if "@" not in nouvel_email:
            print("Email invalide : un email doit contenir '@'.")
            return

        self.__email = nouvel_email
        print("Email mis à jour avec succès.")

    def changer_mot_de_passe(self, ancien_mot_de_passe, nouveau_mot_de_passe):
        if ancien_mot_de_passe != self.__mot_de_passe:
            print("Ancien mot de passe incorrect.")
            return

        if len(nouveau_mot_de_passe) < 6:
            print("Le nouveau mot de passe doit contenir au moins 6 caractères.")
            return

        self.__mot_de_passe = nouveau_mot_de_passe
        print("Mot de passe mis à jour avec succès.")

    def afficher_infos(self):
        print(f"Utilisateur : {self.__nom_utilisateur}")
        print(f"Email : {self.__email}")


# --- Tests ---
compte = CompteUtilisateur("Mohamed", "mohamed@mail.com", "abc123")

compte.se_connecter("mauvais")      # tentative 1, échec
compte.se_connecter("mauvais")      # tentative 2, échec
compte.se_connecter("mauvais")      # tentative 3, échec -> verrouillé
compte.se_connecter("abc123")       # refusé, même bon mot de passe, car verrouillé

print()
compte.changer_email("pasunbonmail")     # refusé
compte.changer_email("mohamed@new.com")  # accepté

print()
compte.changer_mot_de_passe("mauvais", "nouveau123")  # refusé, ancien faux
compte.changer_mot_de_passe("abc123", "court")         # refusé, trop court
compte.changer_mot_de_passe("abc123", "nouveau123")    # accepté

print()
compte.afficher_infos()