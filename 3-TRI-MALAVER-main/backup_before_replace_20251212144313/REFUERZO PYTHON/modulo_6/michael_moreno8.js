try {
  throw new Error("Algo salió mal, moreno");
} catch (e) {
  console.log("Error capturado:", e.message);
}
