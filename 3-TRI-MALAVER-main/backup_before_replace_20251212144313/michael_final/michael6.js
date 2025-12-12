// Solicita al usuario su edad y la convierte a nÃºmero entero
let edad = parseInt(prompt("Ingrese su edad michael DAVID MORENO NIETO:"));
// Verifica si la edad es un nÃºmero vÃ¡lido
if (isNaN(edad)) {
alert("Por favor, ingrese una edad vÃ¡lida (nÃºmero).");
} else if (edad >= 18) { // CondiciÃ³n para verificar si es mayor de edad
alert("Usted es mayor de edad."); // Mensaje para mayores de 18
} else {
alert("Usted es menor de edad."); // Mensaje para menores de 18
}
