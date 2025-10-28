import os
import time
import gradio as gr
from openai import OpenAI
import PyPDF2

from theme import CustomTheme

# OpenAI Client initialisieren
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Dokumente aus dem Modulhandbuch-Ordner laden
def load_documents(path="./modulhandbuch/"):
    """Lädt alle Textdateien und PDFs aus dem angegebenen Ordner"""
    context = ""
    
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        
        # Überspringe Verzeichnisse
        if os.path.isdir(filepath):
            continue
            
        try:
            # PDF-Dateien
            if filename.endswith('.pdf'):
                with open(filepath, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    context += f"\n\n--- {filename} ---\n"
                    for page_num, page in enumerate(pdf_reader.pages, 1):
                        text = page.extract_text()
                        if text.strip():
                            context += f"\n[Seite {page_num}]\n{text}\n"
            
            # Text-Dateien
            elif filename.endswith(('.txt', '.md')):
                with open(filepath, 'r', encoding='utf-8') as f:
                    context += f"\n\n--- {filename} ---\n"
                    context += f.read()
                    
        except Exception as e:
            print(f"Fehler beim Laden von {filename}: {e}")
    
    return context

# Kontext beim Start laden
print("Lade Dokumente...")
CONTEXT = load_documents()
print(f"Kontext geladen: {len(CONTEXT)} Zeichen")

# System Prompt mit Kontext
SYSTEM_PROMPT = f"""Du bist ein hilfreicher Assistent, der Fragen basierend auf dem folgenden Kontext beantwortet.

KONTEXT:
---------------------
{CONTEXT}
---------------------

Beantworte Fragen NUR basierend auf diesem Kontext. Nutze NICHT dein allgemeines Wissen.
Antworte auf Deutsch und gibt immer die Seitenzahl an, von der Seite auf der die Information steht, die Du ausgibst.
"""


def response(message, history):
    """Generiert eine Antwort mit OpenAI Streaming"""
    
    # Konvertiere Gradio history Format zu OpenAI messages Format
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for msg in history:
        if msg["role"] == "user":
            messages.append({"role": "user", "content": msg["content"]})
        elif msg["role"] == "assistant":
            messages.append({"role": "assistant", "content": msg["content"]})
    
    messages.append({"role": "user", "content": message})
    
    # Streaming-Anfrage an OpenAI
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.1,
        stream=True
    )
    
    answer = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            text = chunk.choices[0].delta.content
            time.sleep(0.05)
            answer += text
            yield answer


theme = CustomTheme()

def main():
    chatbot = gr.Chatbot(
        value=[{"role": "assistant", "content": "Wie kann ich Dir helfen?"}],
        type="messages",
        show_label=False,
        avatar_images=("./avatar_images/human.png", "./avatar_images/robot.png"),
        elem_id="CHATBOT"
    )

    chatinterface = gr.ChatInterface(
        fn=response,
        chatbot=chatbot,
        type="messages",
        theme=theme,
        css_paths="./style.css"
    )

    chatinterface.launch(inbrowser=True)


if __name__ == "__main__":
    main()