# Project Edu Wiki - Features 🌟

## 📑 Inhaltsverzeichnis 

### Weitere Seiten
| **Seite** | **Beschreibung** |
|-|-|
| [Projektübersicht](01_Projektübersicht.md) | Einführung in das Projekt und seine Ziele, inklusive der Struktur und Motivation. |
| [Features](02_Features.md) | Beschreibung der geplanten Funktionen des Bots, wie Stundenplan, Benachrichtigungen und Statistiken. |
| [Voraussetzungen und benutzte Libraries](03_Voraussetzungen.md) | Technische Anforderungen und verwendete Libraries im Projekt. |
| [Zeitplan](04_Zeitplan.md) | Übersicht des Projektzeitplans und der Meilensteine. |
| [Reflexion und Herausforderungen](05_Reflexion.md) | Reflexion und Dokumentation von Herausforderungen, Schwierigkeiten und Lernerfahrungen im Projekt. |

---

### Diese Seite
- **Aktuelle Features** ✨
    - aktuell implementierte Features
- **Geplante Features** 🔮
    - Features, an denen zurzeit gearbeitet wird
    - Ideen für neue Features
- **Versions Benennung** 🏷️
    - nach welcher Struktur die Versionen benannt werden

---

## ✨ Aktuelle Features

Zum aktuellen Stand (**24-09-24**) sind folgende Features bereits implementiert und funktionieren einwandfrei:

- **Welcome Nachricht** -> Nachricht an neue Discord Mitglieder
- **Github Update Kanal**
- **Discord und Terminal Logging-System**
- **User Commands**:
    - `/botping` -> gibt den Ping des Bots wieder
- **Dev Commands**:
    - `/createuserpanel` -> Erstellt das User-Panel neu
    - `/reload` -> lädt alle Commands neu (kann länger dauern)
    - `/stopbot` -> Stoppt den Bot sofort
- **EduPage API Commands**:
    - `/schüleranzahl` -> Gibt die Anzahl an Schülern in EduPage an
    - `/stundenplan` -> gibt den persönlichen Stundenplan für ein beliebiges Datum an
    - `/nutzerdaten` -> Login-Daten ändern
- **User-Panel**:
    - Login und Logout Buttons

---

## 🔮 Geplante Features 

- **EduPage Benachrichtigungen** 
    - Raumänderungen
    - Vertretungen / Ausfall
    - Ankündigungen
    - Hausaufgaben
- **Fächer-/Kursinformationen** 
    - Details zu Lehrer, Räumen, etc.
- **Erinnerungen** 
    - Anstehende Hausaufgaben
    - Bevorstehende Tests/Klausuren
- **Statistiken** 
    - Schüler-/Lehreranzahl
    - Bot Benutzer
    - Klassen-/Kursanzahl
- ...

---

## 🏷️ Versions Benennung

Die Versionsbenennung basiert auf der [Semantic Versioning](https://semver.org/lang/de/), ist jedoch teils eigenständig verändert worden.

### Schema:

`MAJOR.MINOR.PATCH`

- **MAJOR**: Nicht abwärtskompatible Änderungen
- **MINOR**: Neue Features, abwärtskompatibel
- **PATCH**: Fehlerbehebungen und kleine Änderungen

---

### 🌿 Branches

- **`release`**: Dies ist der stabile Branch, der nur vollständig getestete und freigegebene Versionen enthält.

- **`rc`**: Der Release-Candidate-Branch (rc) enthält Versionen, die als potenziell stabil gelten und zur finalen Prüfung bereit sind. Er dient dazu, letzte Tests vor der Veröffentlichung im `release` Branch durchzuführen. Enthält den `-rc` Tag im Versionsnamen.

- **`testing`**: Dieser Branch wird verwendet, um experimentelle Funktionen oder Bugfixes zu testen, die noch nicht vollständig implementiert oder stabil sind. Er ist weniger stabil als der `rc` Branch. Enthält den `-beta` Tag im Versionsnamen.

- **`dev`**: Der Entwicklungs-Branch, in dem neue Funktionen und Änderungen zuerst implementiert werden. Hier finden die meisten Entwicklungsarbeiten statt. Sobald eine Funktion stabil genug ist, wird sie zu `testing` verschoben. Enthält den `-alpha` Tag im Versionsnamen.

---

### 📦 Pre-Releases:

Pre-Releases werden mit einem Tag wie `-alpha`, `-beta` oder `-rc` angegeben. Sie dienen zum Testen neuer Funktionen vor dem offiziellen Release.

**Beispiele**:
- `1.2.0-alpha.1`: Eine frühe Testversion für die neue 1.2.0 Version
- `1.2.0-beta.2`: Eine stabilere, aber noch nicht finale Version
- `1.2.0-rc.1`: Ein möglicher Release-Kandidat für die endgültige Version
