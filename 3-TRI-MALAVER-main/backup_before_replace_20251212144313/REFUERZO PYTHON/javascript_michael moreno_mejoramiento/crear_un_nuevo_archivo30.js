import fs from 'fs';

const michael_moreno1 = new Date().toISOString();
const michael_moreno2 = `Larrota log creado a las: ${michael_moreno1}\n`;

fs.writeFile('larrota_log.txt', michael_moreno2, (larrotaError) => {
  if (larrotaError) {
    console.error("Error Larrota:", larrotaError);
    return;
  }
  console.log("Archivo Larrota creado exitosamente (CREATE)");
});
