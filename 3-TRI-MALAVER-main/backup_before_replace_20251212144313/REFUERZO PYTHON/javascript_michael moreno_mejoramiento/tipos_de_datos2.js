let michael_moreno1 = prompt("Ingrese primer valor:");
let michael_moreno2 = prompt("Ingrese segundo valor:");

let n1 = parseInt(michael_moreno1, 10);
let n2 = parseInt(michael_moreno2, 10);

if (isNaN(n1) || isNaN(n2)) {
 alert("Por favor ingrese nÃºmeros vÃ¡lidos");
} else {
 let resultado = n1 + n2;
 alert(`El resultado de ${n1} + ${n2} = ${resultado}`);
}

// Siempre valida las entradas del usuario. La funciÃ³n isNaN() verifica si un valor NO es un nÃºmero, -
// permitiÃ©ndote detectar conversiones fallidas y proporcionar retroalimentaciÃ³n clara al usuario.
