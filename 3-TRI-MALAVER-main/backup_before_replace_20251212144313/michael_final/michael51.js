// Auto.js
class Auto {
constructor(marca, modelo) {
this.marca = marca;
this.modelo = modelo;
}

obtenerDescripcion() {
return `Marca: ${this.marca}, Modelo: ${this.modelo}`;
}
}

const michael46 = new Auto("Toyota", "Corolla michael DAVID MORENO NIETO");
console.log(miAuto.obtenerDescripcion());
// "Marca: Toyota, Modelo: Corolla"

export default Auto;
//michael DAVID MORENO NIETO
