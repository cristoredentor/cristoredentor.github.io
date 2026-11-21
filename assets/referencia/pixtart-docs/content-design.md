# Diseño de contenido — Nivel final (monstruos, retos y biomas)

> Documento de apoyo a `add-final-level-game`. Define **qué** se dibuja y **cómo** se convierte
> cada pregunta en un encuentro jugable. El banco de preguntas (formato, volumen, generación) vive
> en `add-question-bank`; aquí solo se consume vía `topic`, `subtopic`, `challenge_type` y `difficulty`.
> Mockups: `design/mockups/03-final-level/` (`biomes-overview.svg`, `monsters-sheet.svg`,
> `challenge-screen.svg`). Paleta y elenco: `design/style-guide.md`.

## 1. Principios
1. **Una pregunta = un golpe.** El monstruo es la envoltura visual de un ejercicio; el combate no
   añade habilidad motriz (no hay esquivar ni apuntar). Así la nota refleja conocimiento, no reflejos.
2. **El bioma comunica el tema** antes de leer el texto: el alumno sabe "estoy en Docker" por el
   muelle y los contenedores, no por un título.
3. **Arte acotado por presupuesto.** Cada bioma reutiliza el mismo esqueleto de animación y el mismo
   set de tiles base con *palette swap*; el arte nuevo por bioma es la excepción, no la regla.
4. **Original.** Género sandbox 2D pixel-art sí; sprites, jefes, biomas con nombre, logos o paletas
   exactas de Terraria (u otros) no. Nada de corrupción/carmesí/jungla subterránea, ni jefes-ojo, etc.

## 2. Mapeo bioma ↔ tema

| Tema | Bioma (nombre original) | Metáfora visual | Paleta derivada (≤ 16 colores) | Monstruo común | Monstruo raro | Jefe del bioma |
|---|---|---|---|---|---|---|
| **GitHub / Git** | **Bosque de las Ramas** | Árboles cuyas ramas se bifurcan y se vuelven a unir (branch/merge); hongos como *commits* en el tronco | Pasto/bosque base + tierra; acento naranja `#E8823A` | Diablillo del Rebase (demonio pequeño, verde musgo) | Zombie del Merge (zombie con dos cabezas fusionadas) | **Gran Conflicto** (demonio grande, mitad rojo/mitad azul, marcadores `<<<<` en el pecho) |
| **Regex** | **Cavernas del Patrón** | Cueva con cristales que tienen glifos `.` `*` `+` `?` `[ ]`; estalactitas en patrón repetido | Piedra base + noche; acento cian `#46D6D0` y magenta `#C060D0` | Esqueleto Codicioso (esqueleto pequeño, "se come todo" = `.*` greedy) | Fantasma Comodín (fantasma con `?` en el pecho) | **Coloso del Backtracking** (esqueleto grande que se reensambla al fallar) |
| **Docker** | **Muelle Estiba** | Muelle de madera sobre agua, grúa, pilas de contenedores de colores (capas) | Madera base + cielo día; acentos de contenedores `#D04A3A` `#3A7ED0` `#E8B83A` | Zombie Huérfano (zombie con cadena/etiqueta `<none>`, "contenedor colgado") | Mago de Capas (mago con sombrero apilado en capas) | **Leviatán de Volúmenes** (criatura de agua con contenedores en el lomo) — *variante nueva, ver dudas* |
| **APIs** | **Ciudadela Petición** | Ciudad de murallas con puertas numeradas (puertos), mensajeros-paloma, carteles `200` `404` | Piedra clara + cielo día; acento amarillo-moneda y verde acierto | Demonio Mensajero (demonio pequeño con saca de correo) | Espectro 404 (fantasma que "no se encuentra": parpadea) | **Guardián del Rate-Limit** (demonio grande con reloj de arena; ataca más rápido si respondes rápido) |
| **Agentes** | **Torre del Bucle** | Torre en espiral nocturna; runas de *observe → think → act* en cada piso; herramientas flotantes | Noche base + violeta `#7A4ED0`; acento dorado legendario | Esqueleto Herramienta (esqueleto pequeño con llave inglesa) | Mago del Prompt (mago con pergamino infinito) | **Caballero del Contexto** (caballero negro, legendario; su escudo "olvida" — ver §6) |

Notas del mapeo:
- El **caballero negro** (único legendario del elenco) se reserva como jefe de Agentes por ser el
  tema más avanzado. Si las secciones no siguen ese orden, el jefe legendario debe ir en la última
  sección del camino, no fijo a Agentes (configurable por `section.boss_monster_id`).
- Matemáticas (calentamiento) **no** tiene bioma propio en v1: usa la *Pradera de Práctica* (bioma
  genérico con tiles base sin acento) para cualquier tema sin bioma asignado. Evita bloquear
  temas nuevos generados por el pipeline de PDF a que exista arte.
- Los nombres de monstruos son juegos de palabras con conceptos del tema: son **mnemotécnicos**, no
  decoración. El nombre aparece en la pantalla de combate y en el bestiario del perfil.

## 3. Pipeline de arte

### 3.1 Herramienta
| Herramienta | Pros | Contras | Veredicto |
|---|---|---|---|
| **Aseprite** | Estándar de facto; capas, tags de animación, onion skin, export sprite-sheet + JSON (hash/array) que Phaser carga directo; CLI (`aseprite -b`) para export en CI | De pago (~20 USD); compilarlo desde fuente es gratis pero lento | **Recomendado** para el artista principal |
| **LibreSprite** | Fork libre (GPL) de una versión vieja de Aseprite; formato `.ase` compatible | Sin features recientes (tilemaps, mejoras de export), desarrollo lento | **Alternativa libre** aceptable para colaboradores |
| **Piskel** | Web, gratis, cero instalación, export PNG sheet + JSON | Sin capas serias, archivos `.piskel` poco versionables, frágil para > 30 sprites | Solo para bocetos rápidos / contribuciones externas |

Decisión: fuente de verdad en `.aseprite` (compatible LibreSprite) en `design/sprites/src/`; el
build (`aseprite -b --sheet ... --data ... --format json-array --list-tags`) genera
`frontend/public/assets/sprites/<bioma>/<monstruo>.png|.json`. Los SVG de `design/mockups/` son
**mockups**, no assets de producción.

### 3.2 Tamaños (rejilla lógica)
| Elemento | Tamaño | Escala en pantalla (390 px de ancho) |
|---|---|---|
| Tiles de terreno | 16×16 | ×3 (48 px) |
| Items / iconos / proyectiles | 16×16 | ×2–×3 |
| Jugador, monstruos comunes y raros | 32×32 | ×3–×4 |
| Jefes | 48×48 (raros-jefe) o 64×64 (legendario) | ×2–×3 (≈ mismo tamaño físico que ×4 de 32, pero con más detalle) |
| Fondos parallax | 3 capas, 240×135 lógicos | escalado entero al alto disponible |

Siempre **escalado entero** (`pixelArt: true`, `roundPixels: true` en Phaser) para que no se
emborronen píxeles.

### 3.3 Paletas
- Paleta base del style guide (~30 colores) = superconjunto.
- Cada bioma: **≤ 16 colores** = 10–12 de la base + 2–4 acentos propios (tabla §2). Guardadas como
  `.gpl` (GIMP palette, la leen Aseprite/LibreSprite) en `design/palettes/<bioma>.gpl`.
- Monstruos: **≤ 8 colores** por sprite incluyendo contorno. Las variantes por bioma se hacen por
  *palette swap* (mismo índice, otro color) — un esqueleto base sirve para 3 biomas.
- Contorno oscuro de 1 px siempre (legibilidad sobre cualquier fondo).

### 3.4 Export
- `PNG` sprite-sheet (sin padding interno, 1 px de *extrude* para evitar sangrado) + `JSON` atlas
  (formato *JSON array* de Aseprite / compatible `this.load.aseprite()` de Phaser).
- Tags de animación con nombres fijos: `idle`, `attack`, `hurt`, `defeat` (y `enter` opcional
  para jefes). El código **no** debe referenciar números de frame, solo tags.
- Sonidos: `.ogg` + `.mp3` fallback, ≤ 1 s, mono, en `assets/sfx/`.

### 3.5 Animaciones mínimas
| Tag | Frames | fps | Loop | Notas |
|---|---|---|---|---|
| `idle` | 4 | 6 | sí | respiración 1 px arriba/abajo; ojo parpadea en frame 4 |
| `attack` | 4 | 10 | no | anticipación (1) → impulso (2) → impacto (3) → retorno (4); se dispara en fallo/timeout |
| `hurt` | 2 | 12 | no | frame blanco (flash) + retroceso 2 px; se dispara en acierto |
| `defeat` | 5 | 8 | no | caída/desarme → parpadeo → desaparece en partículas (4 px) |
| `enter` (jefes) | 6 | 8 | no | opcional; entrada del jefe |

Coste: 15 frames por monstruo común ⇒ 10 monstruos × 15 = 150 frames + 5 jefes × ~21 ≈ 255 frames
para v1. Es el número que hay que defender contra el *scope creep*.

## 4. Plantilla de ficha de monstruo

Formato: YAML en `content/monsters/<id>.yaml`, validado con JSON Schema en CI.

```yaml
id: regex-skeleton-greedy          # kebab-case, único, estable (no cambiar al renombrar)
name: "Esqueleto Codicioso"         # i18n: clave name_key en v2
rarity: common                      # common | rare | legendary
biome: pattern-caverns              # id del bioma
topic: regex
subtopics: [quantifiers, greedy-lazy, anchors]   # filtra el banco de preguntas
allowed_challenge_types: [multiple_choice, regex_fill, true_false, predict_output]
difficulty_range: [1, 3]            # 1..5, se cruza con la dificultad de la pregunta
stats:
  hp: 1                             # nº de aciertos para derrotarlo (comunes 1, raros 2, jefes = §6)
  damage: 1                         # corazones que quita un fallo/timeout
  time_modifier: 1.0                # multiplica el tiempo base del tipo de reto
behavior:
  pattern: static                   # static | advance (avanza 1 casilla por turno) | phase (jefe)
  on_player_miss: attack
  special: null                     # p.ej. "regenerates_on_timeout"
sprites:
  sheet: sprites/caverns/skeleton-greedy.png
  atlas: sprites/caverns/skeleton-greedy.json
  size: 32
  palette: palettes/pattern-caverns.gpl
sfx: { hit: sfx/bone-hit.ogg, attack: sfx/bone-swing.ogg, defeat: sfx/bone-collapse.ogg }
lore: "Se come todos los caracteres que puede. Derrótalo con un cuantificador perezoso."
accessibility:
  shape_cue: "skull"                # silueta distintiva, no depender del color
```

Reglas: `allowed_challenge_types` ⊆ catálogo §5; si el banco no tiene preguntas suficientes para
`(topic, subtopics, types, difficulty)` el motor degrada a `multiple_choice` del mismo tema y lo
registra (métrica de cobertura del banco).

## 5. Catálogo de tipos de reto

> **Nota de integración (agente 3):** la fórmula de tiempo canónica vive en
> `add-question-bank/design.md` §5 (más tiempo a mayor dificultad, no menos; ver la razón ahí).
> Los tiempos y multiplicadores de esta tabla son la propuesta original de 3.1 y sirven de
> referencia. Los identificadores `challenge_type` de esta tabla sí son los canónicos y el banco
> los adopta.

Tiempos base en segundos para dificultad 3 (media). **Histórico, no vigente**: multiplicadores por dificultad de
UOLINGO V2.5 (fácil ×1.3, media ×1.0, difícil ×0.75) — sustituidos por `f_diff` creciente de
`add-question-bank` §5 (1→0.8 … 5→1.8); luego × `time_modifier` del monstruo; luego ×
`accessibility.time_factor` del usuario (§8).

| Tipo (`challenge_type`) | Ejemplo | Corrección | Tiempo base | Monstruos que lo usan |
|---|---|---|---|---|
| `multiple_choice` | "¿Qué hace `git rebase -i`?" 4 opciones | Exacta por índice; opciones barajadas por intento | 20 s | Todos (fallback universal) |
| `true_false` | "`docker run` siempre descarga la imagen" | Exacta | 10 s | Comunes (golpes rápidos); combos |
| `regex_fill` | Escribe un regex que acepte las 3 cadenas verdes y rechace las 2 rojas | **Casos de prueba**: se ejecuta el regex del usuario contra *should_match* / *should_not_match* con motor RE2 (sin backtracking catastrófico) y timeout 50 ms; acierto si pasa todos. Se muestran casos fallidos como feedback | 45 s | Esqueleto Codicioso, Fantasma Comodín, Coloso del Backtracking |
| `parsons` (ordenar) | Ordena: `git add`, `git commit`, `git push`, `git checkout -b` | Secuencia exacta **o** cualquiera de las `accepted_orders` declaradas (hay órdenes equivalentes) | 30 s | Diablillo del Rebase, Zombie Huérfano, Gran Conflicto |
| `fill_code` (completar código/comando) | `docker ___ -d -p 8080:80 nginx` | Normalización (trim, espacios múltiples, orden de flags si `flags_unordered`) + lista de respuestas aceptadas; **sin ejecución** en v1 | 30 s | Zombie Huérfano, Mago de Capas, Demonio Mensajero |
| `match_pairs` (emparejar) | Código HTTP ↔ significado | Todas las parejas correctas; daño parcial opcional (n/N parejas) solo en jefes | 35 s | Espectro 404, Guardián del Rate-Limit, Mago del Prompt |
| `spot_bug` (detectar el error) | Dockerfile de 6 líneas: toca la línea errónea | Índice de línea exacto | 25 s | Mago de Capas, Esqueleto Herramienta, jefes |
| `predict_output` (predecir salida) | `re.findall(r"a+?", "aaa")` → ? / respuesta de `curl -I` | Opción múltiple sobre salidas candidatas (v1); texto libre normalizado (v2) | 30 s | Esqueleto Codicioso, Demonio Mensajero, Caballero del Contexto |

Decisiones y trade-offs:
- **Nada de ejecutar código del usuario en v1** salvo regex en RE2 (en cliente con `re2-wasm` o en
  servidor). Ejecutar `docker`/`git` real exige sandbox y triplica el coste; se simula con
  `fill_code`/`predict_output`.
- La **corrección es autoritativa en servidor** (el cliente solo envía la respuesta). Si no,
  la calificación del jefe-examen es trivialmente falsificable.
- Texto libre ≠ IA: no se usa LLM para corregir en combate (latencia + coste + no determinista).
  La corrección con IA queda para ejercicios fuera del nivel final (`add-content-pipeline`).
- En móvil, `regex_fill` y `fill_code` necesitan teclado: la pregunta sube y el escenario se
  reduce a una franja (ver mockup). Se ofrece barra de símbolos (`. * + ? [ ] ( ) ^ $ \ |`).

## 6. Mecánicas de combate

### 6.1 Bucle
1. Aparece monstruo (sale del borde, 400 ms) → se muestra pregunta → arranca temporizador.
2. **Acierto** → animación `hurt` del monstruo, −1 HP del monstruo y −daño a la **barra del jefe/
   sección** (ver 6.3). Si HP del monstruo = 0 → `defeat`, siguiente monstruo.
3. **Fallo o timeout** → `attack` del monstruo, el jugador pierde `damage` corazones (corazones del
   combate, ver abajo). Se muestra la respuesta correcta 2 s (aprendizaje > castigo).
4. Fin: se alcanza la calificación mínima (victoria), se agotan corazones o preguntas (derrota),
   o el usuario abandona.

### 6.2 Corazones vs. vidas de sección
> **Nota de integración (agente 3):** `design.md` §1 fija como regla canónica que los corazones del
> combate = margen de error `N − ⌈p·N⌉` (no 5 fijos): con 5 fijos, N=40/p=60 % sería más estricto
> que la calificación pedida y N=5/p=100 % daría corazones sin sentido. "5 corazones" queda como
> alternativa descartada; si se elige "modo difícil", se aplica como tope `min(margen, 3)`. El coste
> de 1 vida de sección por derrota sigue como pregunta abierta (`design.md` §7.1).

- (Propuesta original 3.1) El combate tiene **corazones propios** (5 por defecto; 3 en modo difícil). Perder todos = perder
  el combate y **1 vida de sección**. Fallar una pregunta no quita vidas de sección directamente:
  si no, el nivel final drenaría las 10 vidas en un intento.
- **Abandonar** (botón siempre visible) solo descarta el progreso temporal del combate, sin coste de
  vida (decisión heredada de UOLINGO V2.5). Riesgo: *abuse* por abandono al ir perdiendo → mitigación:
  las preguntas vistas se marcan y el siguiente intento prioriza las no vistas; contador de
  abandonos en analítica.

### 6.3 Barra de vida del jefe = calificación
> Nota (agente 7.1): la regla vigente es la del spec `final-level` (`g` elegido por el usuario,
> `required = ceil(g·N)`); la alternativa "calificación fija por bioma" de `uolingo-review.md`
> C4/C12 es una opción de la pregunta abierta Q35, no una segunda regla.
- Siguiendo UOLINGO V2.5: el examen tiene N preguntas (3–40) y el usuario elige calificación mínima
  p ∈ [60 %, 100 %]. **HP del jefe = ⌈p·N⌉ aciertos**. Cada acierto en el bioma (con monstruos
  comunes/raros o con el jefe) baja la barra; los monstruos comunes son "la guardia" del jefe y
  el jefe aparece en las últimas ⌈0.3·N⌉ preguntas o cuando la barra está ≤ 30 %.
- Si quedan menos preguntas que HP del jefe → derrota anticipada (se informa, no se alarga en vano).

### 6.4 Combos
- 3 aciertos seguidos = **combo ×2**: el siguiente acierto quita 2 HP al **monstruo** (acelera el
  ritmo), pero **no** a la barra de calificación (la nota no se infla). Visual: contador `x2` y
  destellos.
- 5 seguidos con > 50 % del tiempo restante = "golpe crítico": +monedas (economía en
  `add-engagement-system`). Nunca bonifica la nota.

### 6.5 Jefe por bioma (comportamientos)
| Jefe | Fase 1 (100–50 %) | Fase 2 (< 50 %) | Gimmick (siempre justo y anunciado) |
|---|---|---|---|
| Gran Conflicto (Git) | `multiple_choice`, `parsons` | `spot_bug` en diffs con marcadores de conflicto | Cada 3ª pregunta muestra un "conflicto": 2 respuestas parecen correctas, elige la que resuelve |
| Coloso del Backtracking (Regex) | `predict_output` | `regex_fill` | Al fallar, recupera 1 HP **visual** (no de nota) — el esqueleto se reensambla |
| Leviatán de Volúmenes (Docker) | `fill_code` | `spot_bug` (Dockerfile/compose) | Los contenedores del lomo son "capas": cada acierto destruye una capa |
| Guardián del Rate-Limit (APIs) | `match_pairs` | `predict_output` (códigos/headers) | Si respondes en < 3 s, la siguiente pregunta tiene 20 % menos tiempo (enseña rate limiting); desactivable con tiempo extendido |
| Caballero del Contexto (Agentes) | `multiple_choice` | `parsons` (bucle de agente) | "Ventana de contexto": el enunciado de la pregunta anterior se oculta; solo se pueden responder bien preguntas autocontenidas → el banco debe marcarlas `self_contained: true` |

## 7. Criterios de aceptación de arte
- [ ] Usa solo colores de la paleta del bioma (`.gpl`); validación automática del PNG en CI
      (script que cuenta colores únicos y los compara con la paleta).
- [ ] Tamaño exacto (16/32/48/64), sin píxeles semitransparentes salvo partículas de `defeat`.
- [ ] Contorno de 1 px; silueta reconocible en **negro sólido** a ×1 (test de silueta).
- [ ] Tags `idle/attack/hurt/defeat` presentes con los frames de §3.5 (lint del JSON).
- [ ] Legible a ×3 en un móvil de 390 px y con filtro de daltonismo (deuteranopía/protanopía
      simulado): ningún estado depende **solo** del color.
- [ ] Revisión de originalidad: comparación lado a lado con referencias del género; cualquier
      parecido sustancial con un sprite/jefe existente se rehace.
- [ ] Licencia: arte producido por el equipo o CC0/CC-BY con atribución registrada en
      `design/CREDITS.md`. Nada generado con IA sin revisión de licencia del modelo.

## 8. Accesibilidad
- **Daltonismo**: acierto/error se comunican con color **+ icono** (✓ / ✗) **+ sonido**; la barra de
  vida del monstruo usa patrón (segmentos) además de color; las rarezas se distinguen por forma del
  marco (común liso, raro con remaches, legendario con picos), no solo por el borde de color.
- **Tiempo extendido opcional** *(nota de integración, agente 7.1: el spec `question-bank` fija hoy
  un único modo ×1.5 con tope 180 s; los valores 2.0 y "sin límite" de abajo quedan como
  propuesta pendiente, ver `openspec/open-questions.md` Q36)*: ajuste `time_factor` ∈ {1.0, 1.5, 2.0, sin límite}. "Sin límite"
  desactiva timeout pero marca el intento como *práctica* (no cuenta para ranking/arena, sí para
  avanzar). Decisión de producto pendiente (ver dudas).
- **Movimiento reducido**: respeta `prefers-reduced-motion` → sin screen-shake, flashes atenuados
  (el `hurt` usa contorno en lugar de destello blanco a pantalla completa).
- Texto de preguntas en fuente legible (no pixel) ≥ 16 px; 'Press Start 2P' solo para UI corta
  (títulos, contadores). La fuente pixel es ilegible en párrafos de código.
- Lectores de pantalla: la pregunta y opciones son DOM accesible superpuesto al canvas de Phaser,
  no texto pintado en el canvas.

## 9. Riesgos
| Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|
| **Scope creep de arte** (cada tema pide monstruos/jefe/tileset propios) | Alta | Alto | Presupuesto fijo v1: 5 biomas × (1 común + 1 raro + 1 jefe) + bioma genérico. Variantes por *palette swap*. Todo lo demás es v2 |
| **Inconsistencia** entre artistas/sprites | Media | Medio | Paletas `.gpl` bloqueadas, plantilla `.aseprite` con capas y guías, checklist §7 en PR |
| Temas nuevos (PDF→preguntas) sin bioma | Alta | Medio | Bioma genérico + monstruos genéricos; el arte nunca bloquea contenido |
| Banco sin preguntas para un tipo/subtema | Media | Medio | Fallback a `multiple_choice`; métrica de cobertura por `(topic, type)` |
| Presión de tiempo genera ansiedad / abandona usuarios lentos | Media | Alto | Tiempo extendido, mostrar respuesta correcta tras fallo, corazones propios del combate |
| Teclado móvil tapa la escena en `regex_fill`/`fill_code` | Alta | Bajo | Layout compacto (escena en franja), barra de símbolos |
| Parecido con Terraria (IP) | Baja | Alto | Nombres/siluetas originales, revisión §7, sin biomas/jefes análogos |
| Trampas (respuesta en cliente) | Media | Alto | Corrección en servidor; el cliente nunca recibe la respuesta antes de enviar |

## 10. Dudas abiertas
1. **Elenco**: el Leviatán de Volúmenes (Docker) no está en el elenco del style guide. ¿Se
   amplía el elenco con 1 criatura nueva o el jefe de Docker es un "zombie grande"/mago
   reskin? (Recomendación: ampliar; un jefe acuático hace el bioma memorable.)
2. ¿El jefe legendario va fijo en Agentes o en "la última sección" del camino del usuario?
3. ¿"Sin límite de tiempo" cuenta como victoria plena (desbloquea cofre legendario) o solo práctica?
4. ¿Los corazones del combate (5) se pueden recargar con pociones de `add-items-and-inventory`?
   Si sí, hay riesgo de *pay-to-pass* en un nivel que funciona como examen.
5. ¿Se permite daño parcial en `match_pairs`/`regex_fill` (n/N casos) para la nota? Afecta a la
   semántica "HP del jefe = aciertos necesarios".
6. Ejecución real de comandos (`git`/`docker` en sandbox) para v2: ¿vale el coste de infraestructura?
