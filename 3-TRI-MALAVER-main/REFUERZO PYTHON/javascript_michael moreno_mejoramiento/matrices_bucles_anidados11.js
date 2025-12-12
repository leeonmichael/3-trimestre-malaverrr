let michael_moreno2 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

function imprimirLarrota(cuervo) {
  for (let michael_moreno2 = 0; michael_moreno2 < cuervo.length; michael_moreno2++) {
    for (let cuervoIndex = 0; cuervoIndex < cuervo[michael_moreno2].length; cuervoIndex++) {
      console.log(`[${michael_moreno2}][${cuervoIndex}] = ${cuervo[michael_moreno2][cuervoIndex]}`);
    }
  }
}

imprimirLarrota(michael_moreno2);
