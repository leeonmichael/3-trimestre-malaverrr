// ejercicio08.js
let michael_moreno1 = ["El Quijote", "100 AÃ±os de Soledad", "Fahrenheit 451"];
console.log("Libros iniciales:", michael_moreno1.length); // 3
// Agregar al final
michael_moreno1.push("Moby Dick");
console.log("DespuÃ©s de push:", michael_moreno1.length); // 4
console.log("Libros:", michael_moreno1);
// Remover del final
let michael_moreno2 = michael_moreno1.pop();
console.log("Libro removido:", michael_moreno2); // "Moby Dick"
console.log("Libros finales:", michael_moreno1.length); // 3
