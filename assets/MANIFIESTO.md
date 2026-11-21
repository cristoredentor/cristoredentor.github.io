# Manifiesto de assets

Tamaño lógico = rejilla de píxeles del SVG (escálese siempre por enteros).
**Nuevo** = generado para esta página con `herramientas/generar_arte.py`.
**Pixtart** = copiado del proyecto del juego (`privado/Picstart/design/mockups/`).

## Personaje principal — `personajes/cristopher/` (Nuevo)
| Archivo | Tamaño | Uso |
|---|---|---|
| `cristopher-idle.svg` | 32×32 | Pose quieta |
| `cristopher-saludo-f1.svg`, `-f2.svg` | 32×32 | Frames del saludo |
| `cristopher-hoja.svg` | 96×32 | Hoja de 3 frames (idle, saludo f1, f2) para `background-position` + `steps()` |
| `preview.html` | — | Ejemplo de la animación |

Rubio, chamarra negra abierta con playera clara, jeans azules y tenis blancos,
piel en tono cálido apagado, sonriente.

## Mascotas — `mascotas/`
| Archivo | Tamaño | Origen |
|---|---|---|
| `ember-fox.svg` | 16×16 | Sprite limpio (Nuevo) extraído de la tarjeta Pixtart |
| `crystal-owl.svg` | 12×13 | Ídem |
| `mini-golem.svg` | 16×16 | Ídem |
| `tarjetas/pet-*.svg`, `tarjetas/support-characters.svg` | 220×268 | Tarjetas originales Pixtart |

## Fondos — `fondos/` (Nuevo)
| Archivo | Tamaño | Pantalla | Clases animables |
|---|---|---|---|
| `inicio/capa-1-cielo-sol.svg` | 320×180 | Inicio | — |
| `inicio/capa-2-nubes.svg` | 320×180 | Inicio | `.nube` |
| `inicio/capa-3-montanas.svg` | 320×180 | Inicio | — |
| `inicio/capa-4-colinas.svg` | 320×180 | Inicio | — |
| `inicio/capa-5-arboles-fondo.svg` | 320×180 | Inicio | `.arbol` (`transform-origin` en la base, `--i` para desfase) |
| `inicio/capa-6-pasto-arboles-frente.svg` | 320×180 | Inicio | `.arbol`, `.mata` |
| `inicio/capa-7-viento-hojas.svg` | 320×180 | Inicio | `.rafaga`, `.hoja` |
| `inicio/preview.html` | — | Prototipo de la escena completa animada | |
| `museo/museo-sala.svg` | 320×180 | ¿Quién soy? | — |
| `pixtart-aula/pixtart-aula-escena.svg` | 320×140 | Proyectos → Pixtart (encabezado) | — |
| `nivel-final/nivel-final-carrera.svg` | 480×180 | Carrera | `.flama` (antorchas) |
| `agnis/agnis-panel.svg` | 320×140 | Proyectos → Agnis (encabezado: panel de agentes, escudo, reporte) | — |

## UI — `ui/` (Nuevo salvo cofres)
| Archivo | Tamaño | Uso |
|---|---|---|
| `boton-dorado-normal/hover/presionado.svg` | 96×24 | Botón de menú en sus 3 estados |
| `boton-dorado-9slice.svg` | 24×24 | `border-image: url(...) 8 fill / 24px; image-rendering: pixelated` |
| `placa-museo-9slice.svg` | 24×24 | Cédula de museo (slice 8) |
| `marco-cuadro-9slice.svg` | 24×24 | Marco dorado de fotos/diplomas (slice 8) |
| `flecha-dorada-derecha.svg`, `-izquierda.svg` | 16×16 | Carrusel de proyectos |
| `cursor-menu.svg` | 6×7 | Indicador ▶ de opción activa |
| `iconos/icono-quien-soy.svg`, `icono-proyectos.svg`, `icono-carrera.svg` | 16×16 | Íconos de los botones del menú |
| `chest-normal.svg`, `chest-legendary.svg` | 32×32 | Cofres originales de Pixtart (no se editan) |
| `chest-normal-hoja.svg`, `chest-legendary-hoja.svg` | 128×32 | Hoja de 4 frames para la animación de apertura (cerrado, entreabierto, medio, abierto) (Nuevo, `cofres_partidos()`) |

## Fotos — `fotos/`
`miniaturas/`: copias de 640 px máx. para la galería; el original se abre en la vista ampliada.
`foto-1-alpaca.jpg`, `foto-2-estadio.jpg`, `foto-3-machu-picchu.jpg`,
`foto-4-montana-de-colores.jpg`, `foto-5-laguna.jpg` (extraídas del PDF del prompt, máx. 1280 px).

## Diplomas — `diplomas/`
- `img/*.jpg` (16, máx. 1400 px). El PDF de ITAM traía 4 diplomas juntos: se separaron en
  `itam-beca-bailleres`, `itam-alto-rendimiento-ciencia-de-datos`, `itam-dataton` e
  `itam-alto-rendimiento-computacion` (rotados a horizontal). El de EPIC Lab es el bootcamp.
- `miniaturas/*.jpg` (16, 560 px máx.) para la rejilla de Carrera.
- Los 4 de edX (`harvardx-cs50x`, `upv-excel-*`) ya están recortados al marco del certificado (sin URL ni pie del navegador).
- `pdf/*.pdf` (15): originales para descarga. Falta a propósito el de la beca (trae la clave única).

## Arte del juego reutilizable (Pixtart)
| Carpeta | Contenido |
|---|---|
| `personajes/juego/` | 29 personajes 32×32 en paleta base (ogro, búho bibliotecaria, mago, etc.) |
| `personajes/juego-aurora/` | Los mismos en la paleta Aurora |
| `personajes/ogro-evolucion/` | Evolución del ogro en 6 tiers y atuendos (Brote, Aventurero, Leyenda) |
| `nivel-final/` | Biomas, hoja de monstruos, pantalla de reto y `sprites/` (jugador idle/walk/attack, monstruos, tiles) |
| `tiles/base/`, `tiles/aurora/`, `tiles/gris/` | Tiles 16×16 (pasto, tierra, piedra, madera) |

## Referencia — `referencia/`
- `muestra-color-azul-gris.png`: la muestra del prompt. Es idéntica a `tiles/aurora/tile-stone--aurora.svg`.
- `style-guide.md`, `palettes.json`: guía visual y paletas de Pixtart.
- `roster-extended.svg`: elenco completo de personajes.
- `pixtart-docs/`: `project.md`, propuesta y diseño de contenido del nivel final, README de Pixtart
  (base para el texto del proyecto Pixtart).
