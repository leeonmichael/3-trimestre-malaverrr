// VehiculoElectrico.js
class VehiculoElectrico extends Auto {
constructor(marca, modelo, autonomia) {
super(marca, modelo);
this.autonomiaBateria = autonomia;
}

mostrarInfo() {
return `${super.obtenerDescripcion()},
AutonomÃ­a: ${this.autonomiaBateria} km michael DAVID MORENO NIETO`;
}
}

const tesla = new VehiculoElectrico(
"Tesla", "Model 3", 500
);
console.log(tesla.mostrarInfo());
// "Marca: Tesla, Modelo: Model 3,
// AutonomÃ­a: 500 km michael DAVID MORENO NIETO"
//michael DAVID MORENO NIETO
