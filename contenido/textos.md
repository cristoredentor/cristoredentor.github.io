# Textos del sitio (fuente única de verdad)

> Los agentes copian estos textos **tal cual** al HTML. Si un texto cambia, se cambia aquí primero.
> Los marcados con 🔒 son palabras textuales del autor: no se reescriben, solo se corrigen errores
> evidentes de tipografía si el autor lo aprueba.
> Los marcados con ✏️ son borradores propuestos: el autor debe aprobarlos antes de publicar.

---

## 0. Pantalla inicial

- Título (h1, puede ir visualmente oculto si el personaje ocupa la escena): **Cristopher Góngora**
- Subtítulo ✏️: *Ciencia de Datos · Ingeniería en Computación · ITAM*
- Menú (botones dorados, en este orden):
  1. **¿Quién soy?** → submenú: **Resumen** · **Fotos**
  2. **Proyectos**
  3. **Carrera**
- Pista de controles ✏️ (pequeña, abajo): *Usa ↑ ↓ y Enter, o haz clic*

---

## 1. ¿Quién soy?

### 1.1 Resumen — cédula de museo 🔒

**Cristopher Góngora**

Me considero una persona apasionada. Estudio computación y ciencia de datos porque creo que se
puede hacer un gran impacto en el mundo por medio del uso correcto de las tecnologías. Mis
proyectos trato de hacerlos con cariño, pues soy de la idea de que hay que disfrutar lo que
hacemos, aparte uno siempre puede hacer más de lo que los demás esperan y añadir a lo que hace un
toque artístico. Me gusta mucho subir montañas, admirar paisajes, jugar futbol, ir al gimnasio y
leer o hablar sobre temas filosóficos.

### 1.2 Fotos — cuadros de la galería

Cada foto va en un marco dorado pixel-art, colgada arriba de la cédula. Título corto ✏️ en una
mini-cédula bajo cada cuadro (el autor puede cambiarlos):

| Archivo | Título del cuadro ✏️ | `alt` (accesibilidad) |
|---|---|---|
| `assets/fotos/foto-1-alpaca.jpg` | *Compañía andina* | Cristopher recostado en el pasto junto a una alpaca |
| `assets/fotos/foto-2-estadio.jpg` | *Noche de futbol* | Cristopher en las gradas de un estadio iluminado de noche |
| `assets/fotos/foto-3-machu-picchu.jpg` | *Machu Picchu* | Cristopher de pie frente a Machu Picchu y sus montañas |
| `assets/fotos/foto-4-montana-de-colores.jpg` | *Montaña de colores* | Cristopher con los brazos abiertos en una cresta de montaña rojiza |
| `assets/fotos/foto-5-laguna.jpg` | *Laguna entre montañas* | Laguna turquesa entre montañas nevadas y rocas |

---

## 2. Proyectos

Carrusel horizontal con flechas doradas ← →. Orden: 1) Pixtart, 2) Agnis.

### 2.1 Pixtart ✏️ (basado en el prompt/proyecto original de Pixtart)

Encabezado visual: `assets/fondos/pixtart-aula/pixtart-aula-escena.svg` (maestro búho y alumnos).

**Pixtart** — *Aprender cualquier tema mientras juegas.*

Pixtart es una plataforma de aprendizaje gamificada que busca hacer entretenido aprender temas
que pueden llegar a ser muy complejos. Combina un camino de lecciones con un mundo pixel-art de
aventura: cada tema es una sección con niveles, vidas y cofres de recompensa, y termina en un
**nivel final** —un juego 2D donde cada monstruo es una pregunta bajo presión de tiempo—.

- **Constancia con consecuencias visibles:** el personaje evoluciona (de *Brote* a *Leyenda*) al
  acertar y estudiar a diario, y retrocede si se pierden todas las vidas de una sección.
- **Incentivos para guiar el aprendizaje:** cofres normales y legendarios, mascotas, personajes de
  apoyo, atuendos y paletas de color que se desbloquean jugando.
- **Arena multijugador:** duelos por tema donde gana quien responde primero y correcto.
- **Temas iniciales:** Git/GitHub, Regex, Docker, APIs y Agentes, cada uno con su propio bioma.
- **Diseño:** arte 100 % original, especificado con OpenSpec (propuestas, diseño y escenarios
  verificables) antes de escribir código.

Rol ✏️: *Creador — diseño de producto, mecánicas, arte pixel-art y especificación técnica.*

### 2.2 Agnis ✏️

**Agnis** — *Cofundador*

Agnis es una startup fundada con el objetivo de hacer seguro el uso de agentes de IA, evitando
problemas de ciberseguridad. Buscamos que desplegar agentes sea intuitivo, con una interfaz
amigable que te ayude a ver:

- **Permisos:** qué puede hacer cada agente y sobre qué recursos.
- **Acciones críticas:** las operaciones sensibles, señaladas antes de que ocurran.
- **Flujo de trabajo real:** lo que el agente hizo (pasado) y lo que planea hacer (futuro).
- **Reportes confiables:** evidencia clara para auditar y tomar decisiones.

---

## 3. Carrera — "Nivel final"

Presentada como el nivel final de Pixtart: el jugador avanza por el escenario y cada logro aparece
como un cofre/estandarte que se abre.

### Ficha del jugador ✏️

- **Estudios:** Ciencia de Datos e Ingeniería y Ciencias de la Computación — ITAM.
- **Semestre:** quinto.
- **Lenguajes:** C · Python · Java · R
- **Datos y herramientas:** SQL · Tableau · Excel

### Logros (en este orden)

1. **Beca Baillères (ITAM)** — cubre la totalidad del costo de la carrera.
2. **Reconocimiento a alto rendimiento académico 2026** — Licenciatura en Ciencia de Datos (ITAM).
3. **Reconocimiento a alto rendimiento académico 2026** — Ingeniería y Ciencias de la Computación (ITAM).
4. **EPIC Entrepreneurship & Innovation Bootcamp (ITAM)** — curso intensivo de dos semanas para
   potenciar ideas de emprendimiento (15–27 de junio de 2026).
5. **Datatón ITAM** — participación en la ronda eliminatoria.

> Nota: los dos reconocimientos de alto rendimiento salen del PDF de ITAM; el prompt original no
> los menciona en texto, pero sí pide mostrar todos los diplomas. Confirmar con el autor si se
> listan como logro o solo como diploma.

### Diplomas (galería, todos)

| Imagen (`assets/diplomas/img/`) | Título visible | Emisor |
|---|---|---|
| `itam-beca-bailleres.jpg` | Beca Baillères | ITAM |
| `itam-alto-rendimiento-ciencia-de-datos.jpg` | Alto rendimiento académico 2026 — Ciencia de Datos | ITAM |
| `itam-alto-rendimiento-computacion.jpg` | Alto rendimiento académico 2026 — Ing. y Ciencias de la Computación | ITAM |
| `itam-bootcamp-emprendimiento-epic-lab.jpg` | Entrepreneurship & Innovation Bootcamp | EPIC Lab ITAM |
| `itam-dataton.jpg` | Datatón — ronda eliminatoria | ITAM · INEGI · ANTAD |
| `harvardx-cs50x.jpg` | CS50x: Introduction to Computer Science | HarvardX (edX) |
| `upv-excel-xls101x.jpg` | Excel: Fundamentos y herramientas (XLS101x) | UPValenciaX (edX) |
| `upv-excel-xls201x.jpg` | Excel: gestión de datos (XLS201x) | UPValenciaX (edX) |
| `upv-excel-xls202x.jpg` | Excel avanzado: importación y análisis de datos (XLS202x) | UPValenciaX (edX) |
| `datacamp-introduction-to-python-for-developers.jpg` | Introduction to Python for Developers | DataCamp |
| `datacamp-intermediate-python-for-developers.jpg` | Intermediate Python for Developers | DataCamp |
| `datacamp-introduction-to-git.jpg` | Introduction to Git | DataCamp |
| `datacamp-intermediate-git.jpg` | Intermediate Git | DataCamp |
| `datacamp-introduction-to-docker.jpg` | Introduction to Docker | DataCamp |
| `datacamp-intermediate-docker.jpg` | Intermediate Docker | DataCamp |
| `datacamp-introduction-to-fastapi.jpg` | Introduction to FastAPI | DataCamp |

> Las imágenes de edX traen en el margen la URL e impresión del navegador; el agente de assets
> puede recortarlas (sin tocar el contenido del certificado) antes de publicar.
> La carta de la Beca Baillères tiene **la clave única censurada** en la imagen y su PDF se quitó a
> propósito de `assets/diplomas/pdf/` (el original sigue en la carpeta `diplomas/` del autor).
