#!/usr/bin/env python3
"""Baut die Seiten „Wagenpaten – Volksfestumzug der Schulen“.
Startseite: index.html (Vorstellung der Wagenpaten).
Homepage: start.html, festzug.html, ueber-uns.html, impressum.html, datenschutz.html.
Entwicklung (nie auf main): Menü „/ Entwicklung /“ in entwicklung/menu.js, eingebunden in Blöcken ENTWICKLUNG:START/END.
Inhalte (Wagenliste) stehen hier; Gestaltung in assets/vofe.css."""
from pathlib import Path
import re
Z = Path(__file__).resolve().parent.parent

SYMBOLE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="v-horaff" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff400"/>
 <g transform="translate(28 27)" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#1a1817" stroke-width="15"/><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#fff" stroke-width="8.5"/></g>
 <text x="60" y="99" text-anchor="middle" font-family="Poppins, sans-serif" font-size="11" font-weight="700" letter-spacing="1.5" fill="#1a1817">2027</text></symbol>
<symbol id="v-herz" viewBox="-6 -10 252 252">
 <path d="M98 70C94 30 108 4 120 4s26 26 22 66" fill="none" stroke="#8a5428" stroke-width="12" stroke-linecap="round"/>
 <path d="M98 70C94 30 108 4 120 4s26 26 22 66" fill="none" stroke="#fff400" stroke-width="7" stroke-linecap="round"/>
 <path d="M120 214C60 170 14 128 14 80 14 46 40 22 72 22c22 0 38 12 48 28 10-16 26-28 48-28 32 0 58 24 58 58 0 48-46 90-106 134z" fill="rgba(110,64,28,.22)" transform="translate(0 6)"/>
 <path d="M120 214C60 170 14 128 14 80 14 46 40 22 72 22c22 0 38 12 48 28 10-16 26-28 48-28 32 0 58 24 58 58 0 48-46 90-106 134z" fill="#cf8c4e" stroke="#a9682f" stroke-width="3"/>
 <path d="M120 214C60 170 14 128 14 80 14 46 40 22 72 22c22 0 38 12 48 28 10-16 26-28 48-28 32 0 58 24 58 58 0 48-46 90-106 134z" fill="#dba06a" transform="translate(120 112) scale(0.9) translate(-120 -112)"/>
 <path d="M120 214C60 170 14 128 14 80 14 46 40 22 72 22c22 0 38 12 48 28 10-16 26-28 48-28 32 0 58 24 58 58 0 48-46 90-106 134z" fill="none" stroke="#fff" stroke-width="7.5" stroke-linecap="round" stroke-dasharray="0 1.5625" pathLength="100" transform="translate(120 112) scale(0.86) translate(-120 -112)"/>
 <path d="M120 214C60 170 14 128 14 80 14 46 40 22 72 22c22 0 38 12 48 28 10-16 26-28 48-28 32 0 58 24 58 58 0 48-46 90-106 134z" fill="none" stroke="#C51F5D" stroke-width="3.6" stroke-linecap="round" stroke-dasharray="0 2" pathLength="100" transform="translate(120 112) scale(0.76) translate(-120 -112)"/>
 <path transform="translate(52 82) rotate(-30)" d="M0 0c3-4 8-4 11 0-3 4-8 4-11 0z" fill="#fff"/><path transform="translate(48 70) rotate(40)" d="M0 0c3-4 8-4 11 0-3 4-8 4-11 0z" fill="#fff"/><g transform="translate(62 72)"><g fill="#C51F5D"><circle cx="0.0" cy="-6.3" r="3.6"/><circle cx="6.0" cy="-1.9" r="3.6"/><circle cx="3.7" cy="5.1" r="3.6"/><circle cx="-3.7" cy="5.1" r="3.6"/><circle cx="-6.0" cy="-1.9" r="3.6"/></g><circle r="2.7" fill="#fff400"/></g>
 <path transform="translate(188 82) rotate(210)" d="M0 0c3-4 8-4 11 0-3 4-8 4-11 0z" fill="#fff"/><path transform="translate(192 70) rotate(140)" d="M0 0c3-4 8-4 11 0-3 4-8 4-11 0z" fill="#fff"/><g transform="translate(178 72)"><g fill="#C51F5D"><circle cx="0.0" cy="-6.3" r="3.6"/><circle cx="6.0" cy="-1.9" r="3.6"/><circle cx="3.7" cy="5.1" r="3.6"/><circle cx="-3.7" cy="5.1" r="3.6"/><circle cx="-6.0" cy="-1.9" r="3.6"/></g><circle r="2.7" fill="#fff400"/></g>
 <g transform="translate(81.6 64) scale(1.2)" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#8a5428" stroke-width="13"/><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#fff" stroke-width="8"/></g>
 <text x="120" y="153" text-anchor="middle" font-family="Lora, Georgia, serif" font-size="25" font-weight="700" letter-spacing="1" fill="#fff" stroke="#8a5428" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2027</text>
 <path transform="translate(74 144) scale(.06) translate(-120 -118)" d="M120 214C60 170 14 128 14 80 14 46 40 22 72 22c22 0 38 12 48 28 10-16 26-28 48-28 32 0 58 24 58 58 0 48-46 90-106 134z" fill="#C51F5D"/><path transform="translate(166 144) scale(.06) translate(-120 -118)" d="M120 214C60 170 14 128 14 80 14 46 40 22 72 22c22 0 38 12 48 28 10-16 26-28 48-28 32 0 58 24 58 58 0 48-46 90-106 134z" fill="#C51F5D"/>
</symbol>
<symbol id="v-horaff-pur" viewBox="-2 -2 68 56"><g transform="" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#1a1817" stroke-width="15"/><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#fff" stroke-width="8.5"/></g></symbol>
<symbol id="i-brezel" viewBox="0 0 24 24"><circle cx="15.5" cy="9" r="5.5" class="tupfer"/><path d="M12 20.2c-2 1-4.4 1-6.3-.2-2.8-1.8-3.6-5.6-1.8-8.7 1.7-3 5.6-4.6 7.6-2.4 1.6 1.8.9 4.6-.5 6.4"/><path d="M12 20.2c2 1 4.4 1 6.3-.2 2.8-1.8 3.6-5.6 1.8-8.7-1.7-3-5.6-4.6-7.6-2.4-1.6 1.8-.9 4.6.5 6.4"/><path d="m7 18.6 6.5-6.8M17 18.6l-6.5-6.8"/><path d="M8 6.2h.01M11 4.8h.01M14 5.3h.01" stroke-width="2.4"/></symbol>
<symbol id="i-riesenrad" viewBox="0 0 24 24"><circle cx="12" cy="10" r="7.5" class="tupfer"/><circle cx="12" cy="10" r="7"/><circle cx="12" cy="10" r="1.3"/><path d="M12 3v5.7M12 11.3V17M5 10h5.7M13.3 10H19M7 5l4 4M13 11l4 4M17 5l-4 4M11 11l-4 4"/><path d="m8 22 4-10.5L16 22M6.5 22h11"/><rect x="10.8" y="1.4" width="2.4" height="2" rx=".6"/><rect x="3.6" y="9" width="2" height="2.4" rx=".6"/><rect x="18.4" y="9" width="2" height="2.4" rx=".6"/></symbol>
<symbol id="i-ballon" viewBox="0 0 24 24"><path d="M12 15.5c3.4 0 6-3 6-6.6C18 5.3 15.3 2.5 12 2.5S6 5.3 6 8.9c0 3.6 2.6 6.6 6 6.6z" class="tupfer"/><path d="M12 15.5c3.4 0 6-3 6-6.6C18 5.3 15.3 2.5 12 2.5S6 5.3 6 8.9c0 3.6 2.6 6.6 6 6.6z"/><path d="m11 15.5-.7 1.5h3.4l-.7-1.5"/><path d="M12 17c-1.6 1.6 1.6 2.8 0 4.8"/><path d="M9 6.8c.5-1.2 1.4-1.9 2.4-2.1"/></symbol>
<symbol id="i-herz" viewBox="0 0 24 24"><path d="M12 20.5S3 15 3 8.8C3 6 5 4 7.5 4c1.9 0 3.5 1.1 4.5 2.7C13 5.1 14.6 4 16.5 4 19 4 21 6 21 8.8c0 6.2-9 11.7-9 11.7z" class="tupfer"/><path d="M12 20.5S3 15 3 8.8C3 6 5 4 7.5 4c1.9 0 3.5 1.1 4.5 2.7C13 5.1 14.6 4 16.5 4 19 4 21 6 21 8.8c0 6.2-9 11.7-9 11.7z"/><path d="M6.2 9.4c.9.9 1.8-.9 2.8 0s1.9-.9 2.9 0 1.9-.9 2.9 0 1.9-.9 2.8 0"/><path d="M9.5 12.6h5M10.5 15h3"/><path d="M8.5 4.3c1.5-3 5.5-3 7 0"/></symbol>
<symbol id="i-bonbon" viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="5" ry="3.8" class="tupfer"/><ellipse cx="12" cy="12" rx="5" ry="3.8"/><path d="M7.1 11 3 7.8v8.4l4.1-3.2M16.9 11 21 7.8v8.4l-4.1-3.2"/><path d="M10 9.2c.8 1.6.8 4 0 5.6M13.6 9.1c.8 1.7.8 4.1 0 5.8"/></symbol>
<symbol id="i-dirndl" viewBox="0 0 24 24"><path d="M9 3.5 8 8l-3.5 12.5h15L16 8l-1-4.5"/><path d="M8 8h8M9.3 3.5c.8 1.7 4.6 1.7 5.4 0"/><path d="M13.5 8.5 15 20.5" /><path d="M10 12.5h4"/></symbol>
<symbol id="i-lederhose" viewBox="0 0 24 24"><path d="M6.5 9h11l1 11.5h-5L12 14l-1.5 6.5h-5z"/><path d="M8 9 6.5 2.5M16 9l1.5-6.5M7.4 5.2h9.2"/><circle cx="9.3" cy="12" r=".6"/><circle cx="14.7" cy="12" r=".6"/></symbol>
<symbol id="i-wagen" viewBox="0 0 24 24"><path d="M3 15.5h15.5l1-6H5.5z" class="tupfer"/><path d="M3 15.5h15.5l1-6H5.5z"/><path d="M6 9.5 7.5 5.5h8l2 4M19.5 12.5H22"/><circle cx="7" cy="18" r="2.3"/><circle cx="16" cy="18" r="2.3"/><path d="M9.5 5.5 10.5 3l1.2 2.5L13 3l1.1 2.5"/></symbol>
<symbol id="i-engel" viewBox="0 0 24 24"><path d="M10.2 11.4C7.8 8 4 6.3 1.8 7c-.1 4.7 2.5 8.6 6.8 9.7zM13.8 11.4C16.2 8 20 6.3 22.2 7c.1 4.7-2.5 8.6-6.8 9.7z" class="tupfer"/><path d="M10.2 11.4C7.8 8 4 6.3 1.8 7c-.1 4.7 2.5 8.6 6.8 9.7M13.8 11.4C16.2 8 20 6.3 22.2 7c.1 4.7-2.5 8.6-6.8 9.7"/><path d="M4.8 10.3c.9 1.7 2.3 3 4 3.8M19.2 10.3c-.9 1.7-2.3 3-4 3.8"/><ellipse cx="12" cy="2.3" rx="3.2" ry="1"/><circle cx="12" cy="6.4" r="2.1"/><path d="M10.3 9.7h3.4l3.4 11.3H6.9z"/></symbol>
<symbol id="i-hand" viewBox="0 0 24 24"><circle cx="16" cy="8" r="5" class="tupfer"/><path d="M8 12V5.5a1.5 1.5 0 0 1 3 0V11M11 10.5V4a1.5 1.5 0 0 1 3 0v6.5M14 10.5V5.5a1.5 1.5 0 0 1 3 0V13c0 4.4-2.7 8-7 8-3.2 0-4.8-1.6-6.4-4.8L2.4 13.6a1.5 1.5 0 0 1 2.5-1.6L8 15"/></symbol>
<symbol id="i-sonne" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5.5" class="tupfer"/><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/><path d="M10.4 12.6c.9.9 2.3.9 3.2 0"/></symbol>
<symbol id="i-handy" viewBox="0 0 24 24"><rect x="6.5" y="2.5" width="11" height="19" rx="2.2" class="tupfer"/><rect x="6.5" y="2.5" width="11" height="19" rx="2.2"/><path d="M10.5 5h3M9.5 10.8l1.8 1.8 3.4-3.4"/><path d="M11 18.5h2"/></symbol>
<symbol id="i-gespraech" viewBox="0 0 24 24"><path d="M3 5.5A2.5 2.5 0 0 1 5.5 3h8A2.5 2.5 0 0 1 16 5.5v4a2.5 2.5 0 0 1-2.5 2.5H8.5L5 15v-3h.5A2.5 2.5 0 0 1 3 9.5z" class="tupfer"/><path d="M3 5.5A2.5 2.5 0 0 1 5.5 3h8A2.5 2.5 0 0 1 16 5.5v4a2.5 2.5 0 0 1-2.5 2.5H8.5L5 15v-3.1A2.5 2.5 0 0 1 3 9.5z"/><path d="M18.5 8.5A2.5 2.5 0 0 1 21 11v4a2.5 2.5 0 0 1-2.5 2.5H19v3l-3.5-3H11a2.5 2.5 0 0 1-2.5-2.5"/><path d="M7 7.5h5"/></symbol>
<symbol id="i-pfeil" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
<symbol id="i-weiter" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-regen" viewBox="0 0 24 24"><path d="M7 16.5h10.5a4 4 0 0 0 .6-8 6 6 0 0 0-11.6 1A3.5 3.5 0 0 0 7 16.5z" class="tupfer"/><path d="M7 16.5h10.5a4 4 0 0 0 .6-8 6 6 0 0 0-11.6 1A3.5 3.5 0 0 0 7 16.5z"/><path d="M9 19.5l-.8 2M13 19.5l-.8 2M17 19.5l-.8 2"/></symbol>
</defs></svg>'''

VORSEITE = "index.html"

# Seiten der Homepage: Datei -> Link. Absolute Links, damit sie auch aus entwicklung/ heraus stimmen.
LINK = {"index.html": "/", "start.html": "/start.html", "festzug.html": "/festzug.html", "ueber-uns.html": "/ueber-uns.html",
        "impressum.html": "/impressum.html", "datenschutz.html": "/datenschutz.html"}

def i(name, cls="ico"): return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

# Alles zwischen ENTWICKLUNG:START und ENTWICKLUNG:END gehört zu „/ Entwicklung /“ und geht nie auf main.
def entwicklung(inhalt): return f"<!-- ENTWICKLUNG:START -->\n{inhalt}\n<!-- ENTWICKLUNG:END -->"

def kopf(seite):
    if seite == VORSEITE:
        return ('''<header class="kopf"><div class="wrap">
<span class="marke"><svg class="marke__zeichen" aria-hidden="true"><use href="#v-horaff"/></svg><span><b>Wagenpaten</b><small>Volksfestumzug der Schulen 2027</small></span></span>
<nav class="nav" aria-label="Seiten"><a class="knopf" href="/start.html">Zur Homepage</a></nav></div></header>''')
    nav = [("start.html", "Start"), ("festzug.html", "Der Festzug"), ("ueber-uns.html", "Über uns")]
    return (f'''<header class="kopf"><div class="wrap">
<a class="marke" href="/start.html"><svg class="marke__zeichen" aria-hidden="true"><use href="#v-horaff"/></svg><span><b>Wagenpaten</b><small>Volksfestumzug der Schulen 2027</small></span></a>
<div class="stadtlogo" title="Platzhalter – Nutzung des Stadtlogos vor Veröffentlichung mit der Stadt klären"><span>CR</span>Mit freundlicher<br>Unterstützung (Logo Stadt)</div>
<nav class="nav" aria-label="Seiten">''' + "".join(f'<a href="{LINK[d]}"' + (' aria-current="page"' if d == seite else "") + f'>{t}</a>' for d, t in nav) +
            '<a class="knopf" href="/festzug.html">Wagen aussuchen</a></nav></div></header>')

FUSS = '''<footer class="fuss"><div class="wrap">
<div><b>Wagenpaten</b><p style="margin-top:.4rem">Eine Initiative von Crailsheimern für Crailsheim.<br>Kontakt: daniel.stroebel@empiria.de</p></div>
<nav><a href="/start.html">Start</a><a href="/festzug.html">Der Festzug</a><a href="/ueber-uns.html">Über uns</a><a href="/impressum.html">Impressum</a><a href="/datenschutz.html">Datenschutz</a></nav>
</div></footer>'''

def seite(datei, titel, rumpf):
    html = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel} · Wagenpaten (Entwurf)</title>
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="/assets/fonts/fonts.css">
<link rel="stylesheet" href="/assets/vofe.css">
{entwicklung('<link rel="stylesheet" href="/entwicklung/menu.css">')}
</head>
<body>
{SYMBOLE}
{kopf(datei)}
<main>
{rumpf}
</main>
{FUSS}
<script src="/assets/vofe.js"></script>
{entwicklung('<script src="/entwicklung/menu.js"></script>')}
</body>
</html>
'''
    (Z / datei).write_text(html, encoding="utf-8")

# Beispiel-Paten mit Logo (Originalfarben). Das Logo von Müller & Ströbel wird eingebettet,
# weil seine Schrift (Lora) sonst nicht aus der Seite geladen wird.
def _ms_logo():
    s = (Z / "assets/bilder/logos/mueller-stroebel.svg").read_text(encoding="utf-8")
    s = re.sub(r"<\?xml.*?\?>|<!--.*?-->", "", s, flags=re.S).strip()
    s = s.replace(' id="Ebene_1"', ' role="img" aria-label="Müller &amp; Ströbel"').replace(".st", ".ms-st").replace('class="st', 'class="ms-st')
    return s
LOGO = {
    "empiria GmbH": '<img class="logo--empiria" src="/assets/bilder/logos/empiria.svg" alt="empiria GmbH">',
    "sofort sichtbar": '<img class="logo--sofort" src="/assets/bilder/logos/sofortsichtbar.svg" alt="sofort sichtbar">',
    "Müller &amp; Ströbel": _ms_logo(),
}

# ---------------------------------------------------------------- Startseite
START = f'''<section class="held"><div class="wrap">
<div>
  <p class="kicker">Volksfestumzug der Schulen 2027 · Crailsheim</p>
  <h1>Süßes für den <em>Umzug.</em></h1>
  <p class="lead">Beim Fränkischen Volksfest 2027 sind wieder die Schulen dran: Übernehmt die Patenschaft für einen Wagen – damit die Kinder ihre Süßigkeiten nicht mehr selbst mitbringen müssen und am Straßenrand alle strahlen.</p>
  <div class="knoepfe"><a class="knopf" href="/festzug.html">Wagen aussuchen {i("weiter")}</a><a class="knopf knopf--rand" href="#so-gehts">So funktioniert es</a></div>
  <div class="held__fakten"><div><b>23</b>Wagen der Schulen</div><div><b>16</b>Schulen aus Crailsheim</div><div><b>2027</b>Umzug der Schulen</div></div>
</div>
<div class="held__bild" aria-hidden="true">
  <svg class="held__zeichen"><use href="#v-herz"/></svg>
</div>
</div></section>

<section class="sek sek--gelb"><div class="wrap idee">
<div class="idee__text">
  <p class="kicker">Die Idee</p>
  <h2 class="h2">Damit die Kinder einfach nur Spaß haben.</h2>
  <p style="margin-top:1.4rem">Beim Fränkischen Volksfest 2027 gestalten wieder die Schulen den großen Umzug. Hunderte Kinder laufen mit und verteilen Süßigkeiten an die Zuschauer am Straßenrand.</p>
  <p>Bisher bringen die Kinder ihre Süßigkeiten selbst mit. Das wollen wir ändern: Unternehmen aus Crailsheim und Umgebung werden Wagenpaten – zum Wohl aller.</p>
  <p><b>Wagenengel</b> sorgen beim Umzug für die Sicherheit an den Wagen. <b>Wagenpaten</b> sorgen dafür, dass auf dem Wagen ordentlich was zum Verteilen ist.</p>
</div>
<div class="zitat">{i("engel")}<p>„Als Wagenengel habe ich beim letzten Schulumzug gesehen, wie viel Freude die Kinder haben – dass sie dafür aber ihre eigenen Süßigkeiten mitbringen müssen.“</p><small>Daniel Ströbel, Initiator</small></div>
</div></section>

<section class="sek" id="so-gehts"><div class="wrap">
<p class="kicker">So funktioniert es</p>
<h2 class="h2">In vier Schritten zum Wagenpaten.</h2>
<div class="schritte">
  <div class="schritt"><span class="schritt__ico">{i("wagen")}</span><h3>Wagen aussuchen</h3><p>Im Festzug seht ihr jeden Wagen mit Motto und Schule.</p></div>
  <div class="schritt"><span class="schritt__ico">{i("hand")}</span><h3>Wagenpate werden</h3><p>Ein Klick genügt – wir melden uns und klären alles Weitere.</p></div>
  <div class="schritt"><span class="schritt__ico">{i("bonbon")}</span><h3>Süßes bereitstellen</h3><p>Süßigkeiten oder Kleinigkeiten zum Verteilen – Menge und Übergabe stimmen wir mit der Schule ab.</p></div>
  <div class="schritt"><span class="schritt__ico">{i("sonne")}</span><h3>Alle strahlen</h3><p>Am Umzugstag verteilen die Kinder eure Gaben – und ihr seid Teil des Festes.</p></div>
</div>
</div></section>

<section class="sek sek--schwarz"><div class="wrap">
<p class="kicker">Für Unternehmen</p>
<h2 class="h2">Was bringt das eurem Unternehmen?</h2>
<p class="lead">Eine Patenschaft ist ein Beitrag zu einer Tradition, die Crailsheim ausmacht – und ganz nebenbei gut sichtbar.</p>
<div class="nutzen">
  <div>{i("herz")}<h3>Tradition unterstützen</h3><p>Der Volksfestumzug gehört zu Crailsheim. Mit eurer Patenschaft tragt ihr aktiv dazu bei, dass er so bleibt, wie wir ihn lieben.</p></div>
  <div>{i("riesenrad")}<h3>Ein Erlebnis für alle</h3><p>Ihr macht es möglich, dass alle Beteiligten ein großartiges Erlebnis haben – die Kinder auf den Wagen und alle, die am Straßenrand zuschauen.</p></div>
  <div>{i("handy")}<h3>Ganz nebenbei: sichtbar</h3><p>Euer Logo auf dieser Seite und in der Zeile eures Wagens. Dazu Beiträge auf Instagram und Facebook – vor und nach dem Umzug.</p><p class="nutzen__extra">Social-Media-Paket inklusive</p></div>
</div>
</div></section>

<section class="sek sek--hell"><div class="wrap">
<p class="kicker">Social Media</p>
<h2 class="h2">So erzählen wir es weiter.</h2>
<p class="lead">Jede neue Patenschaft wird zum Beitrag – automatisch gebrandet, in Schwarz und Gelb. Beispiele:</p>
<div class="posts">
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>wagenpaten.crailsheim</div><div class="post__bild post__bild--gelb"><small>Neuer Pate</small><b>Musterfirma wird Wagenpate für „Backhaus“.</b>{i("brezel")}</div><p class="post__text">Danke! Die Reußenbergschule freut sich auf süße Unterstützung. #Volksfest #Crailsheim</p></article>
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>wagenpaten.crailsheim</div><div class="post__bild post__bild--schwarz"><small>Countdown</small><b>Noch 30 Tage bis zum Umzug.</b>{i("riesenrad")}</div><p class="post__text">15 Wagen haben schon Wagenpaten – wer macht den nächsten möglich?</p></article>
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>wagenpaten.crailsheim</div><div class="post__bild post__bild--weiss"><small>Danke</small><b>23 Wagen. Ein großes Fest.</b>{i("ballon")}</div><p class="post__text">Danke an alle Wagenpaten, Wagenengel, Schulen und Kinder – das war ein Umzug!</p></article>
</div>
</div></section>

<section class="sek"><div class="wrap">
<div class="ausfall">{i("regen")}<div><h3>Und wenn ein Wagen ausfällt?</h3>
<p class="lead" style="margin-top:.6rem">Krankheit, eine Panne, schlechtes Wetter – es kann immer etwas dazwischenkommen. Dafür haben wir eine faire Regel:</p>
<ul><li><b>Rechtzeitig bekannt:</b> Ihr müsst nichts bereitstellen.</li><li><b>Kurzfristig:</b> Wir finden gemeinsam eine sichtbare Lösung, eure Süßigkeiten trotzdem zu verteilen – wenn ihr das möchtet.</li></ul></div></div>
</div></section>

<section class="sek sek--hell"><div class="wrap">
<p class="kicker">Unsere Paten</p>
<h2 class="h2">Diese Unternehmen sind dabei.</h2>
<p class="lead">Für den Umzug 2027.</p><div class="paten"><span class="beispiel logo">{LOGO["empiria GmbH"]}</span><span class="beispiel logo">{LOGO["sofort sichtbar"]}</span><span class="beispiel logo">{LOGO["Müller &amp; Ströbel"]}</span><span>Euer Logo</span><span>Euer Logo</span><span>Euer Logo</span></div>
</div></section>

<section class="band"><div class="wrap"><h2>Sucht euch euren Wagen aus.</h2><a class="knopf" href="/festzug.html">Zum Festzug {i("weiter")}</a></div></section>'''

# ---------------------------------------------------------------- Festzug
WAGEN = [
 ("Bau der Liebfrauenkapelle, Stadttor &amp; Gräfin Adelheid", "Realschule am Karlsberg", None),
 ("Bischof Burkhard, Begründer der Münsterlinie", "Realschule zur Flügelau und Grundschule Altenmünster", None),
 ("Barbara von Zipplingen und Hammeltanz", "Grundschule Altenmünster", None),
 ("Höfisches Leben auf der Burg Flügelau", "Realschule zur Flügelau", "empiria GmbH"),
 ("Freud’ und Leid in alter Zeit", "Albert-Schweitzer-Gymnasium", None),
 ("Adam Weiß und die Reformation in Crailsheim", "Albert-Schweitzer-Gymnasium", None),
 ("Alchimisten im Mittelalter", "Lise-Meitner-Gymnasium", None),
 ("Recht und Gericht in Crailsheim", "Lise-Meitner-Gymnasium", None),
 ("Brand im Spital", "Käthe-Kollwitz-Schule", None),
 ("Der tapfere Burkhard im Gefolge seiner Stadtknechte", "Leonhard-Sachs-Schule", None),
 ("Widder", "Leonhard-Sachs-Schule", None),
 ("Fahnenträger der belagernden Städte", "Leonhard-Sachs-Schule", None),
 ("Angreifende Haufen der Belagerer", "Leonhard-Sachs-Schule", None),
 ("Blide", "Leonhard-Sachs-Schule", None),
 ("Sturm auf die Stadtmauer", "Eichendorffschule", "sofort sichtbar"),
 ("Bürgermeisterin", "Leonhard-Sachs-Schule", None),
 ("Spielende Kindergruppen", "Sprachheilschule Crailsheim", None),
 ("Bäuerliches Treiben um die Ingersheimer Mühle", "Geschwister-Scholl-Schule", None),
 ("Backhaus", "Reußenbergschule", "Müller &amp; Ströbel"),
 ("Die Gaukler vom Burgberg", "Freie Waldorfschule", None),
 ("Wacholderheide", "Astrid-Lindgren-Schule und Konrad-Biesalski-Schule", None),
 ("Diehlbrunnen von Bronnholzheim", "Fröbelschule Ellrichshausen", None),
 ("Fürstenhochzeit 1537 im Crailsheimer Schloss", "Eugen-Grimminger-Schule", None),
]
def wagen(n, w):
    t, s, p = w
    status = f'<span class="status status--pate">Pate: {p}</span>' if p else '<span class="status status--frei">Noch frei</span>'
    mail = f'mailto:daniel.stroebel@empiria.de?subject=Patenschaft%20Wagen%20{n:02d}'
    unten = (f'<div class="wagen__pate"><span class="wagen__logo">{LOGO.get(p, "LOGO")}</span><div><b>{p}</b> <small>(Beispiel)</small><br><small>ist Pate dieses Wagens – danke!</small></div></div>' if p
             else f'<a class="knopf" href="{mail}">Patenschaft übernehmen {i("weiter")}</a>')
    return (f'<li class="wagen{" wagen--pate" if p else ""}"><span class="wagen__nr">{n:02d}</span><details><summary><div><h3>{t}</h3><p class="wagen__schule">{s}</p></div>{status}{i("pfeil","pfeil")}</summary>'
            f'<div class="wagen__mehr"><dl><dt>Motto</dt><dd>{t}</dd><dt>Schule</dt><dd>{s}</dd><dt>Verteilt wird</dt><dd>Süßigkeiten und Kleinigkeiten – Menge stimmen wir mit der Schule ab</dd></dl>{unten}</div></details></li>')

FESTZUG = f'''<section class="zugkopf"><div class="wrap">
<p class="kicker">Volksfestumzug der Schulen 2027</p>
<h1>Der Festzug.</h1>
<p class="lead">Alle Wagen der Schulen in der Reihenfolge des Umzugs. Klappt einen Wagen auf, um mehr zu sehen – und übernehmt die Patenschaft für einen, der noch frei ist.</p>
<div class="stand"><div class="balken"><i data-balken></i></div><p data-stand></p></div>
<div class="filter" role="group" aria-label="Wagen filtern"><button type="button" data-f="alle" aria-pressed="true">Alle Wagen</button><button type="button" data-f="frei" aria-pressed="false">Noch frei</button><button type="button" data-f="pate" aria-pressed="false">Mit Pate</button></div>
<ol class="zug" data-zug>{"".join(wagen(n+1, w) for n, w in enumerate(WAGEN))}</ol>
<p class="zug__hinweis">Vorschau auf Basis des Festzugs der Schulen 2024 („Luuschd, Laad und Lait – Craalse in alter Zeit“). Die Wagen für 2027 folgen, sobald die Schulen ihre Motive festgelegt haben. Paten sind Beispiele.</p>
</div></section>
<section class="band"><div class="wrap"><h2>Fragen zur Patenschaft?</h2><a class="knopf" href="/ueber-uns.html">Wer dahintersteckt {i("weiter")}</a></div></section>'''

# ---------------------------------------------------------------- Über uns
UEBER = f'''<section class="sek"><div class="wrap ueber">
<div class="ueber__text">
  <p class="kicker">Motivation &amp; über uns</p>
  <h1 class="h2" style="font-size:clamp(2.6rem,6vw,4.6rem)">Weil das Volksfest zu uns gehört.</h1>
  <p style="margin-top:1.6rem">Wir sind Crailsheimer und Hohenloher – seit Kindheitstagen. Das Fränkische Volksfest ist fest in unseren Köpfen verankert: das Riesenrad, die Brezeln, der Umzug, bei dem die ganze Stadt auf den Beinen ist.</p>
  <p>Diese Tradition lebt davon, dass viele mitmachen. Wir haben uns überlegt, wo wir einen kleinen Beitrag leisten können – und sind bei den Kindern gelandet, die den Umzug der Schulen erst möglich machen.</p>
  <p>Die Idee ist einfach: Unternehmen aus der Region werden Wagenpaten. Die Wagenengel kümmern sich um die Sicherheit, die Wagenpaten darum, dass auf dem Wagen ordentlich was zum Verteilen ist. Die Kinder müssen nichts mehr selbst mitbringen – und am Straßenrand freuen sich alle.</p>
</div>
<div class="kopfe">
  <div class="person"><img class="person__foto" src="/assets/bilder/ansprechpartner-daniel.webp" alt="Daniel Ströbel"><div><b>Daniel Ströbel</b><small>Initiator · beim letzten Schulumzug als Wagenengel dabei</small></div></div>
  <div class="person"><span class="person__platz">+</span><div><b>Mitstreiter gesucht</b><small>Platz für weitere Unterstützer der Idee</small></div></div>
</div>
</div>
<div class="wrap"><div class="werte">
  <div><h3>Für die Kinder</h3><p>Sie machen den Umzug – sie sollen ihn ohne Sorgen genießen.</p></div>
  <div><h3>Für Crailsheim</h3><p>Eine Tradition, die die Stadt zusammenbringt, verdient Unterstützung.</p></div>
  <div><h3>Mit Herz, ohne Aufwand</h3><p>Für Paten so einfach wie möglich: aussuchen, bereitstellen, freuen.</p></div>
</div></div></section>
<section class="band"><div class="wrap"><h2>Macht mit – sucht euch einen Wagen aus.</h2><a class="knopf" href="/festzug.html">Zum Festzug {i("weiter")}</a></div></section>'''

# ---------------------------------------------------------------- Vorseite (Vorstellung der Homepage, z. B. für die Schulleitung)
def vorschau(datei, bild, nr, titel, text):
    return (f'<a class="vs-karte" href="{LINK[datei]}"><span class="vs-fenster"><span class="vs-leiste"><i></i><i></i><i></i><span>wagenpaten-crailsheim.de</span></span>'
            f'<span class="vs-seite"><img src="/assets/bilder/vorschau-{bild}.jpg?v=3" alt="Vorschau der Seite „{titel}“"></span></span>'
            f'<span class="vs-text"><small>Seite {nr}</small><b>{titel}</b><span class="vs-text__p">{text}</span><span class="vs-pfeil">Seite öffnen {i("weiter")}</span></span></a>')

VORSTELLUNG = f'''<section class="held vs-held"><div class="wrap">
<div>
  <p class="kicker">Eine Idee für den Volksfestumzug der Schulen 2027</p>
  <h1>Warum es die <em>Wagenpaten</em> gibt.</h1>
  <p class="lead">Beim letzten Schulumzug war ich als Wagenengel dabei. Ich habe gesehen, wie viel Freude die Kinder haben – und dass sie die Süßigkeiten zum Verteilen selbst mitbringen. Das möchte ich ändern. Denn das Volksfest gehört zu Crailsheim, und der Umzug der Schulen gehört dazu.</p>
  <div class="knoepfe"><a class="knopf" href="/start.html">Zur Homepage {i("weiter")}</a></div>
  <div class="vs-person"><img src="/assets/bilder/ansprechpartner-daniel.webp" alt="Daniel Ströbel"><div><b>Daniel Ströbel</b><small>Crailsheimer · <span class="vs-nw">ehemaliger Schüler des ASG</span></small></div></div>
</div>
<div class="vs-marke">
  <svg aria-hidden="true"><use href="#v-horaff"/></svg>
  <b>Wagenpaten</b><small>Volksfestumzug der Schulen 2027</small>
  <dl class="vs-rollen"><div><dt>Wagenengel</dt><dd>Sicherheit <em>am Wagen.</em></dd></div><div><dt>Wagenpaten</dt><dd>Süßes <em>auf dem Wagen.</em></dd></div></dl>
</div>
</div></section>

<section class="sek sek--gelb"><div class="wrap">
<p class="kicker">Die Idee</p>
<h2 class="h2">So läuft es ab.</h2>
<ol class="vs-ablauf">
  <li><span class="vs-ablauf__nr">1</span>{i("gespraech")}<h3>Idee vorstellen</h3><p>Wir gehen auf Unternehmen aus Crailsheim und Umgebung zu und stellen ihnen die Wagenpaten vor.</p></li>
  <li><span class="vs-ablauf__nr">2</span>{i("wagen")}<h3>Wagen aussuchen</h3><p>Auf der Homepage sehen die Unternehmen alle Wagen, die beim Umzug mitfahren. Mit einem Klick übernehmen sie die Patenschaft für einen Wagen.</p></li>
  <li><span class="vs-ablauf__nr">3</span>{i("handy")}<h3>Darüber berichten</h3><p>Wir berichten regelmäßig in Social Media über die Paten. Dazu bekommen die Unternehmen fertige Postings, mit denen sie sich auf ihren eigenen Kanälen als Wagenpate zeigen.</p></li>
  <li class="vs-ablauf--ziel"><span class="vs-ablauf__nr">4</span><span class="vs-ablauf__marke">Das Highlight</span>{i("sonne")}<h3>Der Umzug</h3><p>Beim Volksfestumzug 2027 sind die Wagen ordentlich ausgestattet. Glückliche Kinder auf beiden Seiten: auf dem Wagen und am Straßenrand.</p></li>
</ol>
</div></section>

<section class="sek"><div class="wrap">
<p class="kicker">Wie wir es angehen</p>
<h2 class="h2">Zwei Möglichkeiten.</h2>
<div class="vs-wege">
  <article class="vs-weg"><p class="vs-weg__kopf"><small>Möglichkeit 1</small></p>
  <h3>Gemeinsam mit dem ASG.</h3>
  <p>Als ehemaliger Schüler hole ich das Albert-Schweitzer-Gymnasium sehr gern mit ins Boot. Wenn das ASG möchte, tritt es als Mitinitiator der Wagenpaten auf und ist auf der Homepage und in Social Media sichtbar.</p>
  <p class="vs-weg__hinweis">Die genaue Ausgestaltung stimmen wir gemeinsam ab. Sie lässt sich individuell an die Wünsche des ASG anpassen.</p>
  </article>
  <article class="vs-weg"><p class="vs-weg__kopf"><small>Möglichkeit 2</small></p>
  <h3>Ich treibe es allein voran.</h3>
  <p>Nicht jede Schule kann oder darf als Initiator einer Aktion mit Unternehmen auftreten, etwa weil sie damit Verantwortung übernehmen würde. Dann setze ich die Wagenpaten als private Initiative um. Das ASG ist wie alle Schulen beim Umzug dabei.</p>
  </article>
</div>
<ul class="vs-beide"><li><small>In beiden Fällen</small></li><li>Kein Aufwand für die Schule</li><li>Die Umsetzung übernehme ich</li><li>Alle Schulen profitieren</li></ul>
</div></section>

<section class="sek sek--hell"><div class="wrap">
<p class="kicker">Die Homepage</p>
<h2 class="h2">Drei Seiten, jede mit einer Aufgabe.</h2>
<div class="vs-seiten">
  {vorschau("start.html", "umzug-schulen", 1, "Start", "Erklärt Unternehmen die Idee: was eine Patenschaft bringt, wie sie in vier Schritten funktioniert und wie wir in Social Media darüber berichten.")}
  {vorschau("festzug.html", "festzug", 2, "Der Festzug", "Alle 23 Wagen der Schulen in der Reihenfolge des Umzugs. Freie Wagen sind markiert, vergebene zeigen ihren Paten. Mit einem Klick wird ein Unternehmen Wagenpate.")}
  {vorschau("ueber-uns.html", "ueber-uns", 3, "Über uns", "Warum es die Wagenpaten gibt und wer dahintersteht. Hier ist auch der Platz für das ASG als Mitinitiator.")}
</div>
</div></section>

<section class="band"><div class="wrap"><h2>Jetzt die Homepage ansehen.</h2><a class="knopf" href="/start.html">Zur Homepage {i("weiter")}</a></div></section>'''

# ---------------------------------------------------------------- Impressum und Datenschutz (Angaben der empiria GmbH)
ANSCHRIFT = """empiria GmbH<br>
Kapellengasse 6<br>
74564 Crailsheim"""
KONTAKT = """Telefon: <a href="tel:+4917631347217">+49 176 31347217</a><br>
E-Mail: <a href="mailto:daniel.stroebel@empiria.de">daniel.stroebel@empiria.de</a>"""

IMPRESSUM = f'''<section class="sek recht"><div class="wrap">
<h1 class="h2">Impressum</h1>
<h2>Angaben gemäß § 5 DDG</h2>
<address>{ANSCHRIFT}</address>
<h2>Vertreten durch</h2>
<p>Daniel Ströbel</p>
<h2>Kontakt</h2>
<p>{KONTAKT}</p>
<h2>Registereintrag</h2>
<p>Eintragung im Handelsregister.<br>Registergericht: Amtsgericht Ulm<br>Registernummer: HRB 750146</p>
<h2>Umsatzsteuer-ID</h2>
<p>Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz:<br>DE 281217286</p>
<h2>Verbraucher&shy;streit&shy;beilegung / Universal&shy;schlichtungs&shy;stelle</h2>
<p>Wir nehmen an einem Streitbeilegungsverfahren vor einer Verbraucher&shy;schlichtungs&shy;stelle teil. Zuständig ist die Universalschlichtungsstelle des Zentrums für Schlichtung e.V., Straßburger Straße 8, 77694 Kehl am Rhein (<a href="https://www.verbraucher-schlichter.de" target="_blank" rel="noopener">www.verbraucher-schlichter.de</a>).</p>
</div></section>'''

DATENSCHUTZ = f'''<section class="sek recht"><div class="wrap">
<h1 class="h2">Datenschutz&shy;erklärung</h1>

<h2>1. Datenschutz auf einen Blick</h2>
<h3>Allgemeine Hinweise</h3>
<p>Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können. Ausführliche Informationen zum Thema Datenschutz entnehmen Sie unserer unter diesem Text aufgeführten Datenschutzerklärung.</p>
<h3>Datenerfassung auf dieser Website</h3>
<p><strong>Wer ist verantwortlich für die Datenerfassung auf dieser Website?</strong><br>Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber. Dessen Kontaktdaten können Sie dem Abschnitt „Hinweis zur verantwortlichen Stelle“ in dieser Datenschutzerklärung entnehmen.</p>
<p><strong>Wie erfassen wir Ihre Daten?</strong><br>Diese Website ist eine reine Informationsseite. Sie enthält keine Kontaktformulare und keine Registrierung. Personenbezogene Daten erhalten wir nur, wenn Sie uns diese aktiv mitteilen, etwa wenn Sie uns per E-Mail oder Telefon kontaktieren. Andere Daten werden automatisch beim Besuch der Website durch den Hosting-Dienstleister erfasst (v. a. technische Daten wie Browser, Betriebssystem oder Uhrzeit des Seitenaufrufs in Server-Logfiles).</p>
<p><strong>Wofür nutzen wir Ihre Daten?</strong><br>Ein Teil der Daten wird erhoben, um eine fehlerfreie Bereitstellung der Website zu gewährleisten. Von Ihnen aktiv übermittelte Daten (z. B. per E-Mail) verwenden wir zur Bearbeitung Ihrer Anfrage.</p>
<p><strong>Welche Rechte haben Sie bezüglich Ihrer Daten?</strong><br>Sie haben jederzeit das Recht, unentgeltlich Auskunft über Herkunft, Empfänger und Zweck Ihrer gespeicherten personenbezogenen Daten zu erhalten. Sie haben außerdem ein Recht, die Berichtigung oder Löschung dieser Daten zu verlangen. Eine erteilte Einwilligung können Sie jederzeit für die Zukunft widerrufen. Unter bestimmten Umständen können Sie die Einschränkung der Verarbeitung verlangen. Des Weiteren steht Ihnen ein Beschwerderecht bei der zuständigen Aufsichtsbehörde zu.</p>

<h2>2. Hosting</h2>
<p>Wir hosten die Inhalte unserer Website bei folgendem Anbieter:</p>
<h3>Vercel</h3>
<p>Anbieter ist die Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, USA (nachfolgend „Vercel“).</p>
<p>Wenn Sie unsere Website besuchen, erfasst Vercel als unser Auftragsverarbeiter automatisch Server-Logfiles, die Ihr Browser übermittelt (u. a. IP-Adresse, Datum und Uhrzeit des Zugriffs, angeforderte Datei/URL, Browsertyp und -version, Betriebssystem). Dies ist technisch erforderlich, um die Website zuverlässig und sicher auszuliefern. Die Verarbeitung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer zuverlässigen und sicheren Darstellung unserer Website).</p>
<p>Die Datenübertragung in die USA wird auf die Standardvertragsklauseln der EU-Kommission gestützt; zudem ist Vercel unter dem EU-U.S. Data Privacy Framework zertifiziert. Details: <a href="https://vercel.com/legal/privacy-policy" target="_blank" rel="noopener">vercel.com/legal/privacy-policy</a>.</p>
<p>Die auf dieser Website verwendeten Schriftarten (Lora, Poppins) sind lokal auf unserem Hosting eingebunden; es findet dabei kein Verbindungsaufbau zu Servern Dritter statt.</p>

<h2>3. Allgemeine Hinweise und Pflicht&shy;informationen</h2>
<h3>Datenschutz</h3>
<p>Die Betreiber dieser Seiten nehmen den Schutz Ihrer persönlichen Daten sehr ernst. Wir behandeln Ihre personenbezogenen Daten vertraulich und entsprechend den gesetzlichen Datenschutzvorschriften sowie dieser Datenschutzerklärung. Wir weisen darauf hin, dass die Datenübertragung im Internet (z. B. bei der Kommunikation per E-Mail) Sicherheitslücken aufweisen kann. Ein lückenloser Schutz der Daten vor dem Zugriff durch Dritte ist nicht möglich.</p>
<h3>Hinweis zur verantwortlichen Stelle</h3>
<p>Die verantwortliche Stelle für die Datenverarbeitung auf dieser Website ist:</p>
<address>empiria GmbH<br>
Daniel Ströbel<br>
Kapellengasse 6<br>
74564 Crailsheim<br>
{KONTAKT}</address>
<p>Verantwortliche Stelle ist die natürliche oder juristische Person, die allein oder gemeinsam mit anderen über die Zwecke und Mittel der Verarbeitung von personenbezogenen Daten entscheidet.</p>
<h3>Speicherdauer</h3>
<p>Soweit innerhalb dieser Datenschutzerklärung keine speziellere Speicherdauer genannt wurde, verbleiben Ihre personenbezogenen Daten bei uns, bis der Zweck für die Datenverarbeitung entfällt. Wenn Sie ein berechtigtes Löschersuchen geltend machen oder eine Einwilligung zur Datenverarbeitung widerrufen, werden Ihre Daten gelöscht, sofern wir keine anderen rechtlich zulässigen Gründe für die Speicherung (z. B. steuer- oder handelsrechtliche Aufbewahrungsfristen) haben; im letztgenannten Fall erfolgt die Löschung nach Fortfall dieser Gründe.</p>
<h3>Allgemeine Hinweise zu den Rechtsgrundlagen der Datenverarbeitung</h3>
<p>Sofern Sie in die Datenverarbeitung eingewilligt haben, verarbeiten wir Ihre Daten auf Grundlage von Art. 6 Abs. 1 lit. a DSGVO bzw. Art. 9 Abs. 2 lit. a DSGVO. Sind Ihre Daten zur Vertragserfüllung oder zur Durchführung vorvertraglicher Maßnahmen erforderlich, verarbeiten wir sie auf Grundlage des Art. 6 Abs. 1 lit. b DSGVO. Zur Erfüllung einer rechtlichen Verpflichtung verarbeiten wir Daten auf Grundlage des Art. 6 Abs. 1 lit. c DSGVO. Die Datenverarbeitung kann ferner auf Grundlage unseres berechtigten Interesses nach Art. 6 Abs. 1 lit. f DSGVO erfolgen.</p>
<h3>Empfänger von personenbezogenen Daten</h3>
<p>Im Rahmen unserer Geschäftstätigkeit geben wir personenbezogene Daten nur weiter, wenn dies zur Vertragserfüllung erforderlich ist, wir gesetzlich dazu verpflichtet sind, ein berechtigtes Interesse an der Weitergabe besteht oder eine sonstige Rechtsgrundlage die Weitergabe erlaubt. Beim Einsatz von Auftragsverarbeitern (z. B. unserem Hosting-Anbieter) geben wir Daten nur auf Grundlage eines gültigen Vertrags über Auftragsverarbeitung weiter.</p>
<h3>Widerruf Ihrer Einwilligung zur Datenverarbeitung</h3>
<p>Viele Datenverarbeitungsvorgänge sind nur mit Ihrer ausdrücklichen Einwilligung möglich. Sie können eine bereits erteilte Einwilligung jederzeit widerrufen. Die Rechtmäßigkeit der bis zum Widerruf erfolgten Datenverarbeitung bleibt vom Widerruf unberührt.</p>
<h3>Widerspruchsrecht gegen die Datenerhebung in besonderen Fällen (Art. 21 DSGVO)</h3>
<p>Wenn die Datenverarbeitung auf Grundlage von Art. 6 Abs. 1 lit. e oder f DSGVO erfolgt, haben Sie jederzeit das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, gegen die Verarbeitung Ihrer personenbezogenen Daten Widerspruch einzulegen; dies gilt auch für ein auf diese Bestimmungen gestütztes Profiling. Wir verarbeiten die betroffenen Daten dann nicht mehr, es sei denn, wir können zwingende schutzwürdige Gründe für die Verarbeitung nachweisen, die Ihre Interessen, Rechte und Freiheiten überwiegen, oder die Verarbeitung dient der Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen.</p>
<h3>Beschwerderecht bei der zuständigen Aufsichtsbehörde</h3>
<p>Im Falle von Verstößen gegen die DSGVO steht den Betroffenen ein Beschwerderecht bei einer Aufsichtsbehörde zu, insbesondere in dem Mitgliedstaat ihres gewöhnlichen Aufenthalts, ihres Arbeitsplatzes oder des Orts des mutmaßlichen Verstoßes. Das Beschwerderecht besteht unbeschadet anderweitiger verwaltungsrechtlicher oder gerichtlicher Rechtsbehelfe.</p>
<h3>Recht auf Datenübertragbarkeit</h3>
<p>Sie haben das Recht, Daten, die wir auf Grundlage Ihrer Einwilligung oder in Erfüllung eines Vertrags automatisiert verarbeiten, an sich oder an einen Dritten in einem gängigen, maschinenlesbaren Format aushändigen zu lassen. Sofern Sie die direkte Übertragung der Daten an einen anderen Verantwortlichen verlangen, erfolgt dies nur, soweit es technisch machbar ist.</p>
<h3>Auskunft, Berichtigung und Löschung</h3>
<p>Sie haben im Rahmen der geltenden gesetzlichen Bestimmungen jederzeit das Recht auf unentgeltliche Auskunft über Ihre gespeicherten personenbezogenen Daten, deren Herkunft und Empfänger und den Zweck der Datenverarbeitung und ggf. ein Recht auf Berichtigung oder Löschung dieser Daten. Hierzu sowie zu weiteren Fragen zum Thema personenbezogene Daten können Sie sich jederzeit an uns wenden.</p>
<h3>Recht auf Einschränkung der Verarbeitung</h3>
<p>Sie haben das Recht, die Einschränkung der Verarbeitung Ihrer personenbezogenen Daten zu verlangen. Hierzu können Sie sich jederzeit an uns wenden. Das Recht auf Einschränkung der Verarbeitung besteht in folgenden Fällen:</p>
<ul>
<li>Wenn Sie die Richtigkeit Ihrer bei uns gespeicherten Daten bestreiten, benötigen wir in der Regel Zeit, um dies zu überprüfen. Für die Dauer der Prüfung haben Sie das Recht, die Einschränkung der Verarbeitung zu verlangen.</li>
<li>Wenn die Verarbeitung Ihrer Daten unrechtmäßig geschah/geschieht, können Sie statt der Löschung die Einschränkung der Verarbeitung verlangen.</li>
<li>Wenn wir Ihre Daten nicht mehr benötigen, Sie sie jedoch zur Ausübung, Verteidigung oder Geltendmachung von Rechtsansprüchen benötigen, haben Sie das Recht, statt der Löschung die Einschränkung der Verarbeitung zu verlangen.</li>
<li>Wenn Sie einen Widerspruch nach Art. 21 Abs. 1 DSGVO eingelegt haben, muss eine Abwägung zwischen Ihren und unseren Interessen vorgenommen werden. Solange noch nicht feststeht, wessen Interessen überwiegen, haben Sie das Recht, die Einschränkung der Verarbeitung zu verlangen.</li>
</ul>
<p>Wenn Sie die Verarbeitung Ihrer personenbezogenen Daten eingeschränkt haben, dürfen diese Daten – von ihrer Speicherung abgesehen – nur mit Ihrer Einwilligung oder zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen oder zum Schutz der Rechte einer anderen natürlichen oder juristischen Person oder aus Gründen eines wichtigen öffentlichen Interesses der Europäischen Union oder eines Mitgliedstaats verarbeitet werden.</p>
<h3>SSL- bzw. TLS-Verschlüsselung</h3>
<p>Diese Seite nutzt aus Sicherheitsgründen und zum Schutz der Übertragung vertraulicher Inhalte eine SSL- bzw. TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie daran, dass die Adresszeile des Browsers von „http://“ auf „https://“ wechselt und an dem Schloss-Symbol in Ihrer Browserzeile. Wenn die SSL- bzw. TLS-Verschlüsselung aktiviert ist, können die Daten, die Sie an uns übermitteln, nicht von Dritten mitgelesen werden.</p>

<h2>4. Datenerfassung auf dieser Website</h2>
<h3>Server-Log-Dateien</h3>
<p>Der Provider der Seiten erhebt und speichert automatisch Informationen in so genannten Server-Log-Dateien, die Ihr Browser automatisch an uns übermittelt. Dies sind: Browsertyp und Browserversion, verwendetes Betriebssystem, Referrer URL, Hostname des zugreifenden Rechners, Uhrzeit der Serveranfrage und die IP-Adresse. Eine Zusammenführung dieser Daten mit anderen Datenquellen wird nicht vorgenommen. Die Erfassung dieser Daten erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO. Der Websitebetreiber hat ein berechtigtes Interesse an der technisch fehlerfreien Darstellung und der Sicherheit seiner Website – hierzu müssen die Server-Log-Files erfasst werden.</p>
<h3>Cookies</h3>
<p>Diese Website setzt keine Cookies und verwendet keine Analyse- oder Marketingdienste.</p>
<h3>Anfrage per E-Mail oder Telefon</h3>
<p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, etwa um die Patenschaft für einen Wagen zu übernehmen, wird Ihre Anfrage inklusive aller daraus hervorgehenden personenbezogenen Daten (Name, Anfrage) zum Zwecke der Bearbeitung Ihres Anliegens bei uns gespeichert und verarbeitet. Diese Daten geben wir nicht ohne Ihre Einwilligung weiter. Die Verarbeitung dieser Daten erfolgt auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO, sofern Ihre Anfrage mit der Erfüllung eines Vertrags zusammenhängt oder zur Durchführung vorvertraglicher Maßnahmen erforderlich ist. In allen übrigen Fällen beruht die Verarbeitung auf unserem berechtigten Interesse an der effektiven Bearbeitung der an uns gerichteten Anfragen (Art. 6 Abs. 1 lit. f DSGVO) oder auf Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), sofern diese abgefragt wurde. Die von Ihnen an uns übersandten Daten verbleiben bei uns, bis Sie uns zur Löschung auffordern, Ihre Einwilligung widerrufen oder der Zweck für die Datenspeicherung entfällt. Zwingende gesetzliche Bestimmungen – insbesondere gesetzliche Aufbewahrungsfristen – bleiben unberührt.</p>

<p class="recht__stand">Stand: Oktober 2026</p>
</div></section>'''

seite(VORSEITE, "Vorstellung", VORSTELLUNG)
seite("start.html", "Süßes für den Umzug", START)
seite("festzug.html", "Der Festzug", FESTZUG)
seite("ueber-uns.html", "Über uns", UEBER)
seite("impressum.html", "Impressum", IMPRESSUM)
seite("datenschutz.html", "Datenschutz", DATENSCHUTZ)
print("6 Seiten gebaut")
