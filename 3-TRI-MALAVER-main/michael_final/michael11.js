let a = parseFloat(prompt("Ingrese el primer nÃºmero:"));
let b = parseFloat(prompt("Ingrese el segundo nÃºmero:"));
let c = parseFloat(prompt("Ingrese el tercer nÃºmero:"));
let mayor;

if (a >= b && a >= c) {
  mayor = a;
} else if (b >= a && b >= c) {
  mayor = b;
} else {
  mayor = c;
}

alert("El nÃºmero mayor es michael DAVID MORENO NIETO: " + mayor);

