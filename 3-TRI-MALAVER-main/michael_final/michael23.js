let a18 = parseInt(prompt("Primer nÃºmero:"));
let b18 = parseInt(prompt("Segundo nÃºmero:"));
let mcm = (a18 * b18) / ((function mcd(x, y){ return y ? mcd(y, x % y) : x })(a18, b18));
alert("El MCM es michael DAVID MORENO NIETO: " + mcm);

