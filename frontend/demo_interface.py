import tkinter as tk
from tkinter import scrolledtext
import requests
import threading
import re

API_URL = "http://127.0.0.1:8000/chat"

COLOR_PRIMARY = "#006837"
COLOR_PRIMARY_HOVER = "#004D28"
COLOR_BG = "#F4F6F8"
COLOR_WHITE = "#FFFFFF"
COLOR_TEXT_DARK = "#0F1B29"
COLOR_BORDER = "#CBD5E1"

window = tk.Tk()
window.title("STAR Assurances - Assistant AI")
window.geometry("750x850")
window.configure(bg=COLOR_BG)

# ================= HEADER =================
header_frame = tk.Frame(window, bg=COLOR_PRIMARY, height=70)
header_frame.pack(fill="x", side="top")
header_frame.pack_propagate(False)

tk.Label(
    header_frame, text="★ STAR ASSURANCES",
    font=("Segoe UI", 15, "bold"), fg=COLOR_WHITE, bg=COLOR_PRIMARY
).pack(anchor="w", padx=20, pady=(10, 0))

tk.Label(
    header_frame, text="Assistant Virtuel & Téléassistance",
    font=("Segoe UI", 9), fg="#A7F3D0", bg=COLOR_PRIMARY
).pack(anchor="w", padx=20)

# ================= CHAT CONTAINER =================
chat_frame = tk.Frame(window, bg=COLOR_BG)
chat_frame.pack(padx=20, pady=10, fill="both", expand=True)

chat_box = scrolledtext.ScrolledText(
    chat_frame, wrap=tk.WORD, font=("Segoe UI", 10),
    bg=COLOR_WHITE, fg=COLOR_TEXT_DARK, bd=0,
    highlightthickness=1, highlightbackground=COLOR_BORDER,
    padx=15, pady=15
)
chat_box.pack(fill="both", expand=True)

# Configuration mtaa el Alignement
chat_box.tag_configure("bot_header", font=("Segoe UI", 10, "bold"), foreground=COLOR_PRIMARY, justify="left", spacing1=10, spacing3=2)
chat_box.tag_configure("bot_text", font=("Segoe UI", 10), foreground=COLOR_TEXT_DARK, justify="left", spacing2=2)

chat_box.tag_configure("user_header", font=("Segoe UI", 10, "bold"), foreground="#2563EB", justify="right", spacing1=10, spacing3=2)
chat_box.tag_configure("user_text", font=("Segoe UI", 10), foreground=COLOR_TEXT_DARK, justify="right", spacing2=2)

chat_box.tag_configure("typing_text", font=("Segoe UI", 9, "italic"), foreground="#64748B", justify="left", spacing2=2)

# ================= TYPING INDICATOR (ATTENTE API) =================
is_typing = False
typing_dots = 0

def animate_typing():
    global typing_dots
    if not is_typing:
        return

    chat_box.config(state="normal")
    if "typing_start" in chat_box.mark_names():
        chat_box.delete("typing_start", tk.END)

    dots = "." * (typing_dots % 4)
    chat_box.insert(tk.END, "\n● STAR AI\n", "bot_header")
    chat_box.insert(tk.END, f"est en train d'écrire{dots}\n", "typing_text")
    
    chat_box.config(state="disabled")
    chat_box.see(tk.END)

    typing_dots += 1
    window.after(400, animate_typing)

def show_typing():
    global is_typing, typing_dots
    if is_typing:
        return
    is_typing = True
    typing_dots = 0
    
    chat_box.config(state="normal")
    chat_box.mark_set("typing_start", "end-1c")
    chat_box.mark_gravity("typing_start", tk.LEFT)
    chat_box.config(state="disabled")
    
    animate_typing()

def hide_typing():
    global is_typing
    is_typing = False
    chat_box.config(state="normal")
    if "typing_start" in chat_box.mark_names():
        chat_box.delete("typing_start", tk.END)
        chat_box.mark_unset("typing_start")
    chat_box.config(state="disabled")

def clean_markdown(text):
    return re.sub(r'\*\*(.*?)\*\*', r'\1', text)

# ================= TYPEWRITER EFFECT (REPONSE BOT) =================
def add_bot_stream_message(text):
    chat_box.config(state="normal")
    cleaned_text = clean_markdown(text)
    
    if chat_box.get("1.0", tk.END).strip():
        chat_box.insert(tk.END, "\n")
    
    chat_box.insert(tk.END, "● STAR AI\n", "bot_header")
    
    index = 0
    chunk_size = 2  # Yiktib 2 caractères kol 12ms bech tji fluide w rapide

    def type_chunk():
        nonlocal index
        if index < len(cleaned_text):
            chat_box.config(state="normal")
            chunk = cleaned_text[index:index + chunk_size]
            chat_box.insert(tk.END, chunk, "bot_text")
            chat_box.config(state="disabled")
            chat_box.see(tk.END)
            index += chunk_size
            window.after(12, type_chunk)
        else:
            chat_box.config(state="normal")
            chat_box.insert(tk.END, "\n", "bot_text")
            chat_box.config(state="disabled")
            chat_box.see(tk.END)

    type_chunk()

def add_message(sender, text):
    chat_box.config(state="normal")
    cleaned_text = clean_markdown(text)
    
    if chat_box.get("1.0", tk.END).strip():
        chat_box.insert(tk.END, "\n")
    
    if sender == "Vous":
        chat_box.insert(tk.END, f"{sender} 👤\n", "user_header")
        chat_box.insert(tk.END, f"{cleaned_text}\n", "user_text")
    else:
        chat_box.insert(tk.END, f"● {sender}\n", "bot_header")
        chat_box.insert(tk.END, f"{cleaned_text}\n", "bot_text")
    
    chat_box.config(state="disabled")
    chat_box.see(tk.END)

# Message de bienvenue
add_message("STAR AI", "Bonjour ! Je suis l'assistant virtuel de STAR Assurances. Comment puis-je vous aider aujourd'hui ?")

# ================= INPUT SECTION =================
input_frame = tk.Frame(window, bg=COLOR_BG)
input_frame.pack(fill="x", padx=20, pady=(5, 15), side="bottom")

entry_border = tk.Frame(input_frame, bg=COLOR_BORDER, bd=1)
entry_border.pack(side="left", fill="x", expand=True, ipady=2)

entry = tk.Entry(entry_border, font=("Segoe UI", 11), bg=COLOR_WHITE, fg=COLOR_TEXT_DARK, bd=0, relief="flat")
entry.pack(fill="x", padx=10, pady=8)

def detect_language(text):
    if any("\u0600" <= c <= "\u06FF" for c in text):
        return "ar"
    english_words = ["hello", "hi", "how", "what", "insurance", "price"]
    if any(w in text.lower() for w in english_words):
        return "en"
    return "fr"

def receive_response(answer):
    hide_typing()
    add_bot_stream_message(answer)

def ask_api(message, language):
    try:
        response = requests.post(
            API_URL,
            json={"message": message, "language": language},
            timeout=120
        )
        data = response.json()
        
        if response.status_code == 200:
            answer = data.get("response", "Réponse vide.")
        else:
            answer = f"Erreur [{response.status_code}]: {data.get('detail', response.text)}"

    except Exception as e:
        answer = f"Erreur de connexion : {str(e)}"

    window.after(0, receive_response, answer)

def send_message():
    message = entry.get().strip()
    if not message:
        return

    entry.delete(0, tk.END)
    add_message("Vous", message)
    show_typing()
    
    language = detect_language(message)
    threading.Thread(target=ask_api, args=(message, language), daemon=True).start()

send_button = tk.Button(
    input_frame, text="Envoyer  ➤", font=("Segoe UI", 10, "bold"),
    bg=COLOR_PRIMARY, fg=COLOR_WHITE, activebackground=COLOR_PRIMARY_HOVER,
    activeforeground=COLOR_WHITE, bd=0, padx=18, pady=8, cursor="hand2",
    command=send_message
)
send_button.pack(side="right", padx=(10, 0))

window.bind("<Return>", lambda e: send_message())
window.mainloop()