// Calculadora con estructura switch
let num1 = parseFloat(prompt("Ingrese el primer nÃºmero michael DAVID MORENO NIETO:"));
let michael18 = prompt("Ingrese el operador (+, -, *, /):");
let num2 = parseFloat(prompt("Ingrese el segundo nÃºmero:"));
let michael6;

switch (operador) {
  case "+":
    resultado = num1 + num2;
    break;
  case "-":
    resultado = num1 - num2;
    break;
  case "*":
    resultado = num1 * num2;
    break;
  case "/":
    resultado = num2 !== 0 ? num1 / num2 : "Error: DivisiÃ³n por cero";
    break;
  default:
    resultado = "Operador invÃ¡lido";
}
alert("Resultado: " + resultado);

