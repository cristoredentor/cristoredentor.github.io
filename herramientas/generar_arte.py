#!/usr/bin/env python3
"""Genera el arte pixel-art NUEVO de la GitHub Pages (personaje, fondos, UI, iconos).

Solo Python estandar y determinista (random.Random con semilla fija): correrlo dos veces da
exactamente los mismos SVG. Todo se dibuja con <rect> en una rejilla de pixeles y
shape-rendering="crispEdges", igual que los sprites de Pixtart.

Uso:  python3 herramientas/generar_arte.py      (desde la raiz de esta carpeta)
"""
from __future__ import annotations

import random
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
A = RAIZ / "assets"

# --------------------------------------------------------------------------------------
# Paleta del sitio (azul-grisacea, sacada de la muestra del PDF = tile-stone en paleta Aurora)
# --------------------------------------------------------------------------------------
P = {
    "noche": "#1E2529", "pizarra": "#2D373C", "acero": "#3D4A51", "piedra": "#566972",
    "piedra_c": "#8196A0", "niebla": "#BDC8CD", "hueso": "#E6ECEE", "crema": "#F3EEDC",
    "oro": "#D9A93A", "oro_c": "#F2D27A", "oro_s": "#A87A1E", "oro_o": "#4A3510",
    "contorno": "#1A2024",
}


def svg(w: int, h: int, cuerpo: str, titulo: str, extra: str = "", escala: int = 1) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w * escala}" height="{h * escala}" shape-rendering="crispEdges">\n'
        f"<title>{titulo}</title>\n{extra}{cuerpo}</svg>\n"
    )


def r(x, y, w, h, c, extra="") -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"{extra}/>\n'


def rejilla(filas: list[str], leyenda: dict[str, str], dx: int = 0, dy: int = 0) -> str:
    """Convierte filas ASCII en <rect>, uniendo tramos horizontales del mismo color."""
    out = []
    for y, fila in enumerate(filas):
        x = 0
        while x < len(fila):
            ch = fila[x]
            if ch in leyenda:
                x0 = x
                while x < len(fila) and fila[x] == ch:
                    x += 1
                out.append(r(x0 + dx, y + dy, x - x0, 1, leyenda[ch]))
            else:
                x += 1
    return "".join(out)


def guarda(ruta: Path, texto: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8")
    print("  ", ruta.relative_to(RAIZ))


# --------------------------------------------------------------------------------------
# 1. Personaje principal: Cristopher (rubio, traje formal azul-gris, saludando) 32x32
# --------------------------------------------------------------------------------------
LEY_PJ = {
    "O": P["contorno"], "H": "#E2C66E", "h": "#B89A48", "L": "#F4E3A6",
    "S": "#D9CBBE", "s": "#B3A598", "E": P["contorno"], "m": "#6E5555", "w": "#FFFFFF",
    "J": "#2F3438", "j": "#202427", "K": "#4A5156", "C": P["hueso"], "c": P["niebla"],
    "T": "#3F5566", "P": "#4F6A8A", "p": "#3B5270", "B": "#F7F9FA", "b": P["piedra"],
}
PJ_BASE = [
    "................................",
    "...........OOOOOOOOOO...........",
    ".........OOHHLLLLHHHHOO.........",
    "........OHHHLLLHHHHHHHHO........",
    ".......OHHHHHHHHHHHHHHHHO.......",
    ".......OHHHHHHHHHHHHHHHhO.......",
    ".......OHHHHHhHHHHHHHHHhO.......",
    ".......OHHSSShHHHHHhSSHhO.......",
    ".......OHSSSSSSSSSSSSSSHO.......",
    ".......OSSSwESSSSSSwESSSO.......",
    ".......OSSSEESSSSSSEESSSO.......",
    ".......OSsSSSSSSSSSSSSsSO.......",
    ".......OSSSSSmSSSSmSSSSSO.......",
    ".......OSSSSSSmmmmSSSSSSO.......",
    "........OSSSSSSSSSSSSSSO........",
    "..........OOOssssssOOO..........",
    ".......OOJJJKCCCCCCKJJJOO.......",
    "......OJJjJJKCCCCCCKJJjJJO......",
    "......OJJjJJJKCCCCKJJJjJJO......",
    "......OJJjJJJJKCCKJJJJjJJO......",
    "......OJJjJJJJJCCJJJJJjJJO......",
    "......OJJjJJJJJccJJJJJjJJO......",
    "......OJJjjjjjjjjjjjjjjJJO......",
    "......OSSOPPPPPPPPPPPPOSSO......",
    "......OssOPPPPPPPPPPPPOssO......",
    ".......OO.OPPPPPPPPPPO.OO.......",
    "..........OPPPPOOPPPPO..........",
    "..........OPPpPOOPpPPO..........",
    "..........OPPpPOOPpPPO..........",
    ".........OBBBBBOOBBBBBO.........",
    ".........ObbbbbOObbbbbO.........",
    "................................",
]


def _pinta(filas: list[str], y: int, x: int, trozo: str) -> None:
    f = list(filas[y])
    for i, ch in enumerate(trozo):
        if ch != " ":
            f[x + i] = ch
    filas[y] = "".join(f)


def pj_saludo(desplaza: int) -> list[str]:
    f = list(PJ_BASE)
    # quita el brazo derecho (lado derecho de la imagen) que colgaba
    for y in range(17, 23):
        _pinta(f, y, 23, "O..")
    for y in (23, 24):
        _pinta(f, y, 23, "...")
    _pinta(f, 25, 23, "..")
    _pinta(f, 16, 22, "JJO")
    # brazo levantado con la mano abierta (saludo); 'desplaza' mueve la mano 1 px
    d = desplaza
    _pinta(f, 3, 26 + d, "O.O")
    _pinta(f, 4, 25 + d, "OSOSO")
    _pinta(f, 5, 25 + d, "OSSSSO")
    _pinta(f, 6, 24 + d, "OSSSSSO")
    _pinta(f, 7, 24 + d, "OsSSSsO")
    _pinta(f, 8, 25 + d, "OsssO")
    _pinta(f, 9, 25 + d // 2, "OjjjO")
    for y in range(10, 14):
        _pinta(f, y, 25, "OJJjO")
    _pinta(f, 14, 24, "OJJJjO")
    _pinta(f, 15, 23, "OJJJO")
    _pinta(f, 16, 22, "JJJJO")
    _pinta(f, 17, 22, "JJO")
    return [fila[:32].ljust(32, ".") for fila in f]


def personaje() -> None:
    d = A / "personajes" / "cristopher"
    t = "Cristopher — personaje principal (rubio, chamarra negra, jeans y tenis blancos), 32x32"
    guarda(d / "cristopher-idle.svg", svg(32, 32, rejilla(PJ_BASE, LEY_PJ), t + " · idle", escala=8))
    for i, dd in enumerate((0, 1), start=1):
        guarda(d / f"cristopher-saludo-f{i}.svg",
               svg(32, 32, rejilla(pj_saludo(dd), LEY_PJ), t + f" · saludo f{i}", escala=8))
    # hoja de sprites horizontal: idle | saludo f1 | saludo f2 (para CSS steps())
    hoja = rejilla(PJ_BASE, LEY_PJ) + rejilla(pj_saludo(0), LEY_PJ, dx=32) + \
        rejilla(pj_saludo(1), LEY_PJ, dx=64)
    guarda(d / "cristopher-hoja.svg", svg(96, 32, hoja, t + " · hoja 3 frames (idle, saludo f1, f2)", escala=4))
    guarda(d / "preview.html", PREVIEW_PJ)


PREVIEW_PJ = """<!doctype html><meta charset="utf-8"><title>Preview personaje</title>
<style>body{background:#2D373C;display:grid;place-items:center;height:100vh;margin:0}
.pj{width:256px;height:256px;background:url(cristopher-hoja.svg) 0 0/768px 256px no-repeat;
image-rendering:pixelated;animation:saluda .8s steps(1) infinite}
@keyframes saluda{0%{background-position:-256px 0}50%{background-position:-512px 0}}</style>
<div class="pj" role="img" aria-label="Cristopher saludando"></div>
"""


# --------------------------------------------------------------------------------------
# 2. Mascotas: sprite limpio sacado de las tarjetas de Pixtart (sin marco ni fondo)
# --------------------------------------------------------------------------------------
def mascotas() -> None:
    fondo = {"#2B2F55", "#353A66", "#1B1F3B", "#FFE27A", "#F2A81D", "#3F7FE0", "#8FB8FF", "#B8B8B8"}
    for src in sorted((A / "mascotas" / "tarjetas").glob("pet-*.svg")):
        txt = src.read_text(encoding="utf-8")
        m = re.search(r'<g transform="translate\(24,20\)">(.*?)</g>\s*<text', txt, re.S)
        bloque = m.group(1) if m else txt
        celdas = []
        for a in re.finditer(r"<rect ([^>]*)/>", bloque):
            at = dict(re.findall(r'(\w+)="([^"]*)"', a.group(1)))
            if "opacity" in at or at.get("fill", "").upper() in fondo:
                continue
            try:
                x, y, w, h = (int(float(at[k])) for k in ("x", "y", "width", "height"))
            except (KeyError, ValueError):
                continue
            if w % 8 or h % 8 or w >= 160 or not (6 <= x < 166 and 6 <= y < 166):
                continue
            celdas.append((x, y, w, h, at["fill"]))
        if not celdas:
            print("   (sin celdas)", src.name)
            continue
        x0 = min(c[0] for c in celdas)
        y0 = min(c[1] for c in celdas)
        x1 = max(c[0] + c[2] for c in celdas)
        y1 = max(c[1] + c[3] for c in celdas)
        cuerpo = "".join(r((x - x0) // 8, (y - y0) // 8, w // 8, h // 8, c) for x, y, w, h, c in celdas)
        W, H = (x1 - x0) // 8, (y1 - y0) // 8
        nombre = src.stem.replace("pet-", "")
        guarda(A / "mascotas" / f"{nombre}.svg", svg(W, H, cuerpo, f"Mascota {nombre} (sprite limpio)", escala=8))


# --------------------------------------------------------------------------------------
# 3. Fondos
# --------------------------------------------------------------------------------------
def banda_cielo(w: int, colores: list[str], y0: int, alto: int) -> str:
    """Cielo por bandas con frontera tramada (dither) de 2 filas, estilo pixel."""
    out, n = [], len(colores)
    paso = alto // n
    for i, c in enumerate(colores):
        out.append(r(0, y0 + i * paso, w, paso + (alto - paso * n if i == n - 1 else 0), c))
        if i < n - 1:
            yb = y0 + (i + 1) * paso
            for x in range(0, w, 2):
                out.append(r(x, yb - 1, 1, 1, colores[i + 1]))
                out.append(r(x + 1, yb, 1, 1, c))
    return "".join(out)


def disco(cx: int, cy: int, rad: float, c: str, extra: str = "") -> str:
    out = []
    for y in range(int(cy - rad), int(cy + rad) + 1):
        dx = int((rad * rad - (y - cy) ** 2) ** 0.5) if rad * rad >= (y - cy) ** 2 else -1
        if dx >= 0:
            out.append(r(cx - dx, y, 2 * dx + 1, 1, c, extra))
    return "".join(out)


def cresta(rng: random.Random, w: int, base: int, amp: int, paso: int) -> list[int]:
    pts, y = [], base
    for _x in range(0, w + paso, paso):
        y = max(base - amp, min(base + amp // 3, y + rng.randint(-amp // 2, amp // 2)))
        pts.append(y)
    alturas = []
    for x in range(w):
        i, t = divmod(x, paso)
        a, b = pts[i], pts[i + 1]
        alturas.append(round(a + (b - a) * t / paso))
    return alturas


def silueta(alturas: list[int], fondo_y: int, c: str, luz: str | None = None) -> str:
    out = []
    for x, y in enumerate(alturas):
        out.append(r(x, y, 1, fondo_y - y, c))
        if luz and x > 0 and alturas[x - 1] > y:
            out.append(r(x, y, 1, 2, luz))
    return "".join(out)


def pino(x: int, base: int, alto: int, c: tuple[str, str, str], tronco: str) -> str:
    out = [r(x - 1, base - 4, 3, 4, tronco)]
    cuerpo = alto - 4
    for k in range(cuerpo):
        y = base - 4 - k
        nivel = (cuerpo - k) / cuerpo
        diente = (k % 6) / 6
        ancho = max(1, int(nivel * alto * 0.36 * (1 - 0.35 * diente)))
        out.append(r(x - ancho, y, 2 * ancho + 1, 1, c[0]))
        out.append(r(x + 1, y, ancho, 1, c[1]))           # sombra a la derecha
        if k % 6 == 5:
            out.append(r(x - ancho, y, ancho, 1, c[2]))   # brillo en cada piso
    return "".join(out)


def copa(x: int, base: int, rad: int, c: tuple[str, str, str], tronco: str) -> str:
    out = [r(x - 1, base - rad - 3, 3, rad + 3, tronco)]
    cy = base - rad - 4 - rad // 2
    out.append(disco(x, cy, rad, c[0]))
    out.append(disco(x + rad // 3, cy + rad // 3, rad * 0.65, c[1]))
    out.append(disco(x - rad // 3, cy - rad // 3, rad * 0.4, c[2]))
    out.append(disco(x, cy, rad * 0.25, c[0]))
    return "".join(out)


def g_arbol(contenido: str, x: int, base: int, i: int) -> str:
    return (f'<g class="arbol" style="transform-origin:{x}px {base}px;--i:{i}">\n'
            f"{contenido}</g>\n")


def nubes(rng: random.Random, w: int, n: int, ytop: int, ybot: int, c: str, s: str) -> str:
    out = []
    for i in range(n):
        x, y, L = rng.randint(0, w - 40), rng.randint(ytop, ybot), rng.randint(18, 40)
        g = r(x + 4, y, L - 8, 3, c) + r(x, y + 3, L, 4, c) + r(x + 2, y + 7, L - 4, 2, s)
        g += r(x + L // 3, y - 3, L // 3, 3, c)
        out.append(f'<g class="nube" style="--i:{i}">\n{g}</g>\n')
    return "".join(out)


def fondo_inicio() -> None:
    W, H = 320, 180
    rng = random.Random(2026)
    d = A / "fondos" / "inicio"
    cielo = banda_cielo(W, ["#2D373C", "#3D4A51", "#4C5D66", "#647A84", "#8196A0", "#A9B6B4", "#D3CDB6"], 0, 132)
    sol = ""
    for rad, op in ((34, 0.10), (26, 0.16), (19, 0.25)):
        sol += disco(246, 92, rad, "#F2DE9A", f' opacity="{op}"')
    sol += disco(246, 92, 13, "#F6E7B4") + disco(246, 92, 10, "#FBF2D2")
    guarda(d / "capa-1-cielo-sol.svg", svg(W, H, cielo + sol, "Inicio · capa 1 · cielo azul-gris y sol al fondo"))
    guarda(d / "capa-2-nubes.svg", svg(W, H, nubes(rng, W, 7, 12, 70, "#C9D2D4", "#9FAEB3"), "Inicio · capa 2 · nubes (clase .nube)"))
    mont = silueta(cresta(rng, W, 104, 30, 16), 140, "#4A5A63", "#BDC8CD")
    guarda(d / "capa-3-montanas.svg", svg(W, H, mont, "Inicio · capa 3 · montañas lejanas"))
    col = silueta(cresta(rng, W, 128, 10, 20), 160, "#4F625E") + silueta(cresta(rng, W, 138, 6, 24), 160, "#435552")
    guarda(d / "capa-4-colinas.svg", svg(W, H, col, "Inicio · capa 4 · colinas"))
    verdes_f = ("#4E6A5E", "#3B5149", "#6E8A7C")
    verdes_c = ("#425C52", "#31443E", "#5E7A6C")
    arb, i = "", 0
    for x in range(6, W, 22):
        xx, base = x + rng.randint(-5, 5), 146 + rng.randint(-2, 2)
        if rng.random() < 0.6:
            arb += g_arbol(pino(xx, base, rng.randint(26, 36), verdes_f, "#3A3330"), xx, base, i)
        else:
            arb += g_arbol(copa(xx, base, rng.randint(7, 10), verdes_f, "#3A3330"), xx, base, i)
        i += 1
    guarda(d / "capa-5-arboles-fondo.svg", svg(W, H, arb, "Inicio · capa 5 · árboles de fondo (clase .arbol, se mecen)"))
    pasto = r(0, 150, W, 30, "#3E4F4C") + r(0, 150, W, 2, "#56706A")
    for x in range(0, W, 2):
        if rng.random() < 0.5:
            pasto += r(x, 151 + rng.randint(0, 25), 1, 1, "#4A5E5A")
    arb2, i = "", 0
    for x in (14, 70, 286, 304):
        base = 166
        arb2 += g_arbol(pino(x, base, 52, verdes_c, "#2E2826") if x in (14, 304)
                        else copa(x, base, 14, verdes_c, "#2E2826"), x, base, i)
        i += 1
    matas = ""
    for k in range(40):
        x, y = rng.randint(0, W - 3), rng.randint(152, 178)
        matas += (f'<g class="mata" style="transform-origin:{x + 1}px {y + 3}px;--i:{k}">'
                  + r(x, y + 1, 1, 2, "#6E8A7C") + r(x + 1, y, 1, 3, "#5E7A6C") + r(x + 2, y + 1, 1, 2, "#6E8A7C")
                  + "</g>\n")
    guarda(d / "capa-6-pasto-arboles-frente.svg",
           svg(W, H, pasto + matas + arb2, "Inicio · capa 6 · pasto (clase .mata) y árboles cercanos (clase .arbol)"))
    viento = ""
    for k in range(14):
        x, y, L = rng.randint(0, W), rng.randint(20, 165), rng.randint(10, 34)
        viento += (f'<g class="rafaga" style="--i:{k}">' + r(x, y, L, 1, "#E6ECEE", ' opacity="0.55"')
                   + r(x + L // 3, y - 1, L // 2, 1, "#E6ECEE", ' opacity="0.3"') + "</g>\n")
    for k in range(18):
        x, y = rng.randint(0, W), rng.randint(60, 170)
        c = rng.choice(["#6E8A7C", "#8FA67A", "#B89A48"])
        viento += f'<g class="hoja" style="--i:{k}">' + r(x, y, 2, 1, c) + r(x + 1, y + 1, 1, 1, c) + "</g>\n"
    guarda(d / "capa-7-viento-hojas.svg", svg(W, H, viento, "Inicio · capa 7 · ráfagas (.rafaga) y hojas (.hoja)"))
    guarda(d / "preview.html", PREVIEW_INICIO)


PREVIEW_INICIO = """<!doctype html><html lang="es"><meta charset="utf-8">
<title>Preview pantalla inicial</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<!-- Prototipo de referencia para el subagente de animación: NO es la página final. -->
<style>
body{margin:0;background:#1E2529;display:grid;place-items:center;min-height:100vh}
.escena{position:relative;width:min(100vw,1280px);aspect-ratio:16/9;overflow:hidden}
.escena>object,.escena>img{position:absolute;inset:0;width:100%;height:100%;image-rendering:pixelated}
.pj{position:absolute;left:50%;bottom:6%;width:22%;aspect-ratio:1;transform:translateX(-50%);
 background:url(../../personajes/cristopher/cristopher-hoja.svg) 0 0/300% 100% no-repeat;image-rendering:pixelated;
 animation:saluda 1s steps(1) infinite}
@keyframes saluda{0%{background-position:50% 0}50%{background-position:100% 0}}
.escena>.mascota{position:absolute;inset:auto;height:auto;bottom:9%;width:7%;filter:saturate(.7);image-rendering:pixelated;animation:pasea 14s linear infinite}
.escena>.m2{animation-delay:-5s;width:6%}.escena>.m3{animation-delay:-10s;width:6.5%}
@keyframes pasea{0%{left:-10%;transform:translateY(0)}25%{transform:translateY(-6%)}50%{transform:translateY(0)}
75%{transform:translateY(-6%)}100%{left:110%;transform:translateY(0)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>
<div class="escena">
 <object data="capa-1-cielo-sol.svg" type="image/svg+xml"></object>
 <object data="capa-2-nubes.svg" type="image/svg+xml"></object>
 <object data="capa-3-montanas.svg" type="image/svg+xml"></object>
 <object data="capa-4-colinas.svg" type="image/svg+xml"></object>
 <object data="capa-5-arboles-fondo.svg" type="image/svg+xml" class="anim"></object>
 <object data="capa-6-pasto-arboles-frente.svg" type="image/svg+xml" class="anim"></object>
 <img class="mascota m1" src="../../mascotas/ember-fox.svg" alt="">
 <img class="mascota m2" src="../../mascotas/crystal-owl.svg" alt="">
 <img class="mascota m3" src="../../mascotas/mini-golem.svg" alt="">
 <div class="pj" role="img" aria-label="Cristopher saludando"></div>
 <object data="capa-7-viento-hojas.svg" type="image/svg+xml" class="anim"></object>
</div>
<script>
// Inyecta en cada SVG las animaciones de viento (mecer árboles, ráfagas, hojas, nubes).
const css=`.arbol{animation:mece 3.2s ease-in-out infinite;animation-delay:calc(var(--i)*-.37s)}
.mata{animation:mece 1.6s ease-in-out infinite;animation-delay:calc(var(--i)*-.13s)}
@keyframes mece{0%,100%{transform:skewX(0)}50%{transform:skewX(-6deg)}}
.rafaga{animation:sopla 4s linear infinite;animation-delay:calc(var(--i)*-.6s)}
@keyframes sopla{0%{transform:translateX(330px);opacity:0}15%{opacity:1}100%{transform:translateX(-360px);opacity:0}}
.hoja{animation:vuela 6s linear infinite;animation-delay:calc(var(--i)*-.45s)}
@keyframes vuela{0%{transform:translate(330px,-20px) rotate(0)}100%{transform:translate(-340px,25px) rotate(720deg)}}
.nube{animation:deriva 90s linear infinite;animation-delay:calc(var(--i)*-13s)}
@keyframes deriva{0%{transform:translateX(0)}100%{transform:translateX(-340px)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}`;
document.querySelectorAll('object').forEach(o=>o.addEventListener('load',()=>{
 const d=o.contentDocument; if(!d) return; const s=d.createElementNS('http://www.w3.org/2000/svg','style');
 s.textContent=css; d.documentElement.appendChild(s);}));
</script>
"""


def fondo_museo() -> None:
    W, H = 320, 180
    rng = random.Random(7)
    out = r(0, 0, W, H, "#3D4A51")
    out += r(0, 0, W, 10, "#2D373C") + r(0, 10, W, 2, "#566972")                    # moldura techo
    for x in range(8, W, 64):                                                         # paneles de pared
        out += r(x, 22, 52, 86, "#435159") + r(x, 22, 52, 1, "#566972") + r(x, 107, 52, 1, "#2D373C")
        out += r(x, 22, 1, 86, "#566972") + r(x + 51, 22, 1, 86, "#2D373C")
    for x in range(W // 64 + 1):                                                      # focos de luz
        cx = 34 + x * 64
        out += r(cx - 4, 12, 9, 3, "#2D373C") + r(cx - 2, 15, 5, 2, "#F2DE9A")
        for k in range(1, 40):
            out += r(cx - 2 - k // 3, 16 + k, 5 + 2 * (k // 3), 1, "#F2DE9A", ' opacity="0.06"')
    out += r(0, 116, W, 22, "#2D373C") + r(0, 116, W, 2, "#566972") + r(0, 136, W, 2, "#1E2529")  # zócalo
    for x in range(0, W, 16):
        out += r(x, 120, 1, 14, "#3D4A51")
    for y in range(138, H, 8):                                                        # piso en damero
        for x in range(0, W, 16):
            alt = ((x // 16) + (y - 138) // 8) % 2
            out += r(x, y, 16, 8, "#566972" if alt else "#4A5A63")
    out += r(0, 138, W, 1, "#8196A0")
    for x in (40, 280):                                                               # postes y cordón dorado
        out += r(x, 140, 3, 26, P["oro_s"]) + r(x - 2, 138, 7, 3, P["oro"]) + r(x - 3, 166, 9, 3, P["oro_s"])
    for x in range(43, 280):
        y = 145 + int(5 * (1 - ((x - 161.5) / 118.5) ** 2))
        out += r(x, y, 1, 2, "#7A3D3D")
    out += r(130, 150, 60, 6, "#5C4A3A") + r(130, 150, 60, 1, "#7A5C3E") + r(134, 156, 4, 10, "#3A2E26") + r(182, 156, 4, 10, "#3A2E26")
    _ = rng
    guarda(A / "fondos" / "museo" / "museo-sala.svg",
           svg(W, H, out, "¿Quién soy? · sala de museo pixel-art (paredes, focos, cordón, banca)"))


def _sprite_interior(ruta: Path) -> str:
    txt = ruta.read_text(encoding="utf-8")
    return "".join(re.findall(r"<rect [^>]*/>", txt))


def fondo_aula() -> None:
    W, H = 320, 140
    j = A / "personajes" / "juego"
    out = r(0, 0, W, H, "#3D4A51") + r(0, 96, W, 44, "#4A5A63") + r(0, 96, W, 2, "#8196A0")
    for y in range(100, H, 6):
        out += r(0, y, W, 1, "#435159")
    out += r(40, 10, 170, 74, "#6A5A4A") + r(43, 13, 164, 68, "#2F3D3A") + r(40, 82, 170, 4, "#5C4A3A")  # pizarrón
    tiza = "#D8DFE2"
    pix = {"#": tiza}
    # en el gis: una gráfica de barras y un "árbol" de temas (se lee como clase sin texto)
    out += r(58, 24, 1, 40, tiza) + r(58, 63, 70, 1, tiza)
    for k, alto in enumerate((12, 20, 16, 30, 26)):
        out += r(64 + k * 12, 63 - alto, 7, alto, tiza, ' opacity="0.8"')
    out += r(150, 22, 14, 7, tiza) + r(156, 29, 1, 6, tiza) + r(140, 35, 34, 1, tiza)
    for bx in (136, 151, 166):
        out += r(bx + 4, 35, 1, 5, tiza) + r(bx, 40, 10, 6, tiza, ' opacity="0.8"')
    out += r(140, 56, 50, 1, tiza, ' opacity="0.5"') + r(140, 62, 36, 1, tiza, ' opacity="0.5"')
    out += r(180, 70, 8, 3, "#E6ECEE") + r(190, 71, 6, 2, "#BDC8CD")                  # gises
    filtro = ('<defs><filter id="suave"><feColorMatrix type="saturate" values="0.55"/></filter></defs>\n')
    maestro = f'<g filter="url(#suave)" transform="translate(222,60) scale(1.15)">{_sprite_interior(j / "owl-librarian.svg")}</g>\n'
    out += maestro + r(214, 60, 2, 30, "#5C4A3A")                                    # puntero
    alumnos = ["ogre-green.svg", "mushroom-sprout.svg", "imp-small.svg", "skeleton-small.svg", "druid.svg"]
    for k, nombre in enumerate(alumnos):
        x = 18 + k * 60
        out += f'<g filter="url(#suave)" transform="translate({x},80)">{_sprite_interior(j / nombre)}</g>\n'
        out += r(x - 6, 112, 44, 5, "#6A5A4A") + r(x - 6, 112, 44, 1, "#7A6A58") + r(x - 4, 117, 40, 18, "#5C4A3A")
        out += r(x - 4, 117, 1, 18, "#4A3A2E") + r(x + 35, 117, 1, 18, "#4A3A2E")
    guarda(A / "fondos" / "pixtart-aula" / "pixtart-aula-escena.svg",
           svg(W, H, out, "Proyectos · encabezado Pixtart: maestro búho y alumnos en clase", extra=filtro))


def fondo_nivel_final() -> None:
    W, H = 480, 180
    rng = random.Random(99)
    out = banda_cielo(W, ["#151B1F", "#1E2529", "#26303A", "#2D373C", "#3D4A51", "#4C5D66"], 0, 150)
    for _ in range(60):
        out += r(rng.randint(0, W), rng.randint(0, 90), 1, 1, "#E6ECEE", f' opacity="{rng.choice([0.4, 0.7, 1])}"')
    out += disco(290, 30, 11, "#E6ECEE") + disco(294, 27, 9, "#26303A")               # luna
    out += silueta(cresta(rng, W, 120, 18, 20), 160, "#26303A")
    cx = 360                                                                          # castillo
    out += r(cx, 70, 70, 80, "#1E2529") + r(cx + 26, 40, 18, 40, "#1E2529")
    for k in range(0, 70, 8):
        out += r(cx + k, 66, 5, 4, "#1E2529")
    out += r(cx + 34, 26, 1, 14, "#8196A0") + r(cx + 35, 26, 9, 5, P["oro"])          # bandera meta
    for wx, wy in ((cx + 10, 90), (cx + 50, 90), (cx + 32, 52), (cx + 30, 110)):
        out += r(wx, wy, 4, 6, P["oro_c"]) + r(wx, wy, 4, 1, P["oro_s"])
    out += silueta(cresta(rng, W, 140, 6, 30), 160, "#2D373C")
    # suelo de piedra con el MISMO patrón que la muestra azul-gris (tile-stone Aurora)
    for x in range(0, W, 16):
        for y in (148, 164):
            out += r(x, y, 16, 16, "#566972") + r(x, y, 16, 1, "#2D373C") + r(x, y + 1, 16, 1, "#8196A0")
            off = 0 if (y == 148) else 8
            out += r((x + off) % W, y, 1, 16, "#2D373C")
            out += r(x + 4, y + 6, 1, 1, "#2D373C") + r(x + 11, y + 9, 1, 1, "#8196A0")
    for px, py, L in ((60, 118, 48), (170, 104, 40), (270, 120, 48)):                 # plataformas
        out += r(px, py, L, 6, "#566972") + r(px, py, L, 1, "#8196A0") + r(px, py + 5, L, 1, "#2D373C")
    for tx in (30, 150, 250, 340):                                                    # antorchas
        out += r(tx, 132, 2, 16, "#3A2E26") + f'<g class="flama" style="--i:{tx}">' + \
            r(tx - 1, 127, 4, 5, P["oro"]) + r(tx, 125, 2, 3, P["oro_c"]) + "</g>\n"
    guarda(A / "fondos" / "nivel-final" / "nivel-final-carrera.svg",
           svg(W, H, out, "Carrera · nivel final: noche, castillo meta, plataformas y suelo de piedra azul-gris"))


# --------------------------------------------------------------------------------------
# 4. UI dorada estilo menú de videojuego + iconos 16x16
# --------------------------------------------------------------------------------------
def boton(estado: str) -> str:
    cuerpo, luz, sombra = {
        "normal": (P["oro"], P["oro_c"], P["oro_s"]),
        "hover": ("#E6B947", "#FBE49C", P["oro"]),
        "presionado": (P["oro_s"], P["oro"], "#7E5A14"),
    }[estado]
    W, H = 96, 24
    o = P["oro_o"]
    s = r(1, 0, W - 2, H, o) + r(0, 1, W, H - 2, o)
    s += r(1, 1, W - 2, H - 2, cuerpo)
    s += r(2, 2, W - 4, 2, luz) + r(2, 2, 2, H - 6, luz)
    s += r(2, H - 4, W - 4, 2, sombra) + r(W - 4, 4, 2, H - 6, sombra)
    if estado != "presionado":
        s += r(4, 4, 3, 1, "#FFF6D8")                                                  # destello
    return s


def nueve(cuerpo: str, luz: str, sombra: str, borde: str, extra: str = "") -> str:
    """Tile 24x24 para CSS border-image (slice 8): borde de 8 px y centro rellenable."""
    s = r(1, 0, 22, 24, borde) + r(0, 1, 24, 22, borde) + r(1, 1, 22, 22, cuerpo)
    s += r(2, 2, 20, 2, luz) + r(2, 2, 2, 18, luz) + r(2, 20, 20, 2, sombra) + r(20, 4, 2, 18, sombra)
    return s + extra


ICONOS = {
    "quien-soy": [
        "................",
        "......OOOO......",
        ".....OHHHHO.....",
        "....OHHHHHHO....",
        "....OSSSSSSO....",
        "....OSOSSOSO....",
        "....OSSSSSSO....",
        ".....OSmmSO.....",
        "......OSSO......",
        "....OOJCCJOO....",
        "...OJJJCCJJJO...",
        "..OJJJJTTJJJJO..",
        "..OJJJJTTJJJJO..",
        "..OJJJJJJJJJJO..",
        "..OOOOOOOOOOOO..",
        "................",
    ],
    "proyectos": [
        "................",
        "................",
        "...OOOOOOOOOO...",
        "..OWWWWWWWWWWO..",
        "..OWwwwwwwwwWO..",
        "..OWwwwwwwwwWO..",
        "..OOOOOGGOOOOO..",
        "..OWWWOGgOWWWO..",
        "..OWwwOOOOwwWO..",
        "..OWwwwwwwwwWO..",
        "..OWwwwwwwwwWO..",
        "..OWWWWWWWWWWO..",
        "..OOOOOOOOOOOO..",
        "................",
        "................",
        "................",
    ],
    "carrera": [
        "........OF......",
        "........OFFF....",
        "........OFFFF...",
        "........OFF.....",
        "........O.......",
        "...O.O..O.O.O...",
        "...OOOOOOOOOO...",
        "...OKKKKKKKKO...",
        "...OKKKGGKKKO...",
        "...OKKKGGKKKO...",
        "...OKKKKKKKKO...",
        "...OKKKOOKKKO...",
        "...OKKO..OKKO...",
        "...OKKO..OKKO...",
        "...OOOO..OOOO...",
        "................",
    ],
}
LEY_ICONO = {"O": P["contorno"], "H": "#E2C66E", "S": "#D9CBBE", "m": "#6E5555", "J": P["piedra"],
             "C": P["hueso"], "T": "#3F5566", "W": "#5C4A3A", "w": "#7A5C3E", "G": P["oro_c"],
             "g": P["oro_s"], "F": P["oro_c"], "K": P["piedra"]}


def ui() -> None:
    d = A / "ui"
    for est in ("normal", "hover", "presionado"):
        guarda(d / f"boton-dorado-{est}.svg", svg(96, 24, boton(est), f"Botón dorado de menú · {est}", escala=3))
    guarda(d / "boton-dorado-9slice.svg",
           svg(24, 24, nueve(P["oro"], P["oro_c"], P["oro_s"], P["oro_o"]), "Botón dorado · tile 9-slice (border-image-slice: 8)", escala=4))
    tornillos = r(4, 4, 2, 2, "#8B7A55") + r(18, 4, 2, 2, "#8B7A55") + r(4, 18, 2, 2, "#8B7A55") + r(18, 18, 2, 2, "#8B7A55")
    guarda(d / "placa-museo-9slice.svg",
           svg(24, 24, nueve("#ECE6D6", "#F7F3E8", "#CFC6AE", "#5C4A3A", tornillos), "Placa de museo (cédula) · 9-slice, slice 8", escala=4))
    adorno = r(3, 3, 2, 2, P["oro_c"]) + r(19, 3, 2, 2, P["oro_c"]) + r(3, 19, 2, 2, P["oro_c"]) + r(19, 19, 2, 2, P["oro_c"])
    guarda(d / "marco-cuadro-9slice.svg",
           svg(24, 24, nueve("#2D373C", P["oro_c"], P["oro_s"], P["oro_o"], adorno), "Marco dorado de cuadro · 9-slice, slice 8", escala=4))
    flecha = [
        "................",
        "....OO..........",
        "....OGO.........",
        "....OGGO........",
        "....OGGGO.......",
        "....OGGGGO......",
        "....OGGGGGO.....",
        "....OGGGGGGO....",
        "....OgggggggO...",
        "....OggggggO....",
        "....OgggggO.....",
        "....OggggO......",
        "....OgggO.......",
        "....OggO........",
        "....OO..........",
        "................",
    ]
    ley = {"O": P["oro_o"], "G": P["oro_c"], "g": P["oro"]}
    guarda(d / "flecha-dorada-derecha.svg", svg(16, 16, rejilla(flecha, ley), "Flecha dorada → (siguiente proyecto)", escala=4))
    guarda(d / "flecha-dorada-izquierda.svg",
           svg(16, 16, rejilla([f[::-1] for f in flecha], ley), "Flecha dorada ← (proyecto anterior)", escala=4))
    cursor = ["O.....", "OGO...", "OGGO..", "OgggO.", "OggO..", "OgO...", "O....."]
    guarda(d / "cursor-menu.svg", svg(6, 7, rejilla(cursor, ley), "Cursor ▶ del menú (opción seleccionada)", escala=4))
    for nombre, filas in ICONOS.items():
        guarda(d / "iconos" / f"icono-{nombre}.svg", svg(16, 16, rejilla(filas, LEY_ICONO), f"Ícono menú · {nombre}", escala=4))


def _escudo(x0: int, y0: int, ancho: int, alto: int) -> str:
    """Escudo dorado con cerradura (procedural, simétrico)."""
    out = ""
    mitad = ancho // 2
    for y in range(alto):
        k = y - int(alto * 0.55)
        m = mitad if k <= 0 else max(1, int(mitad * (1 - (k / (alto * 0.45)) ** 1.6)))
        cx = x0 + mitad
        out += r(cx - m, y0 + y, 2 * m, 1, P["oro_o"])
        if y in (0, alto - 1) or m < 3:
            continue
        out += r(cx - m + 1, y0 + y, 2 * m - 2, 1, P["oro"])
        if y > 1 and m > 4:
            out += r(cx - m + 3, y0 + y, 2 * m - 6, 1, P["piedra"])
            out += r(cx - m + 3, y0 + y, 2, 1, P["piedra_c"])
    cx, cy = x0 + mitad, y0 + alto // 2 - 2                                           # cerradura
    out += r(cx - 4, cy - 4, 8, 11, P["oro_c"]) + r(cx - 4, cy - 4, 8, 1, P["oro_s"])
    out += r(cx - 2, cy - 2, 4, 3, P["noche"]) + r(cx - 1, cy - 3, 2, 1, P["noche"])
    out += r(cx - 1, cy + 1, 2, 4, P["noche"])
    return out


def _candado(x0: int, y0: int, e: int = 1) -> str:
    """Candado 12x14 (escala entera e)."""
    filas = [
        "...OOOOOO...",
        "..OnnnnnnO..",
        ".OnO....OnO.",
        ".OnO....OnO.",
        ".OnO....OnO.",
        "OOOOOOOOOOOO",
        "OGGGGGGGGGGO",
        "OGgggOOgggGO",
        "OGgggOOgggGO",
        "OGggggOgggGO",
        "OGggggOgggGO",
        "OGggggggggGO",
        "OssssssssssO",
        "OOOOOOOOOOOO",
    ]
    ley = {"O": P["oro_o"], "n": P["niebla"], "G": P["oro_c"], "g": P["oro"], "s": P["oro_s"]}
    if e == 1:
        return rejilla(filas, ley, x0, y0)
    return f'<g transform="translate({x0},{y0}) scale({e})">{rejilla(filas, ley)}</g>\n'


def fondo_agnis() -> None:
    """Encabezado de Agnis: panel de control pixel-art (permisos, acciones críticas, flujo, reportes)."""
    W, H = 320, 140
    out = r(0, 0, W, H, P["acero"]) + r(0, 104, W, 36, "#4A5A63") + r(0, 104, W, 2, P["piedra_c"])
    for y in range(108, H, 6):
        out += r(0, y, W, 1, "#435159")
    for x in range(0, W, 16):                                                         # rejilla tenue en la pared
        out += r(x, 0, 1, 104, "#435159")
    out += r(14, 98, 292, 6, "#5C4A3A") + r(14, 98, 292, 1, "#7A5C3E")                # escritorio
    out += r(150, 92, 20, 6, P["pizarra"]) + r(156, 88, 8, 4, P["pizarra"])           # base del monitor
    out += r(66, 6, 188, 84, P["contorno"]) + r(68, 8, 184, 80, P["pizarra"])         # monitor
    out += r(72, 12, 176, 72, P["noche"])
    out += r(72, 12, 176, 7, P["acero"])                                              # barra de título
    for k, c in enumerate((P["piedra_c"], P["piedra"], P["piedra"])):
        out += r(76 + k * 6, 14, 3, 3, c)
    # columna izquierda: agentes con su nivel de permiso (barras)
    for k in range(4):
        y = 24 + k * 13
        out += rejilla(["OOOOOOO", "OnnnnnO", "OnknknO", "OnnnnnO", ".OOOOO."],
                       {"O": P["contorno"], "n": P["niebla"], "k": P["noche"]}, 78, y)
        out += r(80, y - 2, 1, 2, P["piedra_c"]) + r(79, y - 3, 3, 1, P["oro"] if k == 2 else P["piedra_c"])
        largo = (30, 18, 36, 12)[k]
        out += r(88, y + 1, 40, 3, P["acero"]) + r(88, y + 1, largo, 3, P["oro"] if k == 2 else P["piedra_c"])
    out += _escudo(146, 22, 28, 34)                                                   # escudo central
    # columna derecha: acciones (revisadas ✓ y una crítica ⚠ en dorado)
    palomita = ["......n", ".....n.", "n...n..", ".n.n...", "..n...."]
    for k in range(4):
        y = 24 + k * 13
        out += r(190, y - 1, 52, 9, P["pizarra"])
        if k == 1:
            out += rejilla(["...O...", "..OgO..", "..OgO..", ".OgOgO.", ".OgggO.", "OgggggO", "OOOOOOO"],
                           {"O": P["oro_o"], "g": P["oro_c"]}, 193, y)
            out += r(203, y + 2, 34, 3, P["oro"])
        else:
            out += rejilla(palomita, {"n": P["niebla"]}, 193, y + 1)
            out += r(203, y + 2, (30, 0, 24, 34)[k], 3, P["piedra"])
    # línea de tiempo: pasado (lleno) · ahora (dorado) · futuro (punteado)
    out += r(78, 76, 164, 1, P["acero"])
    for k in range(10):
        x = 80 + k * 16
        if k < 5:
            out += r(x, 73, 7, 7, P["piedra_c"])
        elif k == 5:
            out += r(x - 1, 72, 9, 9, P["oro_o"]) + r(x, 73, 7, 7, P["oro_c"])
        else:
            out += r(x, 73, 7, 1, P["piedra"]) + r(x, 79, 7, 1, P["piedra"]) + r(x, 73, 1, 7, P["piedra"]) + r(x + 6, 73, 1, 7, P["piedra"])
    # a los lados: candado (izquierda) y reporte impreso (derecha), en espejo
    out += _candado(26, 70, 2)
    out += r(270, 52, 30, 46, P["contorno"]) + r(271, 53, 28, 44, P["hueso"]) + r(271, 53, 28, 4, P["niebla"])
    for k in range(6):
        out += r(275, 61 + k * 5, (20, 16, 20, 12, 18, 10)[k], 2, P["piedra_c"])
    out += r(289, 86, 7, 7, P["oro_o"]) + r(290, 87, 5, 5, P["oro"])                   # sello
    guarda(A / "fondos" / "agnis" / "agnis-panel.svg",
           svg(W, H, out, "Proyectos · encabezado Agnis: panel de control de agentes con permisos, escudo y reporte"))


def cofres_partidos() -> None:
    """Hoja de 4 frames (128x32) por cofre para animar la apertura con steps():
    cerrado · entreabierto · a medio abrir · abierto (tapa vista por dentro detrás de la boca).
    Los originales chest-*.svg de Pixtart no se tocan."""
    d = A / "ui"
    patron = r'<rect x="(\d+)" y="(\d+)" width="(\d+)" height="(\d+)" fill="(#\w+)"\s*/>'
    estilos = {  # corte = primera fila de la base; colores de la cara interior de la tapa
        "chest-normal": (13, "#2A1A0E", "#C08A4A", "#5A3A1E", "#45291A"),
        "chest-legendary": (14, "#2A1A0E", "#F2A81D", "#5A3A1E", "#45291A"),
    }
    for nombre, (corte, contorno, borde, tabla, veta) in estilos.items():
        pix = {}
        for x, y, w, h, c in re.findall(patron, (d / f"{nombre}.svg").read_text(encoding="utf-8")):
            for k in range(int(w)):
                for m in range(int(h)):
                    pix[(int(x) + k, int(y) + m)] = c
        tapa = {k: v for k, v in pix.items() if k[1] < corte}
        base = {k: v for k, v in pix.items() if k[1] >= corte}
        arriba = min(y for _, y in tapa)
        izq = min(x for x, y in base if y == corte)
        der = max(x for x, y in base if y == corte)

        def pinta(cel: dict, dx: int) -> str:
            return "".join(r(x + dx, y, 1, 1, c) for (x, y), c in sorted(cel.items()))

        def boca(dx: int, alto: int) -> str:
            """Hueco oscuro con monedas que asoman (alto = cuántas filas se ven)."""
            out = r(izq + 1 + dx, corte - alto, der - izq - 1, alto, "#1A1208")
            for k, cx in enumerate(range(izq + 2, der - 2, 3)):
                h = min(alto, (2, 3, 2, 3, 2, 3, 2, 3)[k % 8])
                out += r(cx + dx, corte - h, 3, h, P["oro"]) + r(cx + dx, corte - h, 2, 1, P["oro_c"])
                out += r(cx + 2 + dx, corte - h + 1, 1, max(0, h - 1), P["oro_s"])
            return out

        def tapa_aplastada(dx: int, factor: float, sube: int) -> str:
            """Tapa inclinada hacia atrás: se reduce su alto (vecino más cercano) y se eleva."""
            alto = corte - arriba
            nuevo = max(2, round(alto * factor))
            out = ""
            for ny in range(nuevo):
                fy = arriba + min(alto - 1, int(ny / nuevo * alto))
                y = corte - sube - nuevo + ny
                for (x, yy), c in tapa.items():
                    if yy == fy:
                        out += r(x + dx, y, 1, 1, c)
            return out

        def tapa_abierta(dx: int) -> str:
            """Cara interior de la tapa, de pie detrás de la boca del cofre."""
            x0, x1, alto = izq + 1, der, 7
            y0 = corte - 2 - alto
            out = r(x0 + dx, y0, x1 - x0, alto, contorno)
            out += r(x0 + 1 + dx, y0 + 1, x1 - x0 - 2, alto - 2, borde)
            out += r(x0 + 2 + dx, y0 + 2, x1 - x0 - 4, alto - 3, tabla)
            for k in range(x0 + 6, x1 - 3, 6):
                out += r(k + dx, y0 + 2, 1, alto - 3, veta)
            return out

        cuadros = [
            pinta(pix, 0),                                                       # cerrado
            boca(32, 2) + pinta(base, 32) + tapa_aplastada(32, 1.0, 2),          # entreabierto
            boca(64, 3) + pinta(base, 64) + tapa_aplastada(64, .45, 3),  # a medio abrir
            tapa_abierta(96) + boca(96, 3) + pinta(base, 96),                    # abierto
        ]
        guarda(d / f"{nombre}-hoja.svg",
               svg(128, 32, "".join(cuadros), f"Cofre ({nombre}) · hoja de apertura: cerrado, entreabierto, medio, abierto", escala=4))
        for vieja in ("tapa", "base", "interior"):
            (d / f"{nombre}-{vieja}.svg").unlink(missing_ok=True)


def main() -> None:
    print("Generando arte en", RAIZ)
    personaje()
    mascotas()
    fondo_inicio()
    fondo_museo()
    fondo_aula()
    fondo_nivel_final()
    fondo_agnis()
    ui()
    cofres_partidos()


if __name__ == "__main__":
    main()
