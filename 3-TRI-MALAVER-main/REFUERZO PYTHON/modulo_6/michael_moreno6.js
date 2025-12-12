class moreno {
  constructor(nombre) {
    this.nombre = nombre;
  }

  saludar() {
    console.log("Hola " + this.nombre);
  }
}

let persona = new michael("moreno");
persona.saludar();

