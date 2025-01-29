console.log("HOLA 1");

console.log("HOLA 2");

console.log("HOLA 3");

console.log("HOLA 4");

console.log("HOLA 5");

var edad = 50;
var apellidos= "Santos";
var meGustaJS= true; //false --- esto no se ejecuta

console.log(edad)

edad = "un texto cualquiera"
console.log(edad)

console.log(apellidos)

var total = 13 - 7

console.log(total - 1)
console.log(total + 1)
console.log(total * 5)
console.log(total)

console.log(total = total * 5)
console.log(total)

var nombre = "Francisco";

console.log("HOLA " + nombre)

var contador = 9;

console.log(contador)

contador = contador + 1;
console.log(contador)

contador += 1;
console.log(contador)

contador -= 2;
console.log(contador)

contador++;
console.log(contador)

console.log(contador > 10);
console.log(contador > 1);

if (contador > 10){
    console.log("RESETEANDO A 1")
    contador = 1;
} else if (contador < 10){
    console.log("AUMENTANDO 5")
    contador += 5;
} else {
    console.log("NO SE CAMBIO NADA PORQUE ES 10")
}
console.log(contador)




var esDia = true

var hora = 14

if (esDia && hora < 12){
    console.log("Que día más excelente en la mañana.")
} else {
    console.log("que mal")
}

if (esDia || hora < 10){
    console.log("Es de dia. o son menos las 10.")
}else{
    console.log("que mal. no cumple.")
}

var numero = 4;

var resto = numero % 2;
console.log(resto != 0)

if (resto != 0){
    console.log("El numero " + numero + " es impar");
}else{
    console.log("El numero " + numero + " es par");
}

if (numero % 2 != 0){
    console.log("El numero " + numero + " es impar");
}else{
    console.log("El numero " + numero + " es par");
}

var numeroA = 5
var numeroB = "5"

console.log(numeroA == numeroB)
console.log(numeroA === numeroB)
console.log(numeroA !== numeroB)