# Business Erfolgsfaktoren – Projekt-Master v2.1

**Stand:** 28.08.2026  
**Ziel:** Aus belastbaren Markt-, Startup-, Regulierungs- und Validierungssignalen ein schlankes, profitables, automatisierbares KI-/Micro-SaaS für Deutschland/DACH ableiten und nur nach Zahlungsbeweis bauen.

## 1. Kurzfazit

Das Projekt wird von einer Ideensammlung zu einem **evidenzgesteuerten Venture-Studio-System** umgebaut:

**Research → Claims/Evidenz → Muster → Opportunity Radar → Ideen → Hard Filter → Opportunity Score → Evidence Score → Founder Fit → Paid Validation → MVP → Retention/Unit Economics.**

Die wichtigste strategische Änderung lautet: **kein Produktbau aufgrund eines hohen Ideen-Scores allein.** Ein Score beschreibt Attraktivität, nicht Nachfrage. Vollbau ist erst erlaubt, wenn echte Evidenz und Zahlungsbereitschaft vorliegen.

### Aktuelle Hauptpriorität

**Elektro-LV Autoquote** bleibt die beste Startnische des aktuellen Portfolios.

Zielkunde: Elektrohandwerksbetriebe mit ca. 5–50 Mitarbeitenden.  
Kernjob: GAEB-X83-/PDF-Leistungsverzeichnisse einlesen, kundeneigene Materialpreise und Lohnfaktoren zuordnen, Lücken markieren und eine prüfbare Angebotskalkulation erzeugen.  
Der vorhandene Projekt-Report bewertet diese Nische mit **88/100**. Dieser Wert ist eine modellbasierte Priorisierung, kein Nachfragebeweis.

**Build-Entscheidung:** Noch kein Vollbau. Zuerst 14 Tage Zahlungsvalidierung.

---

## 2. Quellenbereinigung

### Kanonische Quellenklassen

| Klasse | Zulässig für Scores? | Beispiele |
|---|---:|---|
| A – Primär/amtlich | Ja | Behörden, Gesetze, Standards, offizielle Unternehmens-Metriken |
| B – starke Sekundärquelle | Ja, mit Kennzeichnung | Reuters, TechCrunch, Sifted, Branchenverbände |
| C – Founder-/Directory-Claim | Nur mit Abschlag | Founder-Posts, Revenue-Directories, nicht auditierte Claims |
| D – Demo/generiert/unverifiziert | Nein | zufällig erzeugte Beispiel-Startups, generische Platzhalter, unbelegte Zahlen |

### Korrektur

Die frühere Gemini-Webapp enthält demonstrative und teilweise per Zufall erzeugte Startup-Daten. Diese Daten werden **aus allen Benchmarks, Häufigkeitsangaben, ARR-/Team-Analysen und Scores ausgeschlossen**. Die Webapp kann nur noch als UI-Prototyp dienen.

### Pflichtfelder für jede externe Behauptung

- `entity`
- `metric_type` (ARR, Umsatz, Profit, Nutzer, Kunden, Funding, Traffic usw.)
- `value`
- `currency/unit`
- `as_of_date`
- `source_url`
- `source_grade`
- `claim_type` (official / media / founder / estimate)
- `confidence`
- `last_verified_at`

**Regel:** ARR, Umsatz, Funding, Nutzer, Traffic und Profit dürfen niemals in einer gemeinsamen Wachstumskennzahl vermischt werden.

---

## 3. Aktualisierte Marktsignale 2026

### Startup-Geschwindigkeit

Stripe berichtet für die 2025er Startup-Kohorte:
- rund 50 % schnelleres Wachstum als die 2024er Kohorte,
- doppelt so viele Unternehmen erreichten innerhalb von drei Monaten 10 Mio. USD ARR,
- 20 % der Atlas-Startups belasteten den ersten Kunden innerhalb von 30 Tagen.

Das bestätigt: **Time-to-Revenue wird zu einem zentralen Qualitätsmaß.**

### DACH-Beispiele

**Langdock:** Offizieller Meilenstein von **50 Mio. USD ARR im August 2026**. Das Muster ist für DACH besonders wichtig: sichere, modellunabhängige Unternehmens-KI + Integrationen + Agents + Workflows.

**Peec AI:** Offiziell 0 → 4 Mio. USD+ ARR in zehn Monaten; inzwischen 3.000+ Marketingteams. Das zeigt die Stärke neuer Kategorien, wenn ein klarer Budget-Shift entsteht – hier AI Search/GEO.

### Regulatorische Kaufanlässe

- **EU AI Act Art. 50:** Transparenzpflichten gelten seit 02.08.2026.
- **NIS2 Deutschland:** Umsetzungsgesetz seit 06.12.2025 in Kraft; BSI-Registrierungs-/Meldeprozesse sind aktiv.
- **E-Rechnung Deutschland:** Empfangspflicht seit 01.01.2025; Übergangsfristen für Ausstellung laufen bis Ende 2026 bzw. für kleinere Rechnungsaussteller bis Ende 2027.

Diese Signale werden in den Opportunity Radar aufgenommen. Sie rechtfertigen **keine generischen Compliance-Wrapper**, sondern vertikale Workflow-Produkte mit prüfbarem Output.

---

## 4. Aktualisierte Erfolgsfaktoren

### Tier 1 – Muss erfüllt sein

1. **Enger ICP mit Budget Owner**
2. **Akuter, wiederkehrender Workflow-Pain**
3. **Messbarer ROI in Euro, Zeit, Fehlern oder Risiko**
4. **Time-to-Value unter 10–30 Minuten**
5. **MVP in 7–21 Tagen testbar**
6. **Self-Serve oder sehr leichter Founder-led Sale**
7. **Mindestens ein konkret testbarer Distributionskanal**
8. **Automatisierungsgrad ≥80 %, Ziel ≥90 %**
9. **Bruttomarge ≥70 %, Ziel ≥80 %**
10. **Retention durch Datenhistorie, Integration, Alerts, Reports oder Teamworkflow**
11. **Differenzierung durch Workflow, Daten, UX, Integration, DACH-/Compliance-Vorteil**
12. **Recht, Datenschutz und Plattformabhängigkeit kontrollierbar**

### Tier 2 – Beschleuniger

- externe Regulierungs-/Technologie-/Kosten-Katalysatoren
- Plattform-/Marketplace-Distribution
- offene Standards / OSS-Wedge
- Free Tool / Benchmark / Calculator als Lead Magnet
- virale oder teilbare Outputs
- usage-/ROI-nahes Pricing
- „agentic workflow“ nur dort, wo Aktionen verlässlich und auditierbar sind
- AI als Kostenkompressor im Betrieb, nicht nur als sichtbares Feature

### Tier 3 – Warnsignale

- generischer ChatGPT-Wrapper
- kein Budget Owner
- „alle KMU“ als Zielgruppe
- Enterprise-Sales als einzige Startdistribution
- aktive Abhängigkeit von riskantem Scraping
- hoher manueller Serviceanteil
- Hardware-/Sensorpflicht im ersten MVP
- rechtliche Entscheidung ohne Human Review
- einmaliger Use Case ohne Wiederkehr
- Profit-/ARR-/User-Zahlen nur aus schwachen Founder-Claims

---

## 5. Bewertungsmodell v2.1

Das bisherige 100-Punkte-Opportunity-Modell bleibt für Vergleichbarkeit erhalten. Neu hinzu kommen drei getrennte Scores.

### A. Opportunity Score – 0 bis 100

Bewertet Markt, Problem, Produkt, Wachstum, Retention, Revenue, Skalierung, Differenzierung und Risiko.

### B. Evidence Score – 0 bis 100

- Kundeninterviews – 30 %
- Zahlungsbereitschaft / Paid Pilots – 25 %
- bestehende Ausgaben für Alternative/Personal – 20 %
- Such-/Community-Nachfrage – 15 %
- belegter manueller Workaround – 10 %

**Gates:**
- `<30`: Research only
- `>=30`: Paid MVP testbar
- `>=50`: Vollbau zulässig

### C. Founder / Execution Fit – 0 bis 100

- Domainverständnis – 25 %
- Zugang zu Käufern – 20 %
- technischer Build-Fit – 20 %
- Glaubwürdigkeit/Vertrauen – 15 %
- Support-/Betriebsfit – 10 %
- Kapitalfit – 10 %

### D. Catalyst Score – 0 bis 100

- Regulierung / Deadline – 25 %
- Technologie-Reife – 25 %
- Kosten-/Margendruck – 20 %
- Plattform-/Datenänderung – 15 %
- Wettbewerbsfenster – 15 %

### Prioritätsformel

Nur wenn kein kritischer Hard Filter aktiv ist:

`Priority = 0.45*Opportunity + 0.25*Evidence + 0.15*FounderFit + 0.15*Catalyst`

**Wichtig:** Ein niedriger Evidence Score blockiert den Build unabhängig vom gewichteten Priority Score.

---

## 6. Portfolio-Bereinigung

### Primär

#### Elektro-LV Autoquote
**Status:** VALIDATE NOW  
**Warum:** enger B2B-Workflow, hoher potenzieller Zeit-ROI, standardisierte GAEB-Daten, klarer DACH-Fokus, geringe Abhängigkeit von Frontier-Modellen.  
**Offen:** echte LVs, Preislisten, Zeitersparnis, Zahlungsbereitschaft.

### Sekundär / getrennt weiterführen

#### KryptoEvidence MSP
**Status:** VALIDATE, kein breiter Produktbau.  
Vorhandener Plan fordert explizit zwei zahlende MSP-Piloten vor weiterem Ausbau. Stärkerer Moat, aber höhere Security-/Compliance- und Vertriebsfriktion.

#### Ausschreibungs-Intelligence / DaaS
**Status:** RESEARCH / VALIDATE.  
Guter wiederkehrender Daten-Use-Case, aber Datenzugang, Quellenrechte, Matching-Qualität und Käuferbudget müssen vor Build belegt werden.

### Herabstufung alter High-Scores

- **Property-Tax-Appeal-Bot:** hoher Einmalnutzen, aber schwache Wiederkehr + Legal-Risiko.
- **Cold-Email-Personalizer:** commoditized, Plattform-/Scraping-/ToS-Risiko.
- **LinkedIn Ghostwriter:** schwächerer akuter Pain und schwerer messbarer ROI.
- **Generischer DSGVO-/Compliance-Bot:** Haftungs-/Rechtsrisiko; nur als Evidence-/Assistenz-Workflow sinnvoll.

---

## 7. Zielprodukt: Elektro-LV Autoquote

### 1. Zielgruppe
Elektrohandwerksbetriebe in Deutschland mit etwa 5–50 Mitarbeitenden, die regelmäßig Ausschreibungen/LVs kalkulieren.

### 2. Konkretes Problem
Leistungsverzeichnisse müssen manuell gelesen, Positionen Material-/Lohnpreisen zugeordnet und Angebotslücken geprüft werden. Der Workflow ist repetitiv und fehleranfällig.

### 3. Warum dringend/teuer
Kalkulationszeit ist nicht produktive Baustellenzeit. Fehlende oder falsch bewertete Positionen können Marge kosten. Der monetäre Wert muss im Pilot gemessen werden.

### 4. Lösung
Cloud-Tool, das GAEB-X83 oder PDF-LVs einliest, Positionen strukturiert, kundeneigene Preislisten/Lohnfaktoren anwendet, Unsicherheiten markiert und eine nachvollziehbare Kalkulation exportiert.

### 5. MVP-Funktionen
1. LV-Import (GAEB X83 + PDF-Fallback)
2. Preislisten-/Lohnfaktor-Mapping
3. prüfbare Kalkulation mit Confidence-/Lückenmarkierung und Excel/PDF-Export

### 6. Automatisierung
Deterministisches Parsing und Rechnen zuerst. LLM nur für unstrukturierte Texte, Klassifikation und Mapping-Vorschläge. Keine versteckte KI-Entscheidung ohne Herkunft/Confidence.

### 7. Monetarisierung
Hypothese: monatliches Abo mit Grundkontingent und Usage-Aufpreis. Preis wird erst nach gemessener Zeitersparnis finalisiert.

### 8. Go-to-Market
Founder-led Direktansprache an Elektrofirmen + Innungs-/Branchenkontakte + kostenlose „LV-Zeitkosten“-Analyse als Lead Magnet.

### 9. Technische Architektur
- Web-App
- Python Backend
- Postgres
- GAEB/XML Parser
- PDF-/Tabellenparser
- deterministische Kalkulationsengine
- LLM-Fallback für Mapping
- Job Queue
- Objektstorage
- Audit Log
- EU-Hosting
- Stripe erst nach Pilot

### 10. Kern-Datenmodell
- Organization
- User
- Project
- Tender/LV
- LVPosition
- PriceCatalog
- PriceItem
- LaborFactor
- Mapping
- CalculationRun
- Finding/Gap
- Export
- AuditEvent

### 11. Hauptrisiken
- reale LVs unterscheiden sich stark
- Preislistenformate uneinheitlich
- bestehende AVA-/Kalkulationssoftware könnte ausreichend sein
- falsche Zuordnung kann Vertrauen zerstören
- Datenschutz/Vertraulichkeit von Ausschreibungsunterlagen

---

## 8. 14-Tage-Validierungsplan

### Tage 1–2
- ICP fixieren
- 50 konkrete Zielbetriebe erfassen
- Landingpage + 1-Minuten-Demo-Mockup
- Interviewleitfaden und Pilotangebot

**Gate:** 50 echte Leads + klare Buyer-Rolle.

### Tage 3–5
- 20–30 gezielte Kontakte
- mindestens 10 Gespräche
- fünf anonymisierte LVs
- mindestens zwei reale Preislistenformate

**Gate:** mindestens fünf Betriebe bestätigen denselben Kalkulations-Pain.

### Tage 6–8
Concierge-Prototyp: 3 reale LVs halbmanuell durch den Zielworkflow schicken.

**Messung:**
- aktuelle Bearbeitungszeit
- Zeit mit Prototype
- Korrekturen
- Fehler-/Lückenquote
- Vertrauen in Output

**Gate:** bei mindestens zwei Testfällen ≥60 Minuten Zeitersparnis oder vergleichbarer wirtschaftlicher Nutzen.

### Tage 9–11
- bezahltes Pilotangebot
- Preis als Hypothese testen
- keine kostenlose Dauerbeta

**Gate:** mindestens zwei verbindlich zahlende Piloten oder schriftliche Zahlungszusage.

### Tage 12–14
- Ergebnisse in Evidence Score eintragen
- Opportunity Score nur bei neuen Fakten ändern
- Kill/Pivot/Build-Entscheidung

**Build nur wenn:**
- keine kritischen Hard Filter,
- Opportunity Score ≥75,
- Evidence Score ≥30 für Paid MVP,
- klarer wiederholbarer Datenworkflow.

---

## 9. Produktarchitektur des Gesamtprojekts

Das Projekt selbst sollte als **Lean SaaS Intelligence OS** geführt werden:

### Module
1. **Source Vault** – Quellen + Claims + Verifizierungsstatus
2. **Startup Database** – Unternehmen und getrennte Metriktypen
3. **Pattern Engine** – Erfolgsfaktoren mit Evidenzzählung
4. **Opportunity Radar** – Regulierungen, Plattformänderungen, neue APIs, Marktprobleme
5. **Idea Registry** – Ideen mit ICP, Problem, Buyer, Workaround, ROI
6. **Validator** – Hard Filter + Opportunity/Evidence/Founder/Catalyst
7. **Experiment Tracker** – Interviews, Landingpage, Outreach, Pilot, Zahlung
8. **Decision Log** – Research / Reject / Pivot / Validate / Build
9. **Portfolio Board** – genau ein aktives Build-Projekt; Rest Watchlist
10. **Change Log** – jede neue Quelle kann Scores nachvollziehbar verändern

### Wichtigste UI-Ansichten
- Executive Dashboard
- Claims & Source Quality
- Startup Explorer
- Success Factor Matrix
- Opportunity Radar
- Idea Validator
- Experiment Board
- Portfolio Ranking
- Decision History

---

## 10. Qualitätsregeln

1. Keine Zahl ohne Quelle oder explizite Hypothesenmarkierung.
2. Keine Demo-/KI-generierten Daten im Forschungsdatensatz.
3. Founder-Claims niemals als auditierte Fakten darstellen.
4. Jede Startup-Metrik braucht ein Datum.
5. Keine Kausalität aus bloßer Häufigkeit ableiten.
6. Score und Evidenz strikt trennen.
7. Kein Full Build ohne Zahlungsbeweis.
8. Nur ein aktives MVP gleichzeitig.
9. DACH-Regeln monatlich neu verifizieren.
10. Projektentscheidungen im Change Log festhalten.

---

## 11. Nächster konkreter Schritt

**Jetzt nicht weiter brainstormen.**  
Als nächstes wird der 14-Tage-Test für **Elektro-LV Autoquote** ausgeführt und der Evidence Score real befüllt.

Der erste operative Deliverable ist:
- 50-Betriebe-Leadliste,
- 10-Interview-Skript,
- Pilot-Landingpage,
- Muster-Datenanforderung für LV + Preislisten,
- Paid-Pilot-Angebot,
- Evidence-Score-Sheet.
