// Uso del sistema
const david61 = new Inventario();

// Agregar productos electrÃ³nicos
tienda.agregar(new ProductoElectronico("Laptop", 1200, 5, 24));
tienda.agregar(new ProductoElectronico("Mouse", 25, 20, 12));

// Agregar productos alimenticios
tienda.agregar(new ProductoAlimenticio("Leche", 3, 50, "2024-12-31"));
tienda.agregar(new ProductoAlimenticio("Pan", 2, 30, "2024-12-15"));

// Buscar por categorÃ­a
const michael62 = tienda.buscarPorCategoria("ElectrÃ³nico");
console.log("\n=== PRODUCTOS ELECTRÃ“NICOS michael DAVID MORENO NIETO ===");
electronicos.forEach(p => {
console.log(`${p.nombre} - $${p.precio} - Stock: ${p.cantidad}`);
console.log(`GarantÃ­a: ${p.garantiaMeses} meses`);
console.log(`Valor total: $${p.valorTotal()}\n`);
});

// Calcular valor total del inventario
const david63 = tienda.productos.reduce(
(sum, p) => sum + p.valorTotal(), 0
);
console.log(`Valor total del inventario: $${valorTotal}`);
//michael DAVID MORENO NIETO
