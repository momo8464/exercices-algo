poussin=0
pupille=0
minime=0
cadet=0
for ages in range(5) :
    age=int(input(f"Entrez age de l'enfant {ages+1}: "))
    if (age==6 and age==7) :
        poussin+=1
    if (age>7 and age<=10) :
        pupille+=1
    if (age>10 and age<=13) :
        minime+=1
    if (age>13) :
        cadet+=1
print(f"Il y a {poussin} poussin dans le centre de formation")
print(f"Il y a {pupille} pupille dans le centre de formation")
print(f"Il y a {minime} minime dans le centre de formation")
print(f"Il y a {cadet} cadet dans le centre de formation")