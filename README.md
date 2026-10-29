# VoFe Wagenpaten

Homepage „Wagenpaten – Volksfestumzug der Schulen 2027“ (Crailsheim).

## Branches
- `daniel`: Arbeitsstand mit Menüpunkt „/ Entwicklung /“. Hier wird gearbeitet.
- `main`: Live-Stand. Etwas kommt nur auf ausdrücklichen Auftrag von Daniel hierher,
  und nie Inhalte aus „/ Entwicklung /“ (Ordner `entwicklung/`, Blöcke `ENTWICKLUNG:START` … `ENTWICKLUNG:END`).

## Schutz
- `werkzeuge/main-schutz.sh` läuft bei Vercel als Build-Befehl und bricht auf `main` ab, sobald Entwicklungsinhalte enthalten sind.
- Lokal stoppt `~/Projekte/.git-hooks` (per `core.hooksPath`) Commit und Push auf `main` mit Entwicklungsinhalten.
