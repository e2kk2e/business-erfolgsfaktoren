# Business Erfolgsfaktoren

Evidenzgesteuertes Lean-SaaS-/KI-SaaS-Venture-Studio-System für Deutschland/DACH.

## Ziel

Aus belastbaren Markt-, Startup-, Regulierungs- und Validierungssignalen wird **eine** fokussierte, profitabel und lean umsetzbare SaaS-Chance priorisiert. Ein hoher Ideen-Score allein löst keinen Produktbau aus.

**Kernprozess:**

`Research → Claims/Evidenz → Muster → Opportunity Radar → Ideen → Hard Filter → Opportunity Score → Evidence Score → Founder Fit → Paid Validation → MVP → Retention/Unit Economics`

## Aktueller Status

- Projektversion: **2.1**
- Stand: **2026-08-28**
- Hauptpriorität: **Elektro-LV Autoquote**
- Status: **VALIDATE NOW**
- Build-Gate: **kein Vollbau vor Zahlungsbeweis**

## Repository-Struktur

| Pfad | Zweck |
|---|---|
| `master/PROJECT_MASTER.md` | kanonischer Projektstand |
| `data/business_idea_success_filter.json` | maschinenlesbarer Bewertungsstandard |
| `data/source_registry.json` | Vertrauens-/Provenienzregister der Projektquellen |
| `data/claims.json` | strukturierte, zeitgebundene Claims und Freshness |
| `data/opportunity_radar.json` | priorisierte Chancen/Katalysatoren |
| `sources/verified/` | bevorzugte Forschungsquellen |
| `sources/unverified/` | Alt-/Demo-/unverifizierte Materialien; nie direkt für Core-Scoring |
| `radar/updates/` | monatliche Radar-Updates |
| `docs/UPDATE_POLICY.md` | Regeln für Aktualisierung und Evidenz |
| `scripts/` | Validierung/Freshness-Prüfung |
| `.github/workflows/` | CI + monatliches Freshness-Gate |

## Qualitätsregeln

1. Keine Zahl ohne Quelle oder explizite Hypothesenmarkierung.
2. ARR, Umsatz, Funding, Nutzer, Traffic und Profit nie als dieselbe Metrik behandeln.
3. Demo-/generierte Daten sind für Core-Scoring gesperrt.
4. Founder-Claims als Founder-Claims kennzeichnen.
5. Jede zeitabhängige Kennzahl braucht `as_of_date` und `last_verified_at`.
6. Score und Evidenz strikt trennen.
7. Kein Full Build ohne Zahlungsbeweis.
8. Nur ein aktives MVP gleichzeitig.
9. DACH-Regeln mindestens monatlich neu verifizieren.
10. Änderungen im Change Log dokumentieren.

## Monatlicher Update-Mechanismus

Am 1. jedes Monats prüft GitHub Actions die Freshness der strukturierten Claims. Veraltete bzw. noch nicht extern verifizierte Claims werden in einem Report markiert; zusätzlich wird ein GitHub-Issue für das erforderliche Research-Update erzeugt.

Der Workflow **erfindet keine neuen Marktwerte** und ersetzt keine Quellenrecherche. Nach einer Research-Aktualisierung werden `claims.json`, `opportunity_radar.json`, `PROJECT_MASTER.md` und der Monatsreport gemeinsam aktualisiert.

## Nächste operative Aufgabe

14-Tage-Zahlungsvalidierung für **Elektro-LV Autoquote**:

- 50 Zielbetriebe
- 10 Interviews
- reale/anonymisierte LVs + Preislisten
- Concierge-Test
- Paid-Pilot-Angebot
- Evidence Score aktualisieren
- Entscheidung: `BUILD`, `PIVOT` oder `KILL`
