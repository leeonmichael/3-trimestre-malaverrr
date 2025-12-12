// Crear instancia
const michael60 = new GestionTareas();

// Agregar tareas
misTareas.agregar("Estudiar JavaScript");
misTareas.agregar("Hacer ejercicio");
misTareas.agregar("Preparar presentaciÃ³n");

// Mostrar todas
misTareas.mostrar();

// Completar primera tarea
misTareas.completar(0);

// Mostrar actualizado
misTareas.mostrar();

// Mostrar estadÃ­sticas
const stats = misTareas.obtenerEstadisticas();
console.log("\n=== ESTADÃSTICAS michael DAVID MORENO NIETO ===");
console.log(`Total: ${stats.total}`);
console.log(`Completadas: ${stats.completadas}`);
console.log(`Pendientes: ${stats.pendientes}`);
//michael DAVID MORENO NIETO
