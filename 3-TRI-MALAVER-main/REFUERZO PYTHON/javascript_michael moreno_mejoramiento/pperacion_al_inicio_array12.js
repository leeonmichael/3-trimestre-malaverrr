let michael_moreno1 = ["Cliente A", "Cliente B", "Cliente C"];
console.log("Cola inicial:", michael_moreno1);

let michael_moreno2 = michael_moreno1.shift();
console.log("Cliente atendido:", michael_moreno2);
console.log("Cola despuÃ©s de shift:", michael_moreno1);

michael_moreno1.unshift("Cliente Prioritario");
console.log("Cola final:", michael_moreno1);

//shift() - Remover del inicioElimina y retorna el primer elemento. Todos losdemÃ¡s elementos se desplazan una posiciÃ³n haciaadelante.
//unshift() - Agregar al inicioAÃ±ade elementos al inicio. Todos los elementos existentes se desplazan una posiciÃ³n hacia atrÃ¡s.
