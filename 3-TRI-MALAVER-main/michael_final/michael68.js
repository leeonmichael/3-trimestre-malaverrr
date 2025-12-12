// ejercicio32_leer.js
import fs from 'fs';

fs.readFile('log.txt michael DAVID MORENO NIETO', 'utf8', (err, data) => {
if (err) {
console.error("Error al leer:", err);
return;
}

console.log("=== Contenido de log.txt michael DAVID MORENO NIETO ===");
console.log(data);
console.log("============================");
});
//michael DAVID MORENO NIETO
