var nombre = "Francisco";
var apellido ="Boisier"
var edad  = 39

var persona = {
    nombre: "Francisco",
    apellido: "Boisier",
    edad: 39,
}

var persona2 = {
    nombre: "Javier",
    apellido: "Sandoval",
    edad: 28,
}

console.log(persona)

console.log(persona.edad)
persona.edad = 40

console.log(persona)

persona.pasatiempos = ["musica", "programación", "videojuegos", "anime"]

console.log(persona)
console.log(persona2)

var personas = [persona, persona2] 
//                  0       1

console.log(personas)
console.log(personas[1].edad)
