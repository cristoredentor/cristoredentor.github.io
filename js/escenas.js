/* escenas.js — escena inicial (SVG en línea, parallax, escala entera del personaje)
   y nivel final de Carrera (jugador, cofres, tarjetas de logro). */
(function () {
  "use strict";

  const Sitio = (window.Sitio = window.Sitio || {});
  const sinMovimiento = window.matchMedia("(prefers-reduced-motion: reduce)");
  document.documentElement.classList.add("js");

  /* ---------- SVG en línea: así las clases .arbol, .nube, .flama… se animan desde sitio.css ---------- */
  function cargaSvg(contenedor) {
    return fetch(contenedor.dataset.svg)
      .then((r) => (r.ok ? r.text() : Promise.reject(r.status)))
      .then((txt) => {
        contenedor.innerHTML = txt.replace(/<\?xml[^>]*\?>/, "").replace(/<title>[\s\S]*?<\/title>/, "");
        const svg = contenedor.querySelector("svg");
        if (svg) {
          svg.removeAttribute("width");
          svg.removeAttribute("height");
          svg.setAttribute("aria-hidden", "true");
          svg.setAttribute("focusable", "false");
        }
      })
      .catch(() => {
        // Respaldo: imagen estática (sin viento) si fetch falla, p. ej. abriendo el archivo sin servidor.
        contenedor.innerHTML = '<img alt="" src="' + contenedor.dataset.svg + '">';
      });
  }

  const pendientesInicio = [...document.querySelectorAll(".escena [data-svg]")];
  pendientesInicio.forEach(cargaSvg);

  let nivelCargado = false;
  Sitio.cargaNivel = function () {
    if (nivelCargado) return;
    nivelCargado = true;
    document.querySelectorAll(".nivel [data-svg]").forEach(cargaSvg);
  };

  /* ---------- Escalas enteras (pixel-art nítido) ---------- */
  const raiz = document.documentElement;
  const heroe = document.querySelector(".inicio__heroe");
  const nivel = document.querySelector(".nivel");

  function calculaEscalas() {
    if (heroe && heroe.offsetParent !== null) {
      const alto = heroe.clientHeight;
      const ancho = heroe.clientWidth;
      // el grupo mide 96×32 píxeles lógicos (mascotas a los lados del personaje)
      const esc = Math.max(3, Math.min(8, Math.floor(Math.min(alto / 34, ancho / 98))));
      raiz.style.setProperty("--esc", esc);
    }
    if (nivel && nivel.offsetParent !== null) {
      const en = nivel.clientWidth >= 1400 && window.innerHeight >= 800 ? 3 : 2;
      raiz.style.setProperty("--en", en);
    }
  }
  let rafEsc = 0;
  window.addEventListener("resize", () => {
    cancelAnimationFrame(rafEsc);
    rafEsc = requestAnimationFrame(calculaEscalas);
  });
  Sitio.calculaEscalas = calculaEscalas;

  /* ---------- Parallax suave con el mouse ---------- */
  const inicio = document.getElementById("pantalla-inicio");
  const lienzo = document.querySelector(".escena__lienzo");
  if (inicio && lienzo && window.matchMedia("(pointer: fine)").matches) {
    let rafPar = 0;
    inicio.addEventListener("pointermove", (e) => {
      if (sinMovimiento.matches) return;
      cancelAnimationFrame(rafPar);
      rafPar = requestAnimationFrame(() => {
        const x = (e.clientX / window.innerWidth) * 2 - 1;
        const y = (e.clientY / window.innerHeight) * 2 - 1;
        lienzo.style.setProperty("--px", (-x).toFixed(3));
        lienzo.style.setProperty("--py", (-y).toFixed(3));
      });
    });
    inicio.addEventListener("pointerleave", () => {
      lienzo.style.setProperty("--px", 0);
      lienzo.style.setProperty("--py", 0);
    });
  }

  /* ---------- Nivel final: jugador y cofres ---------- */
  if (nivel) {
    const cofres = [...nivel.querySelectorAll(".cofre")];
    const jugador = nivel.querySelector(".pj--jugador");
    const tarjetas = [...document.querySelectorAll(".logro")];
    const xDe = (i) => parseFloat(cofres[i].parentElement.style.getPropertyValue("--x"));
    let actual = -1;
    let posJugador = 4;
    let ignoraScrollHasta = 0;
    let finCaminata = 0;

    function caminaA(x) {
      const destino = Math.max(2, Math.min(330, x));
      if (destino === posJugador) return;
      jugador.classList.toggle("mira-izq", destino < posJugador);
      posJugador = destino;
      jugador.style.setProperty("--px", destino);
      if (!sinMovimiento.matches) {
        jugador.classList.add("camina");
        clearTimeout(finCaminata);
        finCaminata = setTimeout(() => jugador.classList.remove("camina"), 700);
      }
    }

    function centra(i) {
      const en = parseFloat(getComputedStyle(raiz).getPropertyValue("--en")) || 2;
      const objetivo = (xDe(i) + 16) * en - nivel.clientWidth / 2;
      ignoraScrollHasta = performance.now() + 800;
      nivel.scrollTo({ left: Math.max(0, objetivo), behavior: sinMovimiento.matches ? "auto" : "smooth" });
    }

    function abre(i, opciones = {}) {
      if (i < 0 || i >= cofres.length) return;
      actual = i;
      cofres.forEach((c, k) => c.setAttribute("aria-expanded", String(k === i)));
      tarjetas.forEach((t, k) => t.classList.toggle("visible", k === i));
      caminaA(xDe(i) - 24);
      if (opciones.centrar !== false) centra(i);
    }
    Sitio.abreLogro = abre;

    cofres.forEach((c, i) => {
      c.addEventListener("click", () => abre(i));
      c.addEventListener("focus", () => { caminaA(xDe(i) - 24); centra(i); });
      c.addEventListener("keydown", (e) => {
        if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
          e.preventDefault();
          const j = Math.max(0, Math.min(cofres.length - 1, i + (e.key === "ArrowRight" ? 1 : -1)));
          cofres[j].focus();
          abre(j);
        }
      });
    });

    // Avanzar con scroll: el jugador sigue el centro de la vista y abre el cofre al llegar.
    nivel.addEventListener("scroll", () => {
      if (performance.now() < ignoraScrollHasta) return;
      const en = parseFloat(getComputedStyle(raiz).getPropertyValue("--en")) || 2;
      const centro = (nivel.scrollLeft + nivel.clientWidth / 2) / en;
      let cercano = 0;
      cofres.forEach((_, k) => { if (Math.abs(xDe(k) + 16 - centro) < Math.abs(xDe(cercano) + 16 - centro)) cercano = k; });
      caminaA(centro - 16);
      if (Math.abs(xDe(cercano) + 16 - centro) < 28 && cercano !== actual) abre(cercano, { centrar: false });
    }, { passive: true });

    abre(0, { centrar: false });
  }
})();
