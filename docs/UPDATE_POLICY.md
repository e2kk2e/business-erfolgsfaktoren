# Update Policy

## Zweck

Dieses Repository ist die kanonische Projektbasis. Neue Recherche darf bestehende Bewertungen nur ändern, wenn die Änderung nachvollziehbar dokumentiert und evidenzseitig begründet ist.

## Quellenklassen

- **A** – Primär/amtlich/offiziell/Standard
- **B** – starke Sekundärquelle mit nachvollziehbarer Herkunft
- **C** – Founder-Claim, Directory, Schätzung
- **D** – Demo, generiert, zufällig, unprüfbar

Klasse D ist für Core-Scoring ausgeschlossen.

## Freshness-SLAs

| Claim-Typ | Re-Check |
|---|---:|
| Startup ARR/Umsatz/Nutzer/Team/Funding | 30 Tage |
| Preise/APIs/Produktfeatures | 30 Tage |
| Regulatorische Fristen / Rechtsstand | 30 Tage |
| Marktgröße / Branchenkennzahlen | 90 Tage |
| stabile historische Fakten | 365 Tage |

## Update-Reihenfolge

1. Neue/aktualisierte Quelle erfassen.
2. Claim mit Datum, Typ, Quelle, Source Grade und Confidence aktualisieren.
3. Bei Widerspruch Primärquelle vor Sekundärquelle priorisieren.
4. Opportunity-/Evidence-/Catalyst-Scores nur bei relevanter Evidenz ändern.
5. `master/PROJECT_MASTER.md` synchronisieren.
6. Monatsreport unter `radar/updates/YYYY-MM.md` anlegen/aktualisieren.
7. Change Log ergänzen.

## Nicht zulässig

- Werte aus Demo-/Mock-Datensätzen in reale Benchmarks übernehmen.
- Founder-Claims als auditierte Fakten darstellen.
- alte und neue Metrikstände ohne Datum vermischen.
- „keine Evidenz gefunden“ als Gegenbeweis behandeln.
- Build-Freigabe nur aus Opportunity Score ableiten.
