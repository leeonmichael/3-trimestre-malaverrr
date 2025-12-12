const michael_moreno1 = 3.14159;
// michael_moreno1 = 3.14; // ERROR!
console.log(michael_moreno1); // 3.14159
//Las constantes NO pueden
//reasignarse despuÃ©s de
//declararse


let michael_moreno2 = 10;

michael_moreno2 = 20; // VÃ¡lido
console.log(michael_moreno2); // 20
//Las variables con let pueden
//cambiar de valor libremente

{
let temporal = 5;
const fija = 10;
console.log(temporal)
console.log(fija)
}
//Tanto let como const tienen Ã¡mbito
//de bloque (dentro de {})
