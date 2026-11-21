# Picstart — Guía de estilo visual (compartida por todos los mockups)

Arte **original** pixel-art 2D de aventura/fantasía. Inspiración de género, sin copiar assets,
logos, personajes ni mascotas de otros juegos/apps.

## Formato técnico de las imágenes
- SVG hecho a mano con `<rect>` en una rejilla de píxeles; `shape-rendering="crispEdges"`.
- Sprites: rejilla lógica de **16×16** (items, iconos) o **32×32** (personajes), escalada ×4–×8.
- Mockups de pantalla: lienzo de **390×844** (móvil) salvo que se diga otra cosa; el contenido
  pixel-art dentro usa la misma paleta.
- Texto en SVG: `font-family="'Press Start 2P', monospace"` con fallback monospace.
- Cada SVG debe abrir solo en un navegador (sin dependencias externas salvo la fuente opcional).
- Animaciones: frames sueltos `*-f1.svg … *-fN.svg` **y** un `*.html` que los anime con CSS.

## Paleta base (hex)
| Rol | Colores |
|---|---|
| Cielo día | `#5FA8E8` `#8CC8F0` |
| Cielo noche / UI fondo oscuro | `#1B1F3B` `#2B2F55` |
| Pasto / bosque | `#3E8E41` `#6BBF59` `#2C5E2E` |
| Tierra / madera | `#8B5A2B` `#A86F3C` `#5C3A1A` |
| Piedra | `#7A7A86` `#A3A3AE` `#4A4A55` |
| Marco de UI (madera+metal) | relleno `#6B4423`, borde `#2A1A0E`, brillo `#C08A4A` |
| Texto UI | `#FFF6D8` sobre oscuro, `#2A1A0E` sobre claro |
| Acierto / error | `#58C94A` / `#E04848` |
| Monedas | `#F2C230` `#C8941A` `#FFF1A0` |
| Vidas (corazón) | `#E04848` `#FF8A8A` `#8E1F1F` |

## Rareza (borde + brillo del slot)
| Rareza | Borde | Brillo |
|---|---|---|
| Común | `#B8B8B8` | ninguno |
| Raro | `#3F7FE0` | `#8FB8FF` |
| Legendario | `#F2A81D` | `#FFE27A` + destellos |

## Personaje por defecto: Ogro verde
32×32. Piel `#6BBF59` sombra `#3E8E41`, ojos blancos con pupila `#1B1F3B`, colmillos
`#FFF6D8`, taparrabo/chaleco `#8B5A2B`, contorno `#1E3A1F`. Expresión amistosa (es tutor,
no villano). Es el "anfitrión" que hace las preguntas en los niveles y el apoyo común inicial.

## Elenco (contexto 6)
- Común: ogro verde (default), demonio pequeño, esqueleto pequeño, zombie.
- Raro: mago, demonio grande, esqueleto grande, fantasma.
- Legendario: caballero negro.

## Convención de archivos
`design/mockups/<NN-area>/<nombre>.svg`, p. ej. `design/mockups/01-home/home-path.svg`.
Áreas: `00-navigation`, `01-home`, `02-profile`, `03-final-level`, `04-items`, `05-arena`,
`06-characters`.
