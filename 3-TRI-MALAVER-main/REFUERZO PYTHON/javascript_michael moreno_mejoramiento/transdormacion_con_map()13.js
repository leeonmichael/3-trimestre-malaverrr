let michael_moreno1 = [100, 250, 399, 75];

let michael_moreno2 = michael_moreno1.map(michael_moreno1 => michael_moreno1 * 1.10);

console.log("Originales:", michael_moreno1);
console.log("Con 10% aumento:", michael_moreno2);

//map() - Crear un nuevo arrayAplicar una funciÃ³n a cada elemento de un array y devolver un nuevo array con los resultados.
//Diferencia con filter() filter(): Selecciona elementos (puede haber menos) map(): Transforma todos los elementos (misma cantidad)
