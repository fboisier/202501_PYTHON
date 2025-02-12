console.log("Hola mundo!")

if (5 > 10){
    console.log("5 es mayor a 10.");
} else {
    console.log("5 no es mayor a 10.");
}

// esto es un comentario.

var numero = 5;
var texto = "texto";
var boolTrue = true;
var boolFasle = false;

console.log("5" == 5);

var arreglos = ["gato", "perro", "cosas"];
console.log(arreglos);

var persona = {
    "nombre": "Francisco",
    "apellido": "Boisier"
}

console.log(persona);
console.log(persona["nombre"]);

let alAzar = 0;
let contador = 1;

while (alAzar !== 10) {
  contador++;
  alAzar = Math.floor(Math.random() * 20) + 1;
  console.log(alAzar);
}

console.log(`Tuvimos que ejecutar ${contador} veces el while para encontrar el 10.`);