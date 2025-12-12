class LarrotaDireccion {
  constructor(larrotaCalle, larrotaCodigoPostal) {
    this.larrotaCalle = larrotaCalle;
    this.larrotaCodigoPostal = larrotaCodigoPostal;
  }
}

class LarrotaCliente {
  constructor(larrotaNombre, larrotaDireccion) {
    this.larrotaNombre = larrotaNombre;
    this.larrotaDireccion = larrotaDireccion;
  }

  mostrarLarrotaUbicacion() {
    console.log(`${this.larrotaNombre} vive en:
${this.larrotaDireccion.larrotaCalle},
CP ${this.larrotaDireccion.larrotaCodigoPostal}`);
  }
}

const michael_moreno1 = new LarrotaDireccion(
  "Calle de la Victoria 789", "11011"
);
const michael_moreno2 = new LarrotaCliente("Larrota GÃ³mez", michael_moreno1);
michael_moreno2.mostrarLarrotaUbicacion();
