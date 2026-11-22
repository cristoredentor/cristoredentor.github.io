# Change: add-final-level-game

## Why
Cada sección del camino termina en un **nivel final**: la prueba de que el usuario aprendió el
tema. Un examen plano no retiene; un juego 2D de aventura pixel-art donde **cada monstruo es una
pregunta bajo presión de tiempo** sí, siempre que:
- la evaluación sea válida (preguntas distintas en cada partida, tiempo justo, servidor como
  autoridad — ver `add-question-bank`);
- el juego no se coma el presupuesto: es un *wrapper* temático de un examen, no un sandbox
  completo con minería y construcción.

UOLINGO V2.5 ya proponía el "jefe final" como examen de 3–40 preguntas con tiempo por dificultad,
una barra de vida igual a los puntos que faltan para la calificación mínima elegida (60–100 %), y
que abandonar solo pierde el progreso temporal del combate. Este change lo concreta como juego,
elige motor y define cómo se integra con el resto de la app.

## What Changes
- **Biomas por tema**: un bioma original por tema inicial (Regex, GitHub, Docker, APIs, Agentes),
  con paleta, tiles, monstruos y jefe propios (`content-design.md`, `design/mockups/03-final-level/`).
- **Estructura del nivel**: recorrido lateral lineal por el bioma con encuentros; monstruos
  comunes (1 pregunta), raros (2 preguntas) y jefe final (resto de preguntas, dificultad creciente).
- **Combate por preguntas**: acierto = el jugador ataca y el monstruo pierde vida; fallo o
  *timeout* = el jugador pierde margen de error; temporizador visible, autoritativo en servidor.
- **Reglas de examen**: el usuario elige N ∈ [3, 40] y calificación mínima g ∈ [60 %, 100 %];
  la vida total del recorrido = aciertos requeridos `ceil(g·N)`; el margen de error = `N − ceil(g·N)`.
  Abandonar descarta solo el progreso de esa partida.
- **Tipos de reto** jugables en el combate: opción múltiple, V/F, completar regex (validada con
  casos de prueba en servidor), ordenar comandos (Parsons), completar comando, emparejar,
  detectar error, predecir salida.
- **Motor**: Phaser 3 (versión fijada) embebido como módulo cargado bajo demanda, con la UI de
  preguntas como capa DOM accesible por encima del canvas (ver `design.md`).
- **Sprites base implementables**: jugador (idle/walk/attack), 4 monstruos comunes (idle/hurt),
  4 tiles (`design/mockups/03-final-level/sprites/`).

## Impact
- Specs afectadas: `final-level` (nueva).
- Depende de: `add-question-bank` (selección, tiempo, corrección), `add-platform-architecture`
  (frontend TS, backend, almacenamiento de assets), `add-engagement-system` (vidas de sección,
  cofres y evolución como recompensa).
- Frontend: nueva ruta de nivel final con *chunk* de motor cargado bajo demanda (~1 MB min.).
- Arte: 5 biomas × (tiles + fondo parallax + 3–4 monstruos + jefe) es el mayor coste del
  change; se propone lanzar con 2 biomas completos (Regex, Docker) y el resto con monstruos comunes.
