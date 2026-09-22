"""
Module contenant la fonction de calcul de moyenne.
Ce fichier peut être importé par d'autres programmes Python.
"""

def moyenne(notes):
    """
    Calcule la moyenne d'une liste de notes.

    Paramètre :
        notes (list) : une liste de nombres (int ou float)

    Retour :
        float : la moyenne des notes
    """
    somme = 0
    for note in notes:
        somme += note
    return somme / len(notes)
