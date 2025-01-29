var animales = ["perro", "gato", "tigre", "pajaro", "leon"];
//                  0       1       2        3        4
console.log(animales)
console.log(animales[1])
console.log(animales.length)
animales.push("raton")


var cosas = [1, false, "texto", 100, animales];
//           0    1       2       3     4 
console.log(cosas)
console.log(cosas.length)

cosas[4] = 'otro texto'
console.log(cosas)


console.log("IMPRIMIENDO TODOS LOS ANIMALES")
for(var indice = 0; indice < animales.length; indice++){
    console.log("VIENDO EL ANIMAL " + animales[indice])
}
animales.pop();
console.log("🚀 ~ animales:", animales)

console.log(animales.splice(2, 2))
console.log("🚀 ~ animales:", animales)

console.log(animales.shift())
console.log("🚀 ~ animales:", animales)


var arregloSimple = ["UNO", "DOS"]
//                      0      1

console.log(arregloSimple.reverse())

var temporal = arregloSimple[0]
arregloSimple[0] = arregloSimple[1]
arregloSimple[1] = temporal

console.log(arregloSimple)
console.log(["DOS", "UNO"])
