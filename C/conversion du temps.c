#include <stdio.h>

int main() {
    long temps, jour, heure, minute, seconde, reste;

    printf("Entrer le temps (en secondes) : ");
    scanf("%ld", &temps);

    // Calcul des jours, heures, minutes et secondes
    jour = temps / 86400;
    reste = temps % 86400;

    heure = reste / 3600;
    reste = reste % 3600;

    minute = reste / 60;
    seconde = reste % 60;

    printf("Le temps saisi est le suivant : \n");

    // Affichage avec accord au pluriel
    if (jour > 0) {
        if (jour > 1)
            printf("%ld jours\n", jour);
        else
            printf("%ld jour\n", jour);
    }

    if (heure > 1)
        printf("%ld heures\n", heure);
    else
        printf("%ld heure\n", heure);

    if (minute > 1)
        printf("%ld minutes\n", minute);
    else
        printf("%ld minute\n", minute);

    if (seconde > 1)
        printf("%ld secondes\n", seconde);
    else
        printf("%ld seconde\n", seconde);

    return 0;
}