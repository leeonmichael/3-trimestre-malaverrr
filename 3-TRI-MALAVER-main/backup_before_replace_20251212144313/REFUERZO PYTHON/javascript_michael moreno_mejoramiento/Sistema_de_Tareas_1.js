let michael_moreno1 = [];

function agregarTarea(lista, tarea) {
  const michael_moreno2 = [...lista, tarea];
  console.log(`Tarea agregada: "${tarea}"`);
  return michael_moreno2;
}

function completarTarea(lista, indice) {
  if (indice >= 0 && indice < lista.length) {
    const michael_moreno2 = lista.map((t, i) =>
      i === indice ? "7 " + t : t
    );
    console.log("Tarea marcada como completada");
    return michael_moreno2;
  } else {
    console.log("Ãndice invÃ¡lido");
    return lista;
  }
}


function obtenerEstadisticas(lista) {
  const total = lista.length;
  const completadas = lista.filter(t => t.startsWith("7")).length;
  const pendientes = total - completadas;
  return { total, completadas, pendientes };
}


function mostrarTareas(lista) {
  console.log("\n=== LISTA DE TAREAS ===");
  lista.forEach((tarea, i) => {
    console.log(`${i}. ${tarea}`);
  });
}


michael_moreno1 = agregarTarea(michael_moreno1, "Estudiar JavaScript");
michael_moreno1 = agregarTarea(michael_moreno1, "Hacer ejercicio");
michael_moreno1 = agregarTarea(michael_moreno1, "Preparar presentaciÃ³n");

mostrarTareas(michael_moreno1);

michael_moreno1 = completarTarea(michael_moreno1, 0);

mostrarTareas(michael_moreno1);

const stats = obtenerEstadisticas(michael_moreno1);
console.log("\n=== ESTADÃSTICAS ===");
console.log(`Total: ${stats.total}`);
console.log(`Completadas: ${stats.completadas}`);
console.log(`Pendientes: ${stats.pendientes}`);
