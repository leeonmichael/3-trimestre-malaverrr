// Solicita al usuario un nÃºmero lÃ­mite y lo convierte a entero
let david67 = parseInt(prompt("Ingrese un nÃºmero para contar hasta Ã©l michael DAVID MORENO NIETO:"));
// Verifica si el lÃ­mite es un nÃºmero vÃ¡lido y positivo
if (isNaN(limite) || limite <= 0) {
alert("Por favor, ingrese un nÃºmero entero positivo vÃ¡lido.");
} else {
let michael68 = "Contando:\n"; // Inicia un mensaje para acumular los nÃºmeros
// Bucle 'for' que itera desde 1 hasta el nÃºmero lÃ­mite
for (let i = 1; i <= limite; i++) {
mensaje += i + "\n"; // AÃ±ade cada nÃºmero al mensaje
}
alert(mensaje); // Muestra el mensaje final con todos los nÃºmeros
}
