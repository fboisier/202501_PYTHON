
function nombre(){
    console.log("HOLA1");
    console.log("HOLA2");
    console.log("HOLA3");
    console.log("HOLA4");
}

nombre();

var copiaFuncion = nombre;
copiaFuncion()


function imprimirFOR (inicio, hasta=10, incremento=1){
    if (inicio < hasta){
        console.log("FLUJO NORMAL")

        for(var indice = inicio; indice <= hasta; indice+=incremento ){
            console.log(indice);
        }
    } else if (inicio > hasta) {
        console.log("FLUJO INVERTIDO")

        for(var indice = inicio; indice >= hasta; indice-=incremento ){
            console.log(indice);
        }
    }

    var salidaObjeto = {
        indice: indice,
        nombre: "Francisco"
    }

    return salidaObjeto
}

imprimirFOR(8, 20, 5)
imprimirFOR(20, 8, 6)
imprimirFOR(20, 8)
var resultado_indice = imprimirFOR(5)
console.log("EL INDICE TERMINO EN: ", resultado_indice.indice, resultado_indice.nombre)


function sumar(a, b){
    var resultado = a + b
    return resultado;
}

var resultado = sumar(5,10);
console.log(resultado)

console.log(sumar(80,20))


function fabricaZapatos(color, material, size){
    var zapato = `El zapato es de color ${color} de ${material} de tamño ${size}`;
    return zapato;
}

var zapato1 = fabricaZapatos("negro", "carton", "pequeño")
console.log(zapato1)

var nombre = "Francisco";
var nombre1 = 'Francisco';
var nombre2 = `Francisco`;

var boton = `<button>${nombre}</button>`
console.log(boton)


function mostrarNombre(nombre, edad){
    console.log(`Hola ${nombre} de edad ${edad}`)
}

var persona = {
    nombre: "Francisco",
    edad: 40,
    saludo: mostrarNombre
}

persona.saludo(persona.nombre, persona.edad)


var persona = {
    nombre: "Francisco",
    edad: 40,
    saludo: function(){
        console.log(`Hola ${this.nombre} de edad ${this.edad}`)
    }
}
persona.saludo();
persona.nombre  = "Javier";
persona.saludo();
