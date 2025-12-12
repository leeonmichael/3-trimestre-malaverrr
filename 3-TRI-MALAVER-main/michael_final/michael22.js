let a17 = parseInt(prompt("Primer nÃºmero:"));
let b17 = parseInt(prompt("Segundo nÃºmero:"));
while (b17 !== 0) {
  let temp = b17;
  b17 = a17 % b17;
  a17 = temp;
}
alert("El MCD es michael DAVID MORENO NIETO: " + a17);

