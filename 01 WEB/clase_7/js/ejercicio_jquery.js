
var btnFooter = document.querySelector(".btnFooter");
var opcion = document.querySelector("#opcion");
var numeros = document.querySelectorAll("span.numero");
var titulosNumeros = document.querySelectorAll("span.grado_titulo");

$(".btnFooter").click(function(){
    $("footer").remove()
})

$("#opcion").on("change", function(){
    cambiarTodo($(this).val());
})


function cambiarTodo(tipo){
    numeros.forEach(function(numero){
        var texto = numero.innerText;
        var numeroTexto = parseInt(texto);
        var convertido = convertirTemperatura(numeroTexto, tipo)
        numero.innerText = Math.round(convertido);
    });
    titulosNumeros.forEach(function(titulo){
        if (tipo == "F"){
            titulo.innerText = "F°";
        } else{
            titulo.innerText = "C°";
        } 
    });
}

function convertirTemperatura(valor, tipo) {
    if (tipo === "F") {
        return (valor * 9/5) + 32; // Celsius a Fahrenheit
    } else {
        return (valor - 32) * 5/9; // Fahrenheit a Celsius
    }
}


// var menus = document.querySelectorAll("ul#menu li a")
// var tituloCiudad = document.querySelector("main>h2");
// for(var menu of menus ){
//     menu.addEventListener("click", function(){
//         tituloCiudad.innerText = this.innerText
//     })
// }

$("ul#menu li a").click(function(){
    $("main>h2").html($(this).html())
    $("article").fadeIn(1000);
})

$("article").click(function(){
    $(this).fadeOut(2000);
})

$("main>h2").click(function(){
    $("img").siblings("h2").remove();
    $("img").before(`<h2>${$(this).html()}</h2>`)
});

function saludar(nombre){
    return `Hola ${nombre}`;
}

const saludar = function(nombre){
    return `Hola ${nombre}`;
}

const saludar = (nombre) => {
    return `Hola ${nombre}`;
}

const saludar = nombre => `Hola ${nombre}`;


console.log(saludar("Francisco"));