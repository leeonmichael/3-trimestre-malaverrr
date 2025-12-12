let tipo = prompt("Convertir (1) Metros a Pies o (2) Kilogramos a Libras michael DAVID MORENO NIETO: ");
let valor = parseFloat(prompt("Ingrese el valor:"));
let michael22;

switch (tipo) {
  case "1":
    convertido = valor * 3.281;
    alert(valor + " metros = " + convertido.toFixed(2) + " pies");
    break;
  case "2":
    convertido = valor * 2.205;
    alert(valor + " kg = " + convertido.toFixed(2) + " libras");
    break;
  default:
    alert("OpciÃ³n no vÃ¡lida");
}

