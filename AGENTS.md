# AGENTS.md — GitHub Pages de Cristopher Góngora (estilo Pixtart)

## Proyecto
Sitio personal y portafolio para **reclutadores**, presentado como el menú de un videojuego
pixel-art inspirado en **Pixtart** (el juego de aprendizaje del autor). Debe verse cuidado y
profesional: el estilo de videojuego es el envoltorio, el contenido (quién soy, proyectos,
carrera, diplomas) es lo importante.

El kit de arranque (arte, textos, tokens e instrucciones) vive en la raíz del repositorio
`cristoredentor.github.io`, junto al sitio ya construido (`index.html`, `css/`, `js/`, `404.html`).

## Comandos
- Servir en local: `python3 -m http.server 8000` y abrir `http://localhost:8000`
- Regenerar el arte nuevo (personaje, fondos, UI): `python3 herramientas/generar_arte.py`
- Ver prototipos: `assets/fondos/inicio/preview.html` (escena inicial animada) y
  `assets/personajes/cristopher/preview.html` (saludo)
- Publicar: GitHub Pages desde la rama `main`, carpeta raíz. **Sin paso de build.**

## Mapa de esta carpeta
| Ruta | Qué es |
|---|---|
| `contenido/textos.md` | **Fuente única de todos los textos** (exactos), títulos de fotos y lista de diplomas |
| `diseno/tokens.css` | Paleta azul-gris, fuente única, escalas de texto y espaciado |
| `assets/MANIFIESTO.md` | Inventario de cada asset: qué es, dónde se usa, tamaño lógico |
| `assets/personajes/cristopher/` | Personaje principal NUEVO (rubio, traje formal, saludando) |
| `assets/mascotas/` | Mascotas de Pixtart como sprites limpios (zorro, búho, golem) |
| `assets/fondos/` | Fondos por pantalla (inicio en 7 capas, museo, aula Pixtart, nivel final) |
| `assets/ui/` | Botones dorados, flechas, cursor, placa de museo, marco de cuadro, íconos |
| `assets/fotos/` | 5 fotos del autor para "¿Quién soy? → Fotos" |
| `assets/diplomas/` | 16 diplomas en JPG (`img/`) y PDF para descarga (`pdf/`) |
| `assets/personajes/juego*/`, `assets/nivel-final/`, `assets/tiles/` | Arte original de Pixtart reutilizable |
| `assets/referencia/` | Guía de estilo y docs de Pixtart, muestra de color del prompt |
| `herramientas/generar_arte.py` | Genera el arte nuevo (Python estándar, determinista) |
| `index.html`, `css/`, `js/`, `404.html` | El sitio publicado (ver estructura abajo) |

## Estructura del sitio (implementada)
```
/
├── index.html            # una sola página; cada pantalla es una <section>
├── css/
│   ├── tokens.css        # copia de diseno/tokens.css
│   └── sitio.css
├── js/
│   ├── router.js         # navegación por hash
│   ├── menu.js           # menú de videojuego (teclado + ratón + táctil)
│   └── escenas.js        # animaciones (viento, mascotas, saludo)
├── assets/               # esta carpeta assets/ tal cual
└── 404.html              # "Game over" con botón dorado para volver al inicio
```
Rutas (hash): `#inicio` · `#quien-soy/resumen` · `#quien-soy/fotos` · `#proyectos/pixtart` ·
`#proyectos/agnis` · `#carrera`. HTML, CSS y JS sin frameworks ni bundler.

---

## Reglas globales (todo subagente las cumple)
1. **Una sola fuente**: `Pixelify Sans` (ver `diseno/tokens.css`) en títulos, botones y párrafos.
   No se usa `Press Start 2P` (la del juego) porque cansa en párrafos largos.
2. **Legibilidad**: cuerpo ≥ 18 px, interlineado 1.6, párrafos ≤ 70 caracteres de ancho, contraste
   WCAG AA (≥ 4.5:1). Nada de texto encima del fondo animado sin una placa o panel detrás.
3. **Colores**: solo los de `diseno/tokens.css`. Base azul-grisácea; el dorado es el único acento.
   Sprites del juego muy saturados (mascotas, alumnos) se muestran con `filter: saturate(.7)` o
   menos para no cansar la vista.
4. **Pixel-art nítido**: `image-rendering: pixelated`, escalas enteras (×2, ×3, ×4…), nunca
   tamaños que emborronen.
5. **Tono profesional**: sin chistes ni jerga; los textos salen de `contenido/textos.md`, no se
   inventan. Texto marcado 🔒 no se reescribe; texto ✏️ necesita aprobación del autor.
6. **Accesibilidad**: todo el menú funciona con teclado (↑ ↓ ← → Enter Esc), con foco visible
   (cursor dorado ▶); `alt` en cada imagen; `prefers-reduced-motion` apaga las animaciones;
   HTML semántico (`nav`, `main`, `section`, `h1…h3`).
7. **Rendimiento**: fotos y diplomas con `loading="lazy"`; la pantalla inicial carga < 1 MB.
8. **Responsive**: funciona desde 360 px de ancho; en móvil el menú se apila y la escena se recorta
   centrada en el personaje.
9. **Privacidad**: no se publica la clave única ni datos de contacto que el autor no haya dado.
   La imagen de la Beca Baillères ya viene censurada; no subir su PDF original.
10. **Arte original**: no copiar assets ni nombres de otros juegos (regla heredada de Pixtart).

## Especificación por pantalla

### 0. Pantalla inicial (`#inicio`)
- Escena 16:9 a pantalla completa: las 7 capas de `assets/fondos/inicio/` apiladas en orden
  (cielo y sol → nubes → montañas → colinas → árboles de fondo → pasto y árboles cercanos →
  viento y hojas). Ver el prototipo `preview.html`.
- **Viento**: los árboles (`.arbol`) y matas (`.mata`) se mecen con `skewX` desde su base; las
  ráfagas (`.rafaga`) y hojas (`.hoja`) cruzan de derecha a izquierda; nubes (`.nube`) derivan lento.
  Parallax suave opcional con el mouse (capas lejanas se mueven menos).
- **Personaje principal grande y centrado** (`cristopher-hoja.svg`, alternando los frames de
  saludo). Es la versión "nivel máximo" del jugador.
- **Mascotas** (`assets/mascotas/*.svg`) caminando/saltando detrás o a los lados del personaje.
- **Menú** abajo: botones dorados (`boton-dorado-*.svg` o el 9-slice) con ícono a la izquierda:
  `¿Quién soy?` (con submenú `Resumen` / `Fotos`), `Proyectos`, `Carrera`. Estados normal, hover,
  presionado; el cursor `▶` marca la opción activa.

### 1. ¿Quién soy? (`#quien-soy/...`)
- Fondo: `assets/fondos/museo/museo-sala.svg` (sala de museo pixel-art).
- **Fotos**: las 5 de `assets/fotos/` en marcos dorados (`marco-cuadro-9slice.svg`) colgados en la
  pared, cada una con su mini-cédula. Clic → vista ampliada (lightbox accesible, Esc cierra).
- **Resumen**: el texto 🔒 en una **cédula de museo** (`placa-museo-9slice.svg`): fondo crema,
  texto oscuro, nombre como título — como la ficha que acompaña a un cuadro.
- "Resumen" y "Fotos" son la misma sala: Resumen enfoca la cédula, Fotos enfoca la galería.

### 2. Proyectos (`#proyectos/...`)
- Carrusel de proyectos con **flechas doradas** ← → (`flecha-dorada-*.svg`); también con teclado
  ← → y swipe en móvil. Indicador de posición (1/2, 2/2).
- **Pixtart**: encabezado `assets/fondos/pixtart-aula/pixtart-aula-escena.svg` (maestro búho y
  alumnos en clase) y debajo la explicación de `contenido/textos.md`.
- **Agnis**: el autor es cofundador; texto de `contenido/textos.md`. Encabezado: por definir con el
  autor (puede ser un panel de control pixel-art con candados/escudos en la misma paleta).

### 3. Carrera (`#carrera`)
- Presentada como **el nivel final de Pixtart**: `assets/fondos/nivel-final/nivel-final-carrera.svg`
  (noche, castillo meta, plataformas y el mismo suelo de piedra azul-gris de la muestra).
- El personaje (o el sprite `nivel-final/sprites/player-*`) avanza con scroll o flechas; cada logro
  es un cofre (`ui/chest-*.svg`) que al abrirse muestra la tarjeta del logro.
- Arriba, "ficha del jugador": carreras, semestre, lenguajes y herramientas.
- Al final, galería de **todos** los diplomas (`assets/diplomas/img/`), cada uno abre en grande y
  enlaza a su PDF cuando exista.

---

## Subagentes

El trabajo se divide en subagentes. **El autor definirá las funciones exactas de cada uno más
adelante**; hasta entonces, la columna "Función" queda pendiente y la "Propuesta inicial" sirve
solo como punto de partida. Cuando el autor dé las funciones, se reemplaza la tabla y la sección
de contratos.

| # | Subagente | Función (la define el autor) | Propuesta inicial (provisional) | Aprobada por autor después de leerlo.
|---|---|---|---|
| 1 | `orquestador` |_lsito_ | Lee este archivo, reparte tareas, integra y corre la verificación final. |
| 2 | `maquetador` | _listo_ | `index.html`, estructura semántica, router por hash, layout responsive. |
| 3 | `estilos-ui` | _listo_ | `sitio.css`: menú dorado, placa de museo, marcos, carrusel, estados de foco. |
| 4 | `animacion` | _listo_ | Escena inicial (viento, parallax, mascotas, saludo) y nivel final; respeta reduced-motion. |
| 5 | `contenido` | _listo_ | Pasa `contenido/textos.md` al HTML sin alterar 🔒; marca ✏️ para revisión. |
| 6 | `assets` | _listo_ | Optimiza imágenes, recorta márgenes de diplomas edX, genera arte faltante con `herramientas/`. |
| 7 | `ayudante` | _listo_ | Busca ejemplos inspirados de paisajes para primer fondo, busca estándares de simetria y belleza para aplicarlos a todas las pestañas y comprueba que se cumplan`. |
| 8 | `qa` | _listo_ | Accesibilidad, contraste, teclado, móvil, enlaces rotos, peso de página. |

### Contratos entre subagentes (provisionales)
- Cada subagente solo escribe en sus archivos; lo que necesite de otro lo pide al orquestador.
- `contenido/textos.md` y `diseno/tokens.css` son de solo lectura salvo para el orquestador.
- Arte nuevo se agrega con `herramientas/generar_arte.py` (no SVG editados a mano que luego se
  pierdan al regenerar) y se anota en `assets/MANIFIESTO.md`.

## Definición de terminado
- [ ] Las 6 rutas cargan y se navega entre ellas solo con teclado.
- [ ] Todos los textos coinciden con `contenido/textos.md`; ningún ✏️ sin aprobar.
- [ ] Una sola familia tipográfica en todo el sitio (revisar en DevTools → Fonts).
- [ ] Contraste AA en todos los textos; nada de texto sobre fondo animado sin panel.
- [ ] Los 16 diplomas y las 5 fotos aparecen, con `alt`.
- [ ] Con `prefers-reduced-motion` no hay animaciones.
- [ ] Se ve bien en 360 px, 768 px y 1440 px.
- [ ] Lighthouse: Accesibilidad ≥ 95, Rendimiento ≥ 90.
- [ ] Antes de terminar, reportar qué se verificó y qué no.
