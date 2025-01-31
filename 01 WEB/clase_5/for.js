

console.log(1)
console.log(2)
console.log(3)
console.log(4)
console.log(5)
console.log("Iniciando for")
for(var indice = 1; indice < 6; indice++ ){
    console.log("hola")
    console.log(indice);
    console.log("chao")
}
console.log("fuera del for.")
console.log(indice);



var animales  = ["perro", "gato", "raton"]
//                  0       1       2

for (var indice=0; indice<animales.length; indice++){
    console.log(animales[indice])
}

for (var indice in animales){
    console.log(animales[indice])
}

for (var animal of animales){
    console.log(animal)
}