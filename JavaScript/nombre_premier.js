let a= prompt('entrez a: ')*1
if ((a!==2) && (a!==3)){
    if ((a % 2===0) || (a % 3===0) || (a % 5===0) || (a % 9===0) || (a % 10===0)){
        console.log('le nombre n\'est pas un nombre premier')
    }else{
        console.log('le nombre est un nombre premier')
    }
}else{
    console.log('le nombre est un nombre premier')
}