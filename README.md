# 🤖 STAR AI — AI Assistant for STAR Assurances

STAR AI is an AI-powered assistant designed for **STAR Assurances**.

It allows users to ask questions about STAR Assurances products and services using the company's documentation and Google Gemini AI.

The application combines:

* 🤖 Google Gemini AI
* 📚 RAG (Retrieval-Augmented Generation)
* 📄 STAR Assurances documentation
* ⚡ FastAPI
* 💬 Tkinter desktop interface
* 🌍 French, English and Arabic support

> **Important:** The client only needs to install the application, configure their Gemini API key, and start the backend and frontend.

---

# ✨ Main Features

* 🤖 AI chatbot powered by Google Gemini
* 🏢 STAR Assurances knowledge base
* 📚 Document-based RAG system
* 🔎 Information retrieval from company documentation
* 🌍 Multilingual support:

  * 🇫🇷 French
  * 🇬🇧 English
  * 🇹🇳 Arabic
* 💬 Desktop chat interface
* ⚡ FastAPI backend
* 🔐 Secure API key configuration using `.env`
* 🧠 Conversation history
* 🏥 STARCARE information
* 🚫 Prevents the AI from inventing information outside the provided documentation

---

# 🖥️ Requirements

Before installing STAR AI, make sure the computer has:

* **Windows 10 or Windows 11**
* **Python 3.10 or newer**
* **Git**
* Internet connection
* A valid **Google Gemini API key**

---

# 🚀 Installation

## Step 1 — Download the Project

Open **PowerShell** or **Command Prompt**.

Clone the project:

```bash
git clone https://github.com/hassen23-wq/Hassen-AI.git
```

Then enter the project folder:

```bash
cd Hassen-AI
```

---

# 🐍 Step 2 — Create the Python Environment

Inside the project folder, run:

```bash
python -m venv venv
```

Then activate the environment:

### Windows PowerShell

```powershell
venv\Scripts\activate
```

If activation is successful, you should see:

```text
(venv)
```

at the beginning of the terminal line.

Example:

```text
(venv) C:\Users\User\Hassen-AI>
```

---

# 📦 Step 3 — Install the Required Packages

Run:

```bash
python -m pip install -r backend/requirements.txt
```

Wait until the installation is complete.

---

# 🔐 Step 4 — Configure the Gemini API Key

STAR AI requires a Google Gemini API key.

The API key must **never be written directly inside the Python code**.

## Create the `.env` file

Inside the `backend` folder, create a file named:

```text
.env
```

The project should look like:

```text
Hassen-AI/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── config.py
│   ├── document_loader.py
│   ├── prompt.py
│   ├── rag_engine.py
│   ├── vector_store.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── demo_interface.py
│
└── knowledge/
```

Open the `.env` file and add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace:

```text
YOUR_GEMINI_API_KEY
```

with your actual Gemini API key.

### ⚠️ Security

**Never share your API key.**

Do not send it by email, WhatsApp, GitHub, or any other public platform.

Do not upload the `.env` file to GitHub.

The project already contains `.gitignore` rules to protect the `.env` file.

---

# ▶️ Step 5 — Start STAR AI

STAR AI uses two components:

```text
Frontend
   ↓
FastAPI Backend
   ↓
Google Gemini
```

The backend must be started **before** the frontend.

---

## Step 5.1 — Start the Backend

Open a terminal inside the project folder:

```bash
cd Hassen-AI
```

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Start the FastAPI server:

```bash
python -m uvicorn backend.app:app --reload
```

If everything is working correctly, you should see:

```text
Uvicorn running on http://127.0.0.1:8000
```

### ⚠️ Important

**Do not close this terminal.**

The backend must remain running while STAR AI is being used.

---

# 🧪 Step 6 — Test the Backend

Open a web browser and go to:

```text
http://127.0.0.1:8000/docs
```

You should see the **FastAPI documentation page**.

If this page opens successfully, the backend is running correctly.

---

# 💬 Step 7 — Start the STAR AI Interface

Open a **second terminal**.

Go to the project folder:

```bash
cd Hassen-AI
```

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Then start the application:

```bash
python frontend/demo_interface.py
```

The STAR AI desktop interface should open.

---

# 🔄 How STAR AI Works

The application works as follows:

```text
                 USER
                   │
                   ▼
          ┌─────────────────┐
          │   STAR AI UI    │
          │    Tkinter      │
          └────────┬────────┘
                   │
                   │ HTTP
                   ▼
          ┌─────────────────┐
          │ FastAPI Backend │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  RAG System     │
          │ STAR Documents  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  Google Gemini  │
          └────────┬────────┘
                   │
                   ▼
               RESPONSE
                   │
                   ▼
             STAR AI UI
```

When a user asks a question:

1. STAR AI receives the question.
2. The system searches the STAR documentation.
3. Relevant information is retrieved.
4. The information is sent to Gemini.
5. Gemini generates the response.
6. The response is displayed in the STAR AI interface.

---

# 📚 Knowledge Base

STAR AI uses company documentation stored inside:

```text
knowledge/
```

For example:

```text
knowledge/
└── products/
    └── starcare.md
```

The AI is instructed to use the available documentation.

If the requested information is not available in the documentation, STAR AI should not invent an answer.

---

# 🌍 Supported Languages

STAR AI supports:

🇫🇷 **French**

🇬🇧 **English**

🇹🇳 **Arabic**

Users can communicate with the assistant in these languages.

---

# 🔌 Backend API

The main endpoint used by the application is:

```text
POST /chat
```

The frontend sends the user's message to the backend.

The backend processes the request and returns the AI response.

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🛠️ Troubleshooting

## ❌ Error: Connection refused

If you see an error similar to:

```text
HTTPConnectionPool(host='127.0.0.1', port=8000)
```

the backend is probably not running.

Open a terminal and run:

```bash
python -m uvicorn backend.app:app --reload
```

Keep this terminal open.

Then start the frontend again:

```bash
python frontend/demo_interface.py
```

---

## ❌ Error: API key not valid

If you see:

```text
API key not valid
```

check the following:

### 1. `.env` exists

The file must be located at:

```text
backend/.env
```

### 2. The variable name is correct

It must be:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 3. The API key is valid

Make sure the Gemini API key is active and available for the Google project/account being used.

---

## ❌ Error: ModuleNotFoundError

Run:

```bash
python -m pip install -r backend/requirements.txt
```

Then restart the backend:

```bash
python -m uvicorn backend.app:app --reload
```

---

## ❌ Error: Port 8000 already in use

If you see an error saying that port `8000` is already being used, you can start STAR AI on another port:

```bash
python -m uvicorn backend.app:app --reload --port 8001
```

If you do this, the frontend configuration must also use port `8001`.

---

# 🔒 Security

The following information must **never** be uploaded to GitHub:

```text
.env
API keys
Passwords
Access tokens
Private credentials
```

Always use environment variables for sensitive information.

---

# 📁 Project Structure

```text
Hassen-AI/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── config.py
│   ├── document_loader.py
│   ├── prompt.py
│   ├── rag_engine.py
│   ├── vector_store.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── demo_interface.py
│
├── knowledge/
│   └── products/
│       └── starcare.md
│
├── .gitignore
└── README.md
```

---

# 🧑‍💻 Quick Start

For users who already installed Python and Git:

### 1. Download

```bash
git clone https://github.com/hassen23-wq/Hassen-AI.git
cd Hassen-AI
```

### 2. Create environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r backend/requirements.txt
```

### 4. Configure API key

Create:

```text
backend/.env
```

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 5. Start backend

```bash
python -m uvicorn backend.app:app --reload
```

### 6. Open another terminal

```bash
cd Hassen-AI
venv\Scripts\activate
```

### 7. Start STAR AI

```bash
python frontend/demo_interface.py
```

---

# 👤 Project

**STAR AI**

AI Assistant for **STAR Assurances**

Developed by **Hassen**

GitHub repository:

https://github.com/hassen23-wq/Hassen-AI

---

# 📄 License

This project is intended for development, demonstration, and internal use.
