/* router.js — navegación por hash.
   Rutas: #inicio · #quien-soy/resumen · #quien-soy/fotos · #proyectos/pixtart · #proyectos/agnis · #carrera */
(function () {
  "use strict";

  const Sitio = (window.Sitio = window.Sitio || {});
  const NOMBRE = "Cristopher Góngora";
  const RUTAS = {
    inicio: { titulo: NOMBRE, subs: [] },
    "quien-soy": { titulo: "¿Quién soy?", subs: ["resumen", "fotos"] },
    proyectos: { titulo: "Proyectos", subs: ["pixtart", "agnis"] },
    carrera: { titulo: "Carrera", subs: [] },
  };
  const NOMBRES_SUB = { resumen: "Resumen", fotos: "Fotos", pixtart: "Pixtart", agnis: "Agnis" };

  const pantallas = [...document.querySelectorAll("[data-pantalla]")];
  const barra = document.querySelector(".barra");
  const sinMovimiento = window.matchMedia("(prefers-reduced-motion: reduce)");
  let actual = null;
  let primera = true;

  Sitio.rutaActual = () => actual;

  function lee() {
    const [seccion, sub] = location.hash.replace(/^#\/?/, "").split("/");
    if (!seccion) return { seccion: "inicio" };
    if (RUTAS[seccion]) {
      const subs = RUTAS[seccion].subs;
      return { seccion, sub: subs.includes(sub) ? sub : subs[0] };
    }
    // Un ancla a un elemento de la página (p. ej. el enlace "Saltar al contenido") no es una ruta.
    if (document.getElementById(seccion)) return null;
    return { seccion: "inicio" };
  }

  function navega() {
    const ruta = lee();
    if (!ruta) return;
    const anterior = actual;
    const cambia = ruta.seccion !== anterior;
    actual = ruta.seccion;

    pantallas.forEach((p) => (p.hidden = p.dataset.pantalla !== actual));
    barra.hidden = actual === "inicio";
    if (Sitio.cierraSubmenu) Sitio.cierraSubmenu(false);

    document.querySelectorAll("[data-seccion]").forEach((a) => {
      if (a.dataset.seccion === actual) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
    document.querySelectorAll("[data-sub]").forEach((a) => {
      if (a.dataset.sub === ruta.sub) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });

    const r = RUTAS[actual];
    document.title = actual === "inicio" ? NOMBRE
      : r.titulo + (ruta.sub ? " · " + NOMBRES_SUB[ruta.sub] : "") + " — " + NOMBRE;

    if (Sitio.calculaEscalas) requestAnimationFrame(Sitio.calculaEscalas);

    if (actual === "proyectos" && Sitio.muestraProyecto) Sitio.muestraProyecto(ruta.sub);
    if (actual === "carrera" && Sitio.cargaNivel) Sitio.cargaNivel();

    if (cambia) window.scrollTo(0, 0);

    // Foco: al entrar a una pantalla se anuncia su título; al volver al inicio, el menú.
    if (primera) { primera = false; return; }
    if (actual === "inicio") {
      if (anterior && Sitio.enfocaMenu) Sitio.enfocaMenu(anterior);
      return;
    }
    if (actual === "quien-soy") {
      const destino = document.getElementById(ruta.sub);
      destino.focus({ preventScroll: true });
      if (!cambia || ruta.sub === "resumen") {
        destino.scrollIntoView({ behavior: sinMovimiento.matches ? "auto" : "smooth", block: "center" });
      }
      destino.classList.remove("enfocado");
      void destino.offsetWidth;
      destino.classList.add("enfocado");
      return;
    }
    if (cambia) {
      const h = document.querySelector("#pantalla-" + actual + " .titulo-pantalla");
      if (h) h.focus({ preventScroll: true });
    }
  }

  window.addEventListener("hashchange", navega);
  navega();
})();
