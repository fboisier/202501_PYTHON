
var btnFooter = document.querySelector(".btnFooter");
var footer = document.querySelector("footer");
var opcion = document.querySelector("#opcion");
var numeros = document.querySelectorAll("span.numero");
var titulosNumeros = document.querySelectorAll("span.grado_titulo");

btnFooter.addEventListener("click", function(){
    footer.remove();
})

opcion.addEventListener("change", function(){
    console.log(this.value);
    cambiarTodo(this.value);
});

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
