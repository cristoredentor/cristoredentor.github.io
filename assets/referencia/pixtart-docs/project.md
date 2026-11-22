# Project Context — Picstart

> Estado: **fase de propuestas** (OpenSpec). No hay código de aplicación todavía. Todo lo que
> vive en `openspec/changes/` es una propuesta pendiente de aprobación.

## Propósito
Picstart es una app de aprendizaje gamificada: un **camino de lecciones** (mecánica tipo
"learning path" de apps de idiomas) combinado con un **mundo pixel-art 2D de aventura**
(biomas, monstruos, cofres, equipo). El objetivo de producto es retención: que estudiar se
sienta como jugar y que la constancia diaria tenga consecuencias visibles (vidas, evolución).

Temas iniciales (del boceto): Regex, GitHub, Docker, APIs, Agentes; y matemáticas
(esperanza, distribuciones, demostraciones) como ejemplo de calentamiento.

## Restricción de identidad visual (IP)
Nos **inspiramos** en mecánicas de género (camino de lecciones, rachas, cofres, pixel-art
sandbox), pero **no** copiamos assets, logos, personajes, mascotas, nombres ni paletas
exactas de Duolingo, Terraria u otros productos. Todo arte es original (ver
`design/style-guide.md`). Esto también evita problemas legales si el proyecto escala.

## Secciones principales (navegación)
Pedido original: Home (camino), Arena multijugador, Usuario/Perfil, Tienda, Compartir niveles,
Configuración. Propuesta vigente (`changes/add-core-navigation`): 5 destinos **Inicio · Arena ·
Taller · Tienda · Perfil**; "Compartir niveles" se re-encuadra como **Taller** y **Ajustes** sale
de la barra (engrane en el header). Pendiente de aprobación; ver `open-questions.md`.

Índice de changes y orden de implementación: `openspec/README.md`. Decisiones abiertas:
`openspec/open-questions.md`.

## Glosario
| Término | Definición |
|---|---|
| Sección / Unidad | Conjunto de niveles de un tema. Tiene su propio contador de **vidas** (10 por defecto). |
| Nivel | Lección del camino: serie de ejercicios con tiempo. |
| Calentamiento | Ejercicios fáciles al inicio de una sección para motivar/recordar fundamentos. |
| Nivel final / Jefe | Juego tipo aventura 2D donde cada monstruo es una pregunta bajo presión de tiempo. |
| Evolución | Nivel del personaje; sube con aciertos/constancia, baja al perder todas las vidas. Determina atuendos y fondos. |
| Rareza | común / raro / legendario. |
| Cofre normal / legendario | Recompensa en el camino; el legendario aparece tras 4 normales. |
| Personaje de apoyo | Criatura desbloqueada que aparece al usar una poción/ayuda. |
| Arena | Duelo multijugador por tema: gana quien responde primero/correcto/más cerca. |
| BYOK | "Bring your own key": el usuario conecta su propia API key de IA. |

## Convenciones OpenSpec
- `openspec/project.md`: este archivo.
- `openspec/specs/<capability>/spec.md`: verdad actual (vacío hasta que se apruebe/archive algo).
- `openspec/changes/<change-id>/`: `proposal.md` (por qué/qué), `design.md` (decisiones
  técnicas y alternativas), `tasks.md` (checklist), `specs/<capability>/spec.md` (deltas con
  `## ADDED Requirements`, `### Requirement:`, `#### Scenario:` en formato WHEN/THEN).
- IDs de change en kebab-case con verbo: `add-…`, `update-…`.
- Mockups y sprites en `design/mockups/<area>/` (SVG pixel-art, `shape-rendering="crispEdges"`).

## Stack (propuesto, ver `openspec/changes/add-platform-architecture/design.md`)
Pendiente de aprobación. Todo corre en Docker para replicabilidad.
