"""One-shot generator for VOID profile SVG assets. Not shipped as a product."""

from pathlib import Path

OUT = Path(__file__).parent

DARK = {
    "mode": "dark",
    "bg": "#07090E",
    "bg2": "#0C1118",
    "card": "#0C1118",
    "border": "#1B2430",
    "hair": "#3EC8FF",
    "text": "#F2F5F8",
    "muted": "#8B98A8",
    "accent": "#3EC8FF",
    "accent2": "#7A5CFF",
    "pill": "#151C27",
    "pill_text": "#C5D0DC",
    "grid": "0.14",
    "glow_c": "0.28",
    "glow_v": "0.22",
    "scan": "0.12",
}

LIGHT = {
    "mode": "light",
    "bg": "#F4F6F9",
    "bg2": "#FFFFFF",
    "card": "#FFFFFF",
    "border": "#D5DCE6",
    "hair": "#0A7ABF",
    "text": "#0E141D",
    "muted": "#5C6B7A",
    "accent": "#0A7ABF",
    "accent2": "#5B3FD4",
    "pill": "#EEF2F7",
    "pill_text": "#334155",
    "grid": "0.18",
    "glow_c": "0.16",
    "glow_v": "0.10",
    "scan": "0.08",
}


def hero(t: dict) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-label="VOID">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{t['bg']}"/>
      <stop offset="55%" stop-color="{t['bg2']}"/>
      <stop offset="100%" stop-color="{t['bg']}"/>
    </linearGradient>
    <linearGradient id="hair" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['accent']}" stop-opacity="0"/>
      <stop offset="35%" stop-color="{t['accent']}"/>
      <stop offset="70%" stop-color="{t['accent2']}"/>
      <stop offset="100%" stop-color="{t['accent2']}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="word" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['text']}"/>
      <stop offset="100%" stop-color="{t['muted']}"/>
    </linearGradient>
    <radialGradient id="gc" cx="18%" cy="42%" r="46%">
      <stop offset="0%" stop-color="{t['accent']}" stop-opacity="{t['glow_c']}"/>
      <stop offset="100%" stop-color="{t['accent']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="gv" cx="90%" cy="28%" r="38%">
      <stop offset="0%" stop-color="{t['accent2']}" stop-opacity="{t['glow_v']}"/>
      <stop offset="100%" stop-color="{t['accent2']}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.2" cy="1.2" r="0.8" fill="{t['accent']}" opacity="{t['grid']}"/>
    </pattern>
    <filter id="blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10"/>
    </filter>
    <style>
      .pulse {{ animation: pulse 4.5s ease-in-out infinite; }}
      .scan {{ animation: scan 9s ease-in-out infinite; }}
      @keyframes pulse {{ 0%,100% {{ opacity: .45; }} 50% {{ opacity: 1; }} }}
      @keyframes scan {{ 0% {{ transform: translateY(0); opacity: 0; }} 12% {{ opacity: {t['scan']}; }} 88% {{ opacity: {t['scan']}; }} 100% {{ transform: translateY(320px); opacity: 0; }} }}
      @media (prefers-reduced-motion: reduce) {{
        .pulse, .scan {{ animation: none; }}
      }}
    </style>
  </defs>

  <rect width="1200" height="320" rx="20" fill="url(#bg)"/>
  <rect width="1200" height="320" rx="20" fill="url(#dots)"/>
  <rect width="1200" height="320" rx="20" fill="url(#gc)"/>
  <rect width="1200" height="320" rx="20" fill="url(#gv)"/>
  <rect x="1" y="1" width="1198" height="318" rx="19" fill="none" stroke="{t['border']}"/>
  <rect x="80" y="0" width="520" height="2" fill="url(#hair)"/>
  <rect class="scan" x="1" y="0" width="1198" height="2" fill="{t['accent']}"/>

  <text x="72" y="64" fill="{t['accent']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="12" font-weight="600" letter-spacing="4.5">JAMES  ·  SOUTH AFRICA</text>

  <text x="70" y="168" fill="{t['accent']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="92" font-weight="800" letter-spacing="22" opacity="0.28" filter="url(#blur)">VOID</text>
  <text x="72" y="166" fill="url(#word)" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="92" font-weight="800" letter-spacing="22">VOID</text>

  <rect x="72" y="194" width="72" height="2" rx="1" fill="{t['accent']}"/>

  <text x="72" y="232" fill="{t['muted']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="16" letter-spacing="3.2">BUILDER  ·  OPERATOR  ·  EDITOR</text>
  <text x="72" y="268" fill="{t['text']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="15">Websites. Tools. Homelab. Motion. Games.</text>

  <!-- VOID mark -->
  <g transform="translate(1048 160)">
    <circle r="92" fill="none" stroke="{t['border']}" stroke-width="1"/>
    <circle r="74" fill="none" stroke="{t['accent']}" stroke-width="1.25" stroke-dasharray="6 14" opacity="0.7">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="22s" repeatCount="indefinite"/>
    </circle>
    <circle r="48" fill="none" stroke="{t['text']}" stroke-width="2" opacity="0.88"/>
    <circle r="48" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="151 151" stroke-dashoffset="40" opacity="0.95"/>
    <circle r="22" fill="{t['bg']}" stroke="{t['accent2']}" stroke-width="1.5"/>
    <circle class="pulse" r="5" fill="{t['accent']}"/>
  </g>
</svg>
'''


def divider(t: dict) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="28" viewBox="0 0 1200 28" role="img" aria-hidden="true">
  <defs>
    <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['accent']}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{t['accent']}" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="{t['accent2']}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="40" y="13" width="1120" height="1" fill="url(#line)"/>
  <rect x="592" y="8" width="16" height="12" rx="1" transform="rotate(45 600 14)" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1"/>
</svg>
'''


def now(t: dict) -> str:
    items = [
        ("01", "VERTEXWEB", "Shipping high-converting sites for SA businesses."),
        ("02", "ULTA GUIDE", "Building a Windows utility that earns its keep."),
        ("03", "MOTION + LAB", "Cutting video. Running Docker on Ubuntu Server."),
    ]
    blocks = []
    for i, (num, title, body) in enumerate(items):
        x = 36 + i * 388
        blocks.append(f'''
  <g transform="translate({x} 36)">
    <text fill="{t['accent']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="11" font-weight="700" letter-spacing="3">{num}</text>
    <text y="32" fill="{t['text']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="18" font-weight="700" letter-spacing="1.4">{title}</text>
    <text y="60" fill="{t['muted']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="13">{body}</text>
  </g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="140" viewBox="0 0 1200 140" role="img" aria-label="Currently building">
  <rect width="1200" height="140" rx="16" fill="{t['card']}" stroke="{t['border']}"/>
  <rect x="80" y="0" width="280" height="2" fill="{t['accent']}" opacity="0.85"/>
  {''.join(blocks)}
</svg>
'''


def card(t: dict, eyebrow: str, title: str, body: str, tags: list[str]) -> str:
    pills = []
    x = 28
    for tag in tags:
        w = 18 + len(tag) * 7.2
        pills.append(f'''
    <g transform="translate({x:.0f} 158)">
      <rect width="{w:.0f}" height="26" rx="13" fill="{t['pill']}" stroke="{t['border']}"/>
      <text x="{w/2:.1f}" y="17" text-anchor="middle" fill="{t['pill_text']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="11">{tag}</text>
    </g>''')
        x += w + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="380" height="210" viewBox="0 0 380 210" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="top" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['accent']}"/>
      <stop offset="100%" stop-color="{t['accent2']}"/>
    </linearGradient>
  </defs>
  <rect width="380" height="210" rx="16" fill="{t['card']}" stroke="{t['border']}"/>
  <rect x="24" y="0" width="96" height="2" fill="url(#top)"/>
  <text x="28" y="42" fill="{t['accent']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="11" font-weight="700" letter-spacing="3.2">{eyebrow}</text>
  <text x="28" y="82" fill="{t['text']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="26" font-weight="800">{title}</text>
  <text x="28" y="116" fill="{t['muted']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="13">{body[0]}</text>
  <text x="28" y="136" fill="{t['muted']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="13">{body[1]}</text>
  {''.join(pills)}
</svg>
'''


def footer(t: dict) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="72" viewBox="0 0 1200 72" role="img" aria-label="VOID footer">
  <rect width="1200" height="72" rx="16" fill="{t['card']}" stroke="{t['border']}"/>
  <text x="600" y="32" text-anchor="middle" fill="{t['text']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="13" font-weight="700" letter-spacing="8">VOID</text>
  <text x="600" y="52" text-anchor="middle" fill="{t['muted']}" font-family="Segoe UI, Helvetica Neue, Arial, sans-serif" font-size="11" letter-spacing="2.4">build  ·  host  ·  cut  ·  ship</text>
</svg>
'''


CARDS = {
    "vertex": ("PRODUCT", "VertexWeb", ("Sites, hosting, and ops for", "South African businesses."), ["Next.js", "Cloudflare", "PayFast"]),
    "ulta": ("TOOL", "Ulta Guide", ("A Windows utility built to be", "useful, not another tray icon."), ["Windows", "Desktop", "Utility"]),
    "lab": ("LAB", "Homelab", ("Ubuntu Server, Docker, Portainer.", "Self-hosted and always on."), ["Docker", "Ubuntu", "Linux"]),
}


def write_all():
    for t in (DARK, LIGHT):
        m = t["mode"]
        (OUT / f"hero-{m}.svg").write_text(hero(t), encoding="utf-8")
        (OUT / f"divider-{m}.svg").write_text(divider(t), encoding="utf-8")
        (OUT / f"now-{m}.svg").write_text(now(t), encoding="utf-8")
        (OUT / f"footer-{m}.svg").write_text(footer(t), encoding="utf-8")
        for key, (eyebrow, title, body, tags) in CARDS.items():
            (OUT / f"card-{key}-{m}.svg").write_text(card(t, eyebrow, title, body, tags), encoding="utf-8")
    print("wrote", len(list(OUT.glob("*.svg"))), "svgs")


if __name__ == "__main__":
    write_all()
