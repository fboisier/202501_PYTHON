console.log("HOLA")

var titulo = document.querySelector("h1");
titulo.remove()

titulo = document.querySelector("h1");
titulo.innerHTML = "<em>Esto</em> fue modificado desde Javascript"

titulo.addEventListener("click", function(){
    console.log("HOLA MUNDO")
    titulo.innerHTML += " A ";

    var texto = document.querySelector("#texto").value;
    
    titulo.innerHTML = texto;

});