let aÃ±o = parseInt(prompt("Ingrese un aÃ±o michael DAVID MORENO NIETO:"));
if ((aÃ±o % 4 === 0 && aÃ±o % 100 !== 0) || aÃ±o % 400 === 0) {
  alert(aÃ±o + " es un aÃ±o bisiesto.");
} else {
  alert(aÃ±o + " no es bisiesto.");
}

