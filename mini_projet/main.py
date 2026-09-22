import json
import os
from moyenne import moyenne

# Récupère le dossier où se trouve ce script, peu importe d'où il est lancé
dossier_script = os.path.dirname(os.path.abspath(__file__))
chemin_json = os.path.join(dossier_script, "students.json")

# Lecture du fichier JSON contenant les étudiants
with open(chemin_json, "r", encoding="utf-8") as f:
    students = json.load(f)

# Ajout de la clé "moyenne" dans chaque dictionnaire étudiant
for student in students:
    student["moyenne"] = moyenne(student["notes"])

# Tri par ordre décroissant selon la moyenne
top_etudiants = sorted(students, key=lambda student: student["moyenne"], reverse=True)

# Affichage du top 3 des apprenants
print("Top 3 des étudiants :")
for i,student in enumerate(top_etudiants[:3], start=1):
    print(f"{i} : {student['name']} avec {student['moyenne']} de moyenne")