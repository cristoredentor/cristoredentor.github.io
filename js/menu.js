/* menu.js — menú de videojuego (teclado + ratón + táctil), carrusel de proyectos y vista ampliada. */
(function () {
  "use strict";

  const Sitio = (window.Sitio = window.Sitio || {});

  /* =================== Menú principal =================== */
  const menu = document.querySelector(".menu");
  const botones = menu ? [...menu.querySelectorAll(".menu__boton")] : [];
  const botonSub = menu ? menu.querySelector("[aria-controls='submenu-quien-soy']") : null;
  const submenu = document.getElementById("submenu-quien-soy");
  const opcionesSub = submenu ? [...submenu.querySelectorAll("a")] : [];
  let activo = 0;

  function marca(i) {
    activo = (i + botones.length) % botones.length;
    botones.forEach((b, k) => b.classList.toggle("es-activo", k === activo));
  }
  function enfoca(i) { marca(i); botones[activo].focus(); }

  function abreSub(enfocar = true) {
    if (!submenu) return;
    submenu.hidden = false;
    botonSub.setAttribute("aria-expanded", "true");
    if (enfocar) opcionesSub[0].focus();
  }
  function cierraSub(devolverFoco = true) {
    if (!submenu || submenu.hidden) return false;
    submenu.hidden = true;
    botonSub.setAttribute("aria-expanded", "false");
    if (devolverFoco) botonSub.focus();
    return true;
  }
  Sitio.cierraSubmenu = cierraSub;

  if (menu) {
    marca(0);
    botones.forEach((b, i) => {
      b.addEventListener("mouseenter", () => marca(i));
      b.addEventListener("focus", () => marca(i));
      b.addEventListener("keydown", (e) => {
        const sig = e.key === "ArrowDown" || e.key === "ArrowRight";
        const ant = e.key === "ArrowUp" || e.key === "ArrowLeft";
        if (b === botonSub && (e.key === "ArrowRight" || e.key === "ArrowDown") && !submenu.hidden) {
          e.preventDefault(); opcionesSub[0].focus(); return;
        }
        if (sig || ant) { e.preventDefault(); cierraSub(false); enfoca(i + (sig ? 1 : -1)); }
      });
    });

    botonSub.addEventListener("click", () => (submenu.hidden ? abreSub(true) : cierraSub(true)));

    opcionesSub.forEach((o, i) => {
      o.addEventListener("keydown", (e) => {
        if (e.key === "ArrowDown") { e.preventDefault(); opcionesSub[(i + 1) % opcionesSub.length].focus(); }
        else if (e.key === "ArrowUp") { e.preventDefault(); opcionesSub[(i - 1 + opcionesSub.length) % opcionesSub.length].focus(); }
        else if (e.key === "ArrowLeft" || e.key === "Escape") { e.preventDefault(); e.stopPropagation(); cierraSub(true); }
      });
      o.addEventListener("click", () => cierraSub(false));
    });

    document.addEventListener("click", (e) => {
      if (submenu && !submenu.hidden && !e.target.closest(".menu__item--sub")) cierraSub(false);
    });
  }

  Sitio.enfocaMenu = function (seccion) {
    if (!menu) return;
    const i = botones.findIndex((b) => (b.getAttribute("href") || "").startsWith("#" + seccion) ||
      (seccion === "quien-soy" && b === botonSub));
    enfoca(i < 0 ? 0 : i);
  };

  /* =================== Carrusel de proyectos =================== */
  const carrusel = document.querySelector(".carrusel");
  if (carrusel) {
    const pista = carrusel.querySelector(".carrusel__pista");
    const vista = carrusel.querySelector(".carrusel__vista");
    const diapos = [...carrusel.querySelectorAll(".proyecto")];
    const pos = carrusel.querySelector("[data-pos]");
    carrusel.querySelector("[data-total]").textContent = diapos.length;
    let indice = 0;

    function muestra(i, actualizaHash) {
      indice = (i + diapos.length) % diapos.length;
      pista.style.transform = "translateX(" + -100 * indice + "%)";
      diapos.forEach((d, k) => {
        const fuera = k !== indice;
        d.toggleAttribute("inert", fuera);
        d.setAttribute("aria-hidden", String(fuera));
      });
      pos.textContent = indice + 1;
      if (actualizaHash) history.replaceState(null, "", "#proyectos/" + diapos[indice].dataset.proyecto);
    }
    Sitio.muestraProyecto = function (id) {
      const i = diapos.findIndex((d) => d.dataset.proyecto === id);
      muestra(i < 0 ? 0 : i, false);
    };
    Sitio.pasaProyecto = (d) => muestra(indice + d, true);

    carrusel.querySelectorAll("[data-dir]").forEach((b) =>
      b.addEventListener("click", () => muestra(indice + Number(b.dataset.dir), true)));

    // Deslizar en móvil
    let x0 = null;
    vista.addEventListener("pointerdown", (e) => { x0 = e.clientX; });
    vista.addEventListener("pointerup", (e) => {
      if (x0 === null) return;
      const dx = e.clientX - x0;
      x0 = null;
      if (Math.abs(dx) > 50) muestra(indice + (dx < 0 ? 1 : -1), true);
    });
    vista.addEventListener("pointercancel", () => { x0 = null; });
    muestra(0, false);
  }

  /* =================== Vista ampliada (fotos y diplomas) =================== */
  const dialogo = document.querySelector(".lightbox");
  if (dialogo) {
    const img = dialogo.querySelector(".lightbox__img");
    const titulo = dialogo.querySelector(".lightbox__titulo");
    const pie = dialogo.querySelector(".lightbox__pie");
    const pdf = dialogo.querySelector("[data-pdf-enlace]");
    let grupo = [];
    let i = 0;
    let origen = null;

    function pinta() {
      const b = grupo[i];
      const mini = b.querySelector("img");
      img.src = mini.dataset.full || mini.src;
      img.alt = mini.alt;
      titulo.textContent = b.dataset.titulo || mini.alt;
      pie.textContent = b.dataset.emisor ? b.dataset.emisor : mini.alt;
      if (b.dataset.pdf) { pdf.hidden = false; pdf.href = b.dataset.pdf; } else { pdf.hidden = true; pdf.removeAttribute("href"); }
      dialogo.querySelectorAll("[data-paso]").forEach((f) => (f.hidden = grupo.length < 2));
    }
    function abre(boton) {
      grupo = [...document.querySelectorAll('[data-lightbox="' + boton.dataset.lightbox + '"]')];
      i = grupo.indexOf(boton);
      origen = document.activeElement;
      pinta();
      dialogo.showModal();
      dialogo.querySelector("[data-cerrar]").focus();
    }
    document.querySelectorAll("[data-lightbox]").forEach((b) => b.addEventListener("click", () => abre(b)));
    document.querySelectorAll("[data-abre-diploma]").forEach((b) => b.addEventListener("click", () => {
      const d = document.getElementById("diploma-" + b.dataset.abreDiploma);
      if (d) abre(d);
    }));
    dialogo.querySelectorAll("[data-paso]").forEach((f) =>
      f.addEventListener("click", () => { i = (i + Number(f.dataset.paso) + grupo.length) % grupo.length; pinta(); }));
    dialogo.querySelector("[data-cerrar]").addEventListener("click", () => dialogo.close());
    dialogo.addEventListener("click", (e) => { if (e.target === dialogo) dialogo.close(); });
    dialogo.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
        if (grupo.length < 2) return;
        e.preventDefault();
        i = (i + (e.key === "ArrowRight" ? 1 : -1) + grupo.length) % grupo.length;
        pinta();
      }
    });
    dialogo.addEventListener("close", () => { if (origen && origen.focus) origen.focus(); });
    Sitio.dialogoAbierto = () => dialogo.open;
  }

  /* =================== Teclado global =================== */
  document.addEventListener("keydown", (e) => {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    if (Sitio.dialogoAbierto && Sitio.dialogoAbierto()) return;
    const ruta = Sitio.rutaActual ? Sitio.rutaActual() : "inicio";
    const flechas = ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"];

    if (e.key === "Escape") {
      if (cierraSub(true)) return;
      if (ruta !== "inicio") { e.preventDefault(); location.hash = "#inicio"; }
      return;
    }
    // En el inicio, una flecha lleva el foco al menú aunque esté en otra parte.
    if (ruta === "inicio" && flechas.includes(e.key) && !e.target.closest(".menu")) {
      e.preventDefault(); enfoca(activo); return;
    }
    // En proyectos, ← → cambian de proyecto.
    if (ruta === "proyectos" && (e.key === "ArrowLeft" || e.key === "ArrowRight") && Sitio.pasaProyecto) {
      e.preventDefault(); Sitio.pasaProyecto(e.key === "ArrowRight" ? 1 : -1);
    }
  });

})();
