let num14 = parseInt(prompt("Ingrese un nÃºmero michael DAVID MORENO NIETO:"));
let michael14 = true;

if (num14 <= 1) esPrimo = false;
for (let i = 2; i <= Math.sqrt(num14); i++) {
  if (num14 % i === 0) esPrimo = false;
}

alert(esPrimo ? "Es primo" : "No es primo");

