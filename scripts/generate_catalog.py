#!/usr/bin/env python3
"""Genera el catálogo visual desde el contrato estructurado de presets."""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path


from validate_contract import load_catalog
from preset_assets import font_stylesheets, preview_tokens

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "references" / "presets.json"
OUTPUT = ROOT / "assets" / "preset-catalog.html"
SURFACES = ("console", "gallery", "dashboard", "presentation")


def load_contract() -> dict:
    return {'presets': list(load_catalog(SOURCE).values())}


def build_options(presets: list[dict]) -> str:
    rows = []
    for preset in presets:
        rows.append(
            f"""\
        <button class="preset-option" type="button"
                data-preset-id="{html.escape(preset["id"])}"
                aria-pressed="false">
          <span class="preset-index">{preset["n"]:02d}</span>
          <span>
            <strong>{html.escape(preset["name"])}</strong>
            <small>{html.escape(preset["estado"])}</small>
          </span>
          <i aria-hidden="true"></i>
        </button>"""
        )
    return "\n".join(rows)


def render_catalog(contract: dict) -> str:
    presets = [dict(preset, stylesheets=font_stylesheets(preset), preview=preview_tokens(preset))
               for preset in contract["presets"]]
    encoded = json.dumps(presets, ensure_ascii=False, separators=(",", ":"))
    encoded = encoded.replace("</", "<\\/")
    options = build_options(presets)
    surface_buttons = "\n".join(
        f"""\
          <button type="button" data-surface-option="{surface}"
                  aria-pressed="{'true' if surface == 'console' else 'false'}">
            {surface.capitalize()}
          </button>"""
        for surface in SURFACES
    )
    return f"""\
<!doctype html>
<html lang="es" data-preset="01-bold-signal" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>adri-style v5.8 · Catálogo contractual</title>
  <link rel="preconnect" href="https://api.fontshare.com">
  <link href="https://api.fontshare.com/v2/css?f[]=satoshi@500,700,900&display=swap"
        rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap"
        rel="stylesheet">
  <style>
    *,*::before,*::after{{box-sizing:border-box}}
    :root{{
      color-scheme:dark;
      --shell:#0b0b0c;--panel:#121214;--line:#29292d;
      --muted:#92929c;--text:#f4f4f5;--focus:#9ad5ff;
      --preview-bg:#f8f8f8;--preview-accent:#0a0a0a;
      --preview-text:#101014;--display:"Satoshi",sans-serif;
      --body:"Inter",sans-serif
    }}
    html,body{{margin:0;min-height:100%;background:var(--shell);color:var(--text)}}
    body{{font-family:"Inter",sans-serif}}
    button{{font:inherit}}
    button:focus-visible{{outline:2px solid var(--focus);outline-offset:2px}}
    .app{{display:grid;grid-template-columns:320px minmax(0,1fr);min-height:100dvh}}
    .sidebar{{border-right:1px solid var(--line);padding:28px 20px;overflow:auto}}
    .brand{{padding:0 8px 22px;border-bottom:1px solid var(--line)}}
    .brand strong{{display:block;font:900 1.35rem/1 "Satoshi",sans-serif}}
    .brand span{{display:block;margin-top:8px;color:var(--muted);font-size:.76rem}}
    .preset-list{{display:grid;gap:3px;margin-top:16px}}
    .preset-option{{
      appearance:none;border:0;background:transparent;color:var(--text);
      display:grid;grid-template-columns:34px 1fr 8px;gap:10px;align-items:center;
      width:100%;padding:10px 8px;text-align:left;border-radius:7px;cursor:pointer
    }}
    .preset-option:hover{{background:#19191c}}
    .preset-option[aria-pressed="true"]{{background:#222226}}
    .preset-option i{{width:7px;height:7px;border-radius:50%;background:var(--swatch,#888)}}
    .preset-index{{color:var(--muted);font:500 .68rem/1 "Inter",sans-serif}}
    .preset-option strong{{display:block;font-size:.81rem;font-weight:500}}
    .preset-option small{{display:block;margin-top:3px;color:var(--muted);font-size:.64rem}}
    main{{min-width:0;padding:28px clamp(20px,4vw,64px) 48px}}
    .topbar{{display:flex;justify-content:space-between;align-items:flex-start;gap:24px}}
    .topbar h1{{margin:0;font:900 clamp(2rem,4vw,4.5rem)/.92 "Satoshi",sans-serif;letter-spacing:-.055em}}
    .topbar p{{max-width:58ch;margin:12px 0 0;color:var(--muted);font-size:.84rem;line-height:1.55}}
    .mode{{color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.12em}}
    .controls{{display:flex;flex-wrap:wrap;gap:8px;margin:30px 0 16px}}
    .controls button,.compare-action{{
      border:1px solid var(--line);background:var(--panel);color:var(--muted);
      padding:8px 12px;border-radius:999px;cursor:pointer;font-size:.75rem
    }}
    .controls button[aria-pressed="true"]{{background:var(--text);color:var(--shell);border-color:var(--text)}}
    .preview{{
      min-height:540px;background:var(--preview-bg);background-image:var(--preview-background-image,none);color:var(--preview-text);
      border-radius:14px;overflow:hidden;box-shadow:0 24px 80px #0008;
      font-family:var(--body);font-weight:var(--body-weight)
    }}
    .preview-header{{
      display:flex;align-items:center;justify-content:space-between;padding:17px 22px;
      border-bottom:1px solid color-mix(in srgb,var(--preview-text) 15%,transparent)
    }}
    .preview-header strong{{font-family:var(--display);font-weight:var(--display-weight)}}
    .preview-header span{{font-size:.7rem;opacity:.62}}
    .surface{{min-height:476px}}

    .console-shell{{display:grid;grid-template-columns:180px 1fr;min-height:476px}}
    .console-nav{{padding:22px;border-right:1px solid color-mix(in srgb,var(--preview-text) 15%,transparent)}}
    .console-nav b{{display:block;margin-bottom:24px;font:var(--display-weight) 1rem/1 var(--display)}}
    .console-nav span{{display:block;padding:7px 0;font-size:.72rem;opacity:.62}}
    .console-main{{padding:30px}}
    .console-main h2,.gallery-copy h2,.dashboard-head h2,.slide-stage h2{{
      margin:0;font-family:var(--display);font-weight:var(--display-weight);letter-spacing:-.035em
    }}
    .log{{display:grid;grid-template-columns:70px 1fr auto;gap:16px;padding:14px 0;border-bottom:1px solid color-mix(in srgb,var(--preview-text) 12%,transparent);font-size:.74rem}}
    .log em{{color:var(--preview-accent-ink);font-style:normal;font-weight:var(--body-weight)}}
    .media-stream{{display:grid;grid-template-columns:1.2fr .8fr;min-height:476px}}
    .media-art{{background:color-mix(in srgb,var(--preview-accent) 26%,var(--preview-bg));display:grid;place-items:center}}
    .media-art svg{{width:46%;max-width:180px;color:var(--preview-accent)}}
    .gallery-copy{{padding:clamp(28px,5vw,70px);align-self:end}}
    .gallery-copy p{{max-width:38ch;line-height:1.6;opacity:.68}}
    .metric-grid{{padding:30px}}
    .dashboard-head{{display:flex;justify-content:space-between;gap:24px;align-items:end}}
    .dashboard-head p{{margin:0;font-size:.72rem;opacity:.62}}
    .metrics{{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:28px;background:color-mix(in srgb,var(--preview-text) 14%,transparent)}}
    .metric{{padding:24px;background:var(--preview-bg)}}
    .metric strong{{display:block;font:var(--display-weight) 2.1rem/1 var(--display)}}
    .metric span{{font-size:.7rem;opacity:.62}}
    .chart{{height:180px;margin-top:28px;border-left:1px solid currentColor;border-bottom:1px solid currentColor;display:flex;align-items:end;gap:6%;padding:0 5%}}
    .chart i{{display:block;width:14%;height:var(--h);background:var(--preview-accent)}}
    .slide-stage{{min-height:476px;display:grid;grid-template-columns:1fr auto;align-items:center;padding:clamp(32px,7vw,90px)}}
    .slide-stage h2{{font-size:clamp(3rem,8vw,7rem);line-height:.86;max-width:8ch}}
    .slide-stage p{{max-width:26ch;line-height:1.55;opacity:.66}}
    .slide-count{{align-self:end;font:var(--body-weight) .72rem/1 var(--body)}}
    .surface:not(.is-active){{display:none}}
    .details{{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:start;margin-top:20px}}
    .details h2{{margin:0;font:700 1.15rem/1.1 "Satoshi",sans-serif}}
    .details p{{margin:7px 0 0;color:var(--muted);font-size:.76rem}}
    .compare-action[aria-pressed="true"]{{border-color:var(--focus);color:var(--focus)}}
    .compare-tray{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px}}
    .compare-card{{border:1px solid var(--line);border-top:4px solid var(--swatch);padding:14px;background:var(--panel);border-radius:8px}}
    .compare-card strong{{display:block;font-size:.78rem}}
    .compare-card span{{display:block;margin-top:5px;color:var(--muted);font-size:.67rem}}
    @media (max-width:820px){{
      .app{{grid-template-columns:1fr}}.sidebar{{border-right:0;border-bottom:1px solid var(--line);max-height:290px}}
      .topbar{{display:block}}.mode{{margin-top:12px}}.media-stream{{grid-template-columns:1fr}}.media-art{{min-height:220px}}
      .console-shell{{grid-template-columns:120px 1fr}}.compare-tray{{grid-template-columns:1fr}}
    }}
    .preview{{overflow-wrap:anywhere}}
    .preview-header{{gap:16px;flex-wrap:wrap}}
    .preview-header span{{opacity:1;color:var(--preview-text)}}
    .console-main,.gallery-copy,.metric-grid,.slide-stage{{min-width:0}}
    .log{{grid-template-columns:48px minmax(0,1fr) auto;gap:12px}}
    .log b{{font-weight:inherit}}
    .metric{{min-width:0;padding:20px 12px;font-variant-numeric:tabular-nums}}
    .details p{{line-height:1.5}}
    #font-status{{font-size:.75rem;color:var(--muted);min-height:1.5em}}
    @media (max-width:540px){{
      .console-shell{{grid-template-columns:1fr}}.console-nav{{display:none}}
      .console-main,.metric-grid{{padding:22px 16px}}
      .dashboard-head{{display:block}}.metrics{{grid-template-columns:1fr}}
      .details{{grid-template-columns:1fr}}.slide-stage{{grid-template-columns:1fr;padding:28px}}
      .slide-stage h2{{font-size:clamp(2.4rem,11vw,4rem);line-height:1}}
      .gallery-copy{{padding:26px}}.slide-count{{margin-top:20px}}
    }}
    @media print{{
      :root{{--shell:#fff;--text:#111;--muted:#444;--line:#bbb;--panel:#fff}}
      .app{{display:block}}.sidebar,.controls,.compare-action,#font-status{{display:none}}
      main{{padding:0}}.topbar h1{{font-size:26pt;line-height:1.1}}
      .preview{{box-shadow:none;border:1px solid #bbb;border-radius:0;min-height:0}}
      .preview,.preview *{{background:transparent!important;color:#111!important}}
      .chart i{{background:#444!important}}
      .surface{{min-height:0;break-inside:avoid}}.slide-stage h2{{font-size:40pt;line-height:1}}
      .preview-header,.details{{break-inside:avoid}}.media-art{{min-height:120px}}
      .compare-tray{{display:none}}
    }}
    @media (prefers-reduced-motion:reduce){{*,*::before,*::after{{scroll-behavior:auto!important;transition:none!important}}}}
  </style>
</head>
<body>
  <div class="app">
    <aside class="sidebar" aria-label="Presets disponibles">
      <div class="brand">
        <strong>adri-style v5.8</strong>
        <span>{len(presets)} contratos · fuente: presets.json</span>
      </div>
      <nav class="preset-list">
{options}
      </nav>
    </aside>
    <main>
      <header class="topbar">
        <div>
          <h1>Un preset.<br>Cuatro gramáticas.</h1>
          <p>El preset fija identidad; la superficie decide densidad, jerarquía y comportamiento. Esta vista contractual no sustituye los ejemplos completos de cada preset.</p>
        </div>
        <span class="mode" id="mode-label">Modo light</span>
      </header>
      <div class="controls" role="group" aria-label="Superficie de prueba">
{surface_buttons}
      </div>
      <article class="preview" id="preview" data-preset="01-bold-signal" data-theme="light">
        <header class="preview-header">
          <strong id="preview-name">Bold Signal</strong>
          <span id="preview-contract">Satoshi / Inter</span>
        </header>
        <section class="surface console-shell is-active" data-surface="console">
          <nav class="console-nav"><b>Adri Console</b><span>Overview</span><span>Audits</span><span>Systems</span></nav>
          <div class="console-main"><h2>Contract checks</h2><div class="log"><span>09:42</span><b>Preset contract</b><em>PASS</em></div><div class="log"><span>09:43</span><b>Surface grammar</b><em>PASS</em></div><div class="log"><span>09:44</span><b>Font coherence</b><em>PASS</em></div></div>
        </section>
        <section class="surface media-stream" data-surface="gallery">
          <div class="media-art"><svg viewBox="0 0 120 120" fill="none" aria-hidden="true"><path d="M20 89 47 59l18 18 13-14 22 26H20Z" stroke="currentColor" stroke-width="5"/><circle cx="76" cy="37" r="10" stroke="currentColor" stroke-width="5"/></svg></div>
          <div class="gallery-copy"><h2>Referencias que conservan contexto</h2><p>Una galería prioriza ritmo visual y procedencia. No hereda la densidad operativa de Console.</p></div>
        </section>
        <section class="surface metric-grid" data-surface="dashboard">
          <div class="dashboard-head"><div><h2>Auditoría PRO-211</h2><p>Contrato estructurado</p></div><p>18 JUL 2026</p></div>
          <div class="metrics"><div class="metric"><strong>{len(presets)}</strong><span>presets válidos</span></div><div class="metric"><strong>4</strong><span>superficies</span></div><div class="metric"><strong>0</strong><span>reglas decorativas</span></div></div>
          <div class="chart" aria-label="Cobertura creciente: 25, 25, 26, {len(presets)}"><i style="--h:58%"></i><i style="--h:58%"></i><i style="--h:72%"></i><i style="--h:92%"></i></div>
        </section>
        <section class="surface slide-stage" data-surface="presentation">
          <div><h2>Identidad no es plantilla.</h2><p>La presentación amplifica una idea. El dashboard compara datos. El preset puede ser el mismo.</p></div><span class="slide-count">01 / 04</span>
        </section>
      </article>
      <p id="font-status" role="status" aria-live="polite"></p>
      <div class="details">
        <div><h2 id="detail-name">01 · Bold Signal</h2><p id="detail-meta">activo · light · Satoshi / Inter</p></div>
        <button class="compare-action" type="button" id="compare-action" aria-pressed="false">Añadir a comparación</button>
      </div>
      <div class="compare-tray" id="compare-tray" aria-live="polite"></div>
    </main>
  </div>
  <script type="application/json" id="preset-data">{encoded}</script>
  <script>
    (() => {{
      "use strict";
      const presets = JSON.parse(document.querySelector("#preset-data").textContent);
      const byId = new Map(presets.map((preset) => [preset.id, preset]));
      const options = [...document.querySelectorAll(".preset-option")];
      const surfaces = [...document.querySelectorAll("[data-surface-option]")];
      const compare = [];
      let selected = presets[0];

      const loadedStyles = new Map();
      let fontRequest = 0;
      async function loadFonts(preset) {{
        const request = ++fontRequest;
        const status = document.querySelector("#font-status");
        status.textContent = "Cargando tipografías…";
        try {{
          await Promise.all(preset.stylesheets.map((url) => {{
            if (!loadedStyles.has(url)) {{
              loadedStyles.set(url, new Promise((resolve, reject) => {{
                const link = document.createElement("link");
                link.rel = "stylesheet"; link.href = url; link.dataset.presetFont = "";
                link.onload = resolve; link.onerror = () => reject(new Error("stylesheet"));
                document.head.append(link);
              }}));
            }}
            return loadedStyles.get(url);
          }}));
          const faces = await Promise.all(["display", "body"].map((role) =>
            document.fonts.load(`${{preset.preview[role + "_weight"]}} 16px "${{preset.fonts[role]}}"`)));
          if (faces.some((family) => family.length === 0)) throw new Error("font missing");
          if (request === fontRequest) status.textContent = "Tipografías cargadas";
        }} catch (error) {{
          if (request === fontRequest) status.textContent = "Fuentes externas no disponibles; vista con fuentes de reserva.";
        }}
      }}

      function renderPreset(preset) {{
        selected = preset;
        const root = document.documentElement;
        root.style.setProperty("--preview-bg", preset.color.bg);
        root.style.setProperty("--preview-background-image", preset.color.background_image || "none");
        root.style.setProperty("--preview-accent", preset.color.accent);
        root.style.setProperty("--preview-text", preset.preview.text);
        root.style.setProperty("--preview-accent-ink", preset.preview.accent_ink);
        root.style.setProperty("--display-weight", preset.preview.display_weight);
        root.style.setProperty("--body-weight", preset.preview.body_weight);
        document.querySelector("#preview").dataset.preset = preset.id;
        document.querySelector("#preview").dataset.theme = preset.mode_default;
        loadFonts(preset);
        root.style.setProperty("--display", JSON.stringify(preset.fonts.display) + ", sans-serif");
        root.style.setProperty("--body", JSON.stringify(preset.fonts.body) + ", sans-serif");
        document.querySelector("#preview-name").textContent = preset.name;
        document.querySelector("#preview-contract").textContent = `${{preset.fonts.display}} / ${{preset.fonts.body}}`;
        document.querySelector("#detail-name").textContent = `${{String(preset.n).padStart(2, "0")}} · ${{preset.name}}`;
        document.querySelector("#detail-meta").textContent = `${{preset.estado}} · ${{preset.mode_default}} · ${{preset.fonts.display}} / ${{preset.fonts.body}}`;
        document.querySelector("#mode-label").textContent = `Modo ${{preset.mode_default}}`;
        options.forEach((option) => {{
          option.setAttribute("aria-pressed", String(option.dataset.presetId === preset.id));
          option.style.setProperty("--swatch", byId.get(option.dataset.presetId).color.accent);
        }});
        const active = compare.some((item) => item.id === preset.id);
        document.querySelector("#compare-action").setAttribute("aria-pressed", String(active));
        document.querySelector("#compare-action").textContent = active ? "Quitar de comparación" : "Añadir a comparación";
      }}

      function renderCompare() {{
        const cards = compare.map((preset) => {{
          const card = document.createElement("div");
          card.className = "compare-card";
          card.style.setProperty("--swatch", preset.color.accent);
          const title = document.createElement("strong");
          title.textContent = `${{String(preset.n).padStart(2, "0")}} · ${{preset.name}}`;
          const meta = document.createElement("span");
          meta.textContent = `${{preset.mode_default}} · ${{preset.fonts.display}} / ${{preset.fonts.body}}`;
          card.append(title, meta);
          return card;
        }});
        document.querySelector("#compare-tray").replaceChildren(...cards);
      }}

      options.forEach((option) => option.addEventListener("click", () => renderPreset(byId.get(option.dataset.presetId))));
      surfaces.forEach((button) => button.addEventListener("click", () => {{
        surfaces.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
        document.querySelectorAll(".surface").forEach((surface) => surface.classList.toggle("is-active", surface.dataset.surface === button.dataset.surfaceOption));
      }}));
      document.querySelector("#compare-action").addEventListener("click", () => {{
        const index = compare.findIndex((item) => item.id === selected.id);
        if (index >= 0) compare.splice(index, 1);
        else if (compare.length < 3) compare.push(selected);
        else compare.splice(0, 1, selected);
        renderCompare();
        renderPreset(selected);
      }});
      renderPreset(selected);
    }})();
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Comprueba que el catálogo versionado coincide con el generado.",
    )
    args = parser.parse_args()
    try:
        generated = render_catalog(load_contract())
        if args.check:
            current = OUTPUT.read_text(encoding="utf-8")
            if current != generated:
                print("CATALOG_OUT_OF_DATE")
                return 1
            print("CATALOG_OK")
            return 0
        OUTPUT.write_text(generated, encoding="utf-8")
        print(f"CATALOG_WRITTEN {OUTPUT}")
        return 0
    except (OSError, RuntimeError) as exc:
        print(f"CATALOG_ERROR {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
