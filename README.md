# Exercices de programmation — Récapitulatif

Ce dépôt regroupe une série d'exercices réalisés dans le cadre de l'apprentissage de plusieurs langages de programmation (C, JavaScript, Python, Pascal), allant des bases (conditions, boucles, fonctions) jusqu'à la programmation orientée objet (héritage, encapsulation, classes abstraites, polymorphisme).

## Sommaire

- [Conversion de temps (multi-langages)](#conversion-de-temps-multi-langages)
- [Calcul de moyennes](#calcul-de-moyennes)
- [Classement des élèves](#classement-des-élèves)
- [Petits programmes JavaScript](#petits-programmes-javascript)
- [Petits programmes Python](#petits-programmes-python)
- [Programmation orientée objet (Python)](#programmation-orientée-objet-python)

---

## Conversion de temps (multi-langages)

Un même programme — convertir un temps donné en secondes en jours / heures / minutes / secondes, avec gestion correcte du singulier/pluriel — implémenté dans plusieurs langages pour comparer leur syntaxe :

| Fichier | Langage |
|---|---|
| `conversion_du_temps.c` | C |
| `conversion_du_temps.js` (+ page HTML associée) | JavaScript |
| `conversion_du_temps.pas` | Pascal |
| `conversion_du_temps.py` | Python |

**Concepts illustrés** : division entière / modulo, structures conditionnelles, gestion des accords pluriel/singulier.

---

## Calcul de moyennes

### `moyenne.py`
Module réutilisable contenant une fonction `moyenne(notes)` qui calcule la moyenne d'une liste de notes. Conçu pour être importé dans d'autres scripts.

### `calcul_moyenne.js` (+ page HTML associée)
Version JavaScript : demande 3 notes via `prompt()` et affiche leur moyenne dans la console.

**Concepts illustrés** : fonctions, boucles, séparation du code en modules (Python).

---

## Classement des élèves

Trois variantes d'un même programme : classer une liste d'élèves par moyenne décroissante et afficher le top 3.

| Fichier | Langage | Particularité |
|---|---|---|
| `classement_des_eleves_par_la_moyenne.js` (+ HTML) | JavaScript | Données codées en dur dans le script |
| `classement_python_json.py` | Python | Lit les élèves depuis `students.json`, importe `moyenne()` depuis `moyenne.py` |
| `classement_python_inline.py` | Python | Données et fonction `moyenne()` définies directement dans le script |

### `students.json`
Fichier de données contenant 20 élèves avec leurs notes, utilisé par la version Python "JSON".

**Concepts illustrés** : tri avec fonction de comparaison (`sort`/`sorted`), fonctions fléchées et `lambda`, lecture de fichiers JSON, tranches de liste (`[:3]`).

---

## Petits programmes JavaScript

| Fichier | Description |
|---|---|
| `nombre_premier.js` (+ HTML) | Vérifie si un nombre est premier par test de divisibilité |
| `palindrome.js` (+ HTML) | Vérifie si un mot est un palindrome en inversant la chaîne |

---

## Petits programmes Python

| Fichier | Description |
|---|---|
| `frais_livraison.py` | Calcule les frais de livraison (offerts au-delà de 50 £, sinon +4,90 £) |
| `celsius_fahrenheit.py` | Convertit une température de Celsius en Fahrenheit |
| `chiffre_affaires.py` | Calcule le chiffre d'affaires total à partir d'une liste de ventes |
| `appreciation_moyenne.py` | Donne une appréciation (Médiocre → Félicitations du jury) selon une moyenne sur 20 |
| `max_liste.py` | Trouve le plus grand nombre d'une liste (méthode manuelle + fonction `max()`), et illustre 3 façons d'inverser une liste |
| `interets_composes.py` | Calcule l'évolution d'un capital avec intérêts composés sur plusieurs années |
| `categories_age.py` | Classe des enfants par catégorie d'âge (poussin, pupille, minime, cadet) selon leur âge |

**Concepts illustrés** : conditions, boucles `for`/`while`, `input()`, formatage de chaînes (f-strings), fonctions natives (`max`, `reversed`).

---

## Programmation orientée objet (Python)

Une série d'exercices progressifs sur la POO : encapsulation, héritage, classes abstraites et polymorphisme.

| Fichier | Thème | Concepts clés |
|---|---|---|
| `formes_geometriques.py` | Classe abstraite `Forme` + `Rectangle`, `Cercle`, `Triangle` | Classe abstraite (`ABC`), calcul d'aire/périmètre, méthode commune héritée |
| `comptes_bancaires_heritage.py` | `CompteBancaire` + `CompteEpargne`, `CompteCourant` | Héritage, encapsulation (attributs privés), redéfinition de méthode (`super()`) |
| `compte_banque_simple.py` | `comptbanque` (dépôt/retrait) | Version simple sans héritage |
| `gestion_produit.py` | `Produit` (vente, stock, seuil d'alerte) | Encapsulation, validations, gestion d'état interne |
| `employes_heritage.py` | `Employe` + `Manager`, `Developpeur` | Héritage, polymorphisme (`calculer_salaire()` redéfinie) |
| `hopital_simple.py` | `hopital` | Classe basique avec état mutable |
| `compte_utilisateur.py` | `CompteUtilisateur` | Connexion, verrouillage après 3 échecs, changement d'email/mot de passe avec validation |
| `personnes_eleves_enseignants.py` | `Personne` (abstraite) + `Eleve`, `Enseignant` | Classe abstraite, gestion de notes/moyenne, gestion d'heures/paie, fonctions génériques sur listes mixtes |
| `bibliotheque.py` | `Document` (abstraite) + `Livre`, `DVD`, `Magazine` | Durée d'emprunt variable par type, redéfinition de comportement (édition spéciale non empruntable) |
| `location_vehicules.py` | `Vehicule` (abstraite) + `Voiture`, `Utilitaire`, `Moto` | Tarification conditionnelle, règles métier spécifiques par sous-classe, calcul de revenu total sur une flotte |

**Concepts illustrés** :
- Classes abstraites et méthodes abstraites (`ABC`, `@abstractmethod`)
- Encapsulation avec attributs privés (`__attribut`)
- Héritage simple et appel du parent (`super()`)
- Polymorphisme (redéfinition de méthodes selon la sous-classe)
- Validation de données et gestion des cas limites
- Manipulation de listes d'objets (affichage, calculs agrégés)

---

## Notes

Ces exercices couvrent une progression pédagogique classique : bases procédurales (variables, conditions, boucles, fonctions) → traitement de collections (listes, tri, fichiers JSON) → programmation orientée objet (encapsulation, héritage, abstraction, polymorphisme), avec des mises en application concrètes (gestion de comptes bancaires, de stock, de bibliothèque, de location de véhicules, de comptes utilisateurs).
