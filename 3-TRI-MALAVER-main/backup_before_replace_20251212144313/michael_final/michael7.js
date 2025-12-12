// Solicita el valor de la temperatura y lo convierte a flotante
let michael54 = parseFloat(prompt("Ingrese la temperatura michael DAVID MORENO NIETO:"));
// Solicita el tipo de conversiÃ³n deseada
let david55 = prompt("Â¿Desea convertir a Fahrenheit (F) o Celsius (C)?").toUpperCase();
let michael56; // Declara la variable para el resultado
// Verifica si la temperatura es un nÃºmero vÃ¡lido
if (isNaN(temperatura)) {
alert("Por favor, ingrese una temperatura vÃ¡lida.");
} else {
// CondiciÃ³n para convertir a Fahrenheit
if (tipoConversion === 'F') {
resultadoConversion = (temperatura * 9/5) + 32; // FÃ³rmula C a F
alert(temperatura + "Â°C es " + resultadoConversion.toFixed(2) + "Â°F.");
}
// CondiciÃ³n para convertir a Celsius
else if (tipoConversion === 'C') {
resultadoConversion = (temperatura - 32) * 5/9; // FÃ³rmula F a C
alert(temperatura + "Â°F es " + resultadoConversion.toFixed(2) + "Â°C.");
}
// Mensaje para tipo de conversiÃ³n invÃ¡lido
else {
alert("Tipo de conversiÃ³n invÃ¡lido. Por favor, ingrese 'F' o 'C'.");
}
}
