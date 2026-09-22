/*tableau contenant des données des élèves*/
const students=[
    {
        name:'John',
        notes:[1,20,18,19,12]
    },
    {
        name:'Jane',
        notes:[17,18,20,13,15]
    },
    {
        name:'Sophie',
        notes:[17,12,14,15,13]
    },
    {
        name:'Marc',
        notes:[2,3,5,8,9]
    },
    {
        name:'Manon',
        notes:[18,17,18,19,12]
    }
]
//fonction contenant le calcul des moyennes, fonction reuitilisable
const moyenne= (notes) =>{
    let sum = 0
    for (let note of notes){
        sum= sum + note
    }
    return sum / notes.length
}
//Ajout de la clée moyenne dans le tableau contenant l'objet(élève)
for ( let student of students){
    student.moyenne = moyenne(student.notes)
}
//Fonction servant a trier dans l'ordre voulue
const compareStudents= (a,b)=>{
    return b.moyenne - a.moyenne  //Ordre décroissant a cause de b - a
}
//Utilisation d'une methode sort() appliquée sur le tableau
students.sort(compareStudents)
console.log(students) //Permet d'afficher le tableau
console.log('les top 3 sont: ')
const nombre_classement= 3  //Cette varriable est pour le Top du classement
//Utilisation de la boucle for() pour parcourire les éléments du tableau
for (let student=0; student< nombre_classement ;student++){
    console.log(`${student+1} : ${students[student].name} avec une moyenne de ${students[student].moyenne}`)
}