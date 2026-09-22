const temps=prompt('entrez le temps en seconde: ')*1
const jour=(temps/86400)
let rest =(temps % 86400)
const heure=(rest/3600)
let reste =(rest % 3600)
const minute=(reste/60)
const seconde=(reste % 60)
console.log('le temps saisie est le suivant: ')
if (jour>0){
    if (jour>1){
        console.log(Math.floor(jour),' jours')
    }else{
        console.log(Math.floor(jour),' jour')
    }
}
if (heure > 1){
    console.log(Math.floor(heure),' heures')
}else{
    console.log(Math.floor(heure),' heure')
}
if (minute > 1){
    console.log(Math.floor(minute),' minutes')
}else{
    console.log(Math.floor(minute),' minute')
}
if (seconde > 1){
    console.log(Math.floor(seconde),' secondes')
}else{
    console.log(Math.floor(seconde),' seconde')
}