# ID-Bot

## Chatbot mit OpenAI und PDF-Unterstützung

Ein einfacher Chatbot, der Fragen basierend auf PDF-Dokumenten und Textdateien beantwortet. Der Bot nutzt OpenAI's GPT-4o-mini und antwortet im Stil von Shakespeare auf Deutsch.

## Features

- 📄 Lädt automatisch PDFs, Markdown und Textdateien
- 🤖 Nutzt OpenAI GPT-4o-mini
- 💬 Streaming-Antworten in Echtzeit
- 🖥️ Gradio-Oberfläche

## Voraussetzungen

- Python 3.8 oder höher
- OpenAI API Key

## Installation

### 1. Repository klonen 
bitte dieses Repository clonen mit
```
git clone https://github.com/ID-Prototyping-Winter25/ID-Bot.git
cd ID-Bot
```

### 2. Virtuelle Umgebung erstellen

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4. OpenAI API Key einrichten

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="dein-api-key-hier"
```

**Windows (CMD):**
```cmd
set OPENAI_API_KEY=dein-api-key-hier
```

**macOS/Linux:**
```bash
export OPENAI_API_KEY="dein-api-key-hier"
```

### 5. Projektstruktur einrichten

Stelle sicher, dass folgende Ordnerstruktur existiert:
```
projektordner/
│
├── main.py                    # Hauptdatei
├── theme.py                   # Theme-Konfiguration
├── requirements.txt           # Python-Abhängigkeiten
├── style.css                  # (optional) CSS-Styling
│
├── modulhandbuch/            # Deine Dokumente hier ablegen
│   ├── dokument1.pdf
│   ├── dokument2.txt
│   └── ...
│
└── avatar_images/            # Avatar-Bilder
    ├── human.png
    └── robot.png
```

### 6. Dokumente hinzufügen

Lege deine PDF-, TXT- oder MD-Dateien in den `modulhandbuch/` Ordner.

## Verwendung

### Chatbot starten
```bash
python app.py
```

Der Chatbot öffnet sich automatisch in deinem Browser unter `http://localhost:7860`

### Virtuelle Umgebung deaktivieren

Wenn du fertig bist:
```bash
deactivate
```

## Konfiguration

### Model ändern

In `app.py`, Zeile mit `model=`:
```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",  # Ändere zu "gpt-4o" oder "gpt-3.5-turbo"
    ...
)
```

### Temperatur anpassen
```python
temperature=0.1,  # 0.0 = deterministisch, 1.0 = kreativ
```

### Prompt anpassen

Bearbeite die `SYSTEM_PROMPT` Variable in `app.py`:
```python
SYSTEM_PROMPT = f"""Du bist ein hilfreicher Assistent...
Antworte immer auf Deutsch und im Stil von Shakespeare.  # Hier ändern
"""
```

## Fehlerbehebung

### "OpenAI API Key nicht gefunden"
- Stelle sicher, dass die Umgebungsvariable `OPENAI_API_KEY` gesetzt ist
- Überprüfe mit: `echo $OPENAI_API_KEY` (macOS/Linux) oder `echo %OPENAI_API_KEY%` (Windows)

### "Modul nicht gefunden"
- Aktiviere die virtuelle Umgebung
- Installiere die Abhängigkeiten erneut: `pip install -r requirements.txt`

### PDFs werden nicht richtig gelesen
- Versuche `pdfplumber` statt `PyPDF2`
- Ändere in `requirements.txt`: `PyPDF2` → `pdfplumber`
- Passe den Code entsprechend an (siehe Kommentare im Code)

### Zu langer Kontext
Falls deine Dokumente zu groß sind:
- Nutze weniger Dokumente
- Implementiere eine Vektor-Datenbank (z.B. mit ChromaDB oder Pinecone)
- Wechsle zu einem Modell mit größerem Context-Window

## Kosten

- GPT-4o-mini: ~$0.15 / 1M Input Tokens, ~$0.60 / 1M Output Tokens
- Aktuelle Preise: https://openai.com/api/pricing/

