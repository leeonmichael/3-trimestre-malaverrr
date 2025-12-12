let nombre = "michael";

let num1 = parseFloat(prompt("Ingrese el primer nÃºmero:"));
let operador = prompt("Ingrese el operador (+, -, *, /):");
let num2 = parseFloat(prompt("Ingrese el segundo nÃºmero:"));
let resultado;

if (operador === '+') {
    resultado = num1 + num2;
} else if (operador === '-') {
    resultado = num1 - num2;
} else if (operador === '*') {
    resultado = num1 * num2;
} else if (operador === '/') {
    if (num2 !== 0) {
        resultado = num1 / num2;
    } else {
        resultado = "Error: DivisiÃ³n por cero";
    }
} else {
    resultado = "Operador invÃ¡lido";
}

alert("El resultado es: " + resultado);

