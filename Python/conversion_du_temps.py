temps=int(input("Entrez le temps en secondes: "))
jour= temps // 86400
reste= temps % 86400
heure= reste // 3600
reste= reste % 3600
minute= reste // 60
seconde= reste % 60

print("Le temps servir est le suivant: ")
if jour>0 :
    if jour>1 :
        print(f"{jour} jours")
    else :
        print(f"{jour} jour")

if heure>1 :
    print(f"{heure} heures")
else :
    print(f"{heure} heure")

if minute>1 :
    print(f"{minute} minutes")
else :
    print(f"{minute} minute")

if seconde>1 :
    print(f"{seconde} secondes")
else :
    print(f"{seconde} seconde")