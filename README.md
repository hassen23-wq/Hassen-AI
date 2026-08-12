# STAR AI 🤖

**STAR AI** is an AI-powered assistant developed for **STAR Assurances**.

It uses **Python, FastAPI, Tkinter, Google Gemini, RAG, FAISS, and a document-based knowledge base** to provide accurate answers about STAR Assurances products and services.

The assistant is designed to use the available STAR documentation and avoid generating information that is not contained in the knowledge base.

---

# ✨ Features

* 🤖 AI chatbot powered by Google Gemini
* 🏢 STAR Assurances-specific knowledge base
* 📚 Retrieval-Augmented Generation (RAG)
* 🔎 Document-based information retrieval
* 🌍 Multilingual support:

  * 🇫🇷 French
  * 🇬🇧 English
  * 🇹🇳 Arabic
* 💬 Desktop chat interface with Tkinter
* ⚡ FastAPI backend
* 🔐 Secure API key management with environment variables
* 🧠 Conversation history
* 🏥 STARCARE insurance information
* 🚫 Prevents the AI from inventing information outside the documentation
* 📄 Support for document-based knowledge

---

# 🛠️ Technologies

The project is built with:

* **Python 3.10+**
* **FastAPI**
* **Uvicorn**
* **Tkinter**
* **Google Gemini API**
* **Google GenAI SDK**
* **Sentence Transformers**
* **FAISS**
* **NumPy**
* **python-dotenv**
* **PyPDF**

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
│   └── .env                 # Created locally, NOT included in GitHub
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

# 📋 Requirements

Before installing the project, make sure you have:

* Python **3.10 or newer**
* Git
* Internet connection
* A valid Google Gemini API key
* Windows recommended for the current Tkinter interface

You can verify Python with:

```bash
python --version
```

If `python` does not work, try:

```bash
py --version
```

---

# 🚀 Installation

## 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/hassen23-wq/Hassen-AI.git
```

Enter the project directory:

```bash
cd Hassen-AI
```

The project currently uses the `master` branch:

```bash
git checkout master
```

---

# 2. Create a Virtual Environment

It is strongly recommended to use a virtual environment.

From the project root:

```bash
python -m venv venv
```

If `python` does not work:

```bash
py -m venv venv
```

---

# 3. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

After activation, the terminal should look similar to:

```text
(venv) C:\...\Hassen-AI>
```

Make sure `(venv)` appears before the terminal path.

---

# 4. Install Dependencies

Install all required Python packages:

```bash
python -m pip install -r backend\requirements.txt
```

This installs the dependencies required by the backend and RAG system.

If you have problems with `pip`, use:

```bash
python -m pip install --upgrade pip
```

Then run again:

```bash
python -m pip install -r backend\requirements.txt
```

---

# 🔐 Configuration

STAR AI requires a **Google Gemini API key**.

For security reasons, the API key is **not included in the GitHub repository**.

Each developer must create their own `.env` file.

---

# 5. Create the `.env` File

Inside the `backend` folder, create a file named:

```text
.env
```

The final structure should be:

```text
Hassen-AI/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── config.py
│   ├── ...
│   └── .env
│
├── frontend/
├── knowledge/
└── README.md
```

Open:

```text
backend/.env
```

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace:

```text
YOUR_GEMINI_API_KEY
```

with your own Gemini API key.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# ⚠️ Security

**Never upload your API key to GitHub.**

Do NOT put your API key directly inside Python files.

❌ Do not do this:

```python
GEMINI_API_KEY = "your-secret-api-key"
```

✅ Use the `.env` file instead:

```env
GEMINI_API_KEY=your-secret-api-key
```

The `.env` file should remain local.

The `.gitignore` file should contain:

```gitignore
backend/.env
venv/
__pycache__/
*.pyc
```

---

# ▶️ Running STAR AI

The application requires **two terminals**:

* Terminal 1 → FastAPI backend
* Terminal 2 → Tkinter frontend

---

# 🟢 Terminal 1 — Start the Backend

Open a terminal in the project directory:

```bash
cd Hassen-AI
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Start FastAPI:

```bash
python -m uvicorn backend.app:app --reload
```

If everything is working correctly, you should see something similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

Keep this terminal open.

**Do not close the backend terminal while using STAR AI.**

---

# 🧪 Test the Backend

Before starting the frontend, verify that the backend is working.

Open your browser and go to:

```text
http://127.0.0.1:8000/docs
```

You should see the FastAPI interactive documentation.

If the `/docs` page opens correctly, the backend is running.

---

# 🖥️ Terminal 2 — Start the Frontend

Open a **second terminal**.

Go to the project directory:

```bash
cd Hassen-AI
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Start the Tkinter interface:

```bash
python frontend\demo_interface.py
```

The STAR AI desktop interface should open.

---

# 🚀 Quick Start

For experienced users, the complete process is:

```bash
git clone https://github.com/hassen23-wq/Hassen-AI.git
cd Hassen-AI
git checkout master

python -m venv venv
venv\Scripts\activate

python -m pip install -r backend\requirements.txt
```

Then create:

```text
backend/.env
```

with:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Start the backend:

```bash
python -m uvicorn backend.app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Then open another terminal:

```bash
cd Hassen-AI
venv\Scripts\activate
python frontend\demo_interface.py
```

---

# 🔄 How STAR AI Works

The application follows this architecture:

```text
                    USER
                      │
                      ▼
            ┌──────────────────┐
            │ Tkinter Frontend │
            └────────┬─────────┘
                     │
                     │ HTTP POST /chat
                     ▼
            ┌──────────────────┐
            │ FastAPI Backend  │
            └────────┬─────────┘
                     │
                     ▼
              ┌─────────────┐
              │   Chatbot   │
              └──────┬──────┘
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   ┌──────────────┐      ┌─────────────┐
   │ RAG / Search │      │   Gemini    │
   └──────┬───────┘      └──────┬──────┘
          │                      │
          ▼                      │
   STAR Documentation            │
          │                      │
          └──────────┬───────────┘
                     ▼
                AI Response
                     │
                     ▼
            Tkinter Frontend
```

---

# 📚 Knowledge Base

STAR AI uses documentation stored inside:

```text
knowledge/
```

For example:

```text
knowledge/products/starcare.md
```

The knowledge base contains information about STAR Assurances products and services.

The RAG system retrieves relevant information from the documentation before generating a response.

---

# 🧠 RAG System

RAG stands for:

**Retrieval-Augmented Generation**

Instead of allowing the AI to answer freely, STAR AI first searches the available STAR documentation.

The process is:

```text
User Question
      │
      ▼
Search Knowledge Base
      │
      ▼
Retrieve Relevant Information
      │
      ▼
Send Context to Gemini
      │
      ▼
Generate Answer
```

This helps the assistant provide answers based on the available STAR documentation.

---

# 🚫 Preventing Information Invented by AI

STAR AI is configured to avoid inventing information that is not available in the documentation.

If the requested information is not found in the knowledge base, the assistant should use the configured fallback response instead of creating unsupported information.

This is particularly important for insurance-related information.

---

# 🌍 Supported Languages

STAR AI supports:

### 🇫🇷 French

Example:

```text
Quelles sont les garanties de STARCARE ?
```

### 🇬🇧 English

Example:

```text
What does STARCARE cover?
```

### 🇹🇳 Arabic

Example:

```text
شنوة تغطي STARCARE؟
```

---

# 🔌 API

The backend provides a `/chat` endpoint.

## POST `/chat`

The frontend sends the user's message to:

```text
POST /chat
```

The FastAPI backend processes the request and returns the AI response.

The API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Troubleshooting

## ❌ Backend Connection Error

If the frontend displays an error similar to:

```text
HTTPConnectionPool(host='127.0.0.1', port=8000)
```

This usually means that the FastAPI backend is not running.

Start it with:

```bash
python -m uvicorn backend.app:app --reload
```

Make sure you see:

```text
Uvicorn running on http://127.0.0.1:8000
```

Then start the frontend again.

---

# ❌ API Key Not Valid

If you receive:

```text
API key not valid
```

check the following:

### 1. Make sure `.env` exists

```text
backend/.env
```

### 2. Make sure the variable name is correct

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 3. Make sure the API key is valid

### 4. Make sure there are no unnecessary quotes or spaces

Use:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

instead of:

```env
GEMINI_API_KEY="YOUR_API_KEY"
```

if your configuration expects the plain value.

---

# ❌ ModuleNotFoundError

If you see:

```text
ModuleNotFoundError
```

first activate the virtual environment:

```bash
venv\Scripts\activate
```

Then reinstall dependencies:

```bash
python -m pip install -r backend\requirements.txt
```

---

# ❌ Uvicorn Not Recognized

If you get:

```text
'uvicorn' is not recognized
```

use:

```bash
python -m uvicorn backend.app:app --reload
```

instead of:

```bash
uvicorn backend.app:app --reload
```

---

# ❌ Port 8000 Already in Use

If you receive:

```text
Address already in use
```

another process is already using port `8000`.

You can use another port:

```bash
python -m uvicorn backend.app:app --reload --port 8001
```

Then the backend will be available at:

```text
http://127.0.0.1:8001
```

If you change the port, make sure the frontend API URL is changed from:

```text
8000
```

to:

```text
8001
```

---

# ❌ Python Is Not Recognized

If Windows displays:

```text
Python was not found
```

try:

```bash
py --version
```

If Python is installed, you can create the environment using:

```bash
py -m venv venv
```

Then:

```bash
venv\Scripts\activate
```

---

# ❌ Frontend Does Not Open

Make sure:

1. The virtual environment is activated.
2. The backend is running.
3. The project directory is correct.
4. The required dependencies are installed.

Run:

```bash
python frontend\demo_interface.py
```

---

# 🔒 Security Rules

Never commit or upload:

```text
.env
API keys
Passwords
Access tokens
Private credentials
Secret keys
```

The API key must remain inside:

```text
backend/.env
```

and must never be placed directly in the source code.

---

# 🔄 Updating the Project

To get the latest version:

```bash
git pull origin master
```

After updating dependencies:

```bash
python -m pip install -r backend\requirements.txt
```

---

# 💻 Development Workflow

After making changes:

```bash
git status
```

Add the changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Describe your changes"
```

Push to GitHub:

```bash
git push origin master
```

---

# 📌 Important Notes

### `.env` is local

The `.env` file is intentionally excluded from GitHub.

Anyone cloning this project must create their own:

```text
backend/.env
```

and provide their own Gemini API key.

### Two terminals are required

**Terminal 1:**

```bash
python -m uvicorn backend.app:app --reload
```

**Terminal 2:**

```bash
python frontend\demo_interface.py
```

### Always start the backend first

The frontend communicates with:

```text
http://127.0.0.1:8000
```

Therefore, the backend must be running before using the frontend.

---

# 👨‍💻 Author

**Hassen**

STAR AI — AI Assistant for STAR Assurances

GitHub Repository:

https://github.com/hassen23-wq/Hassen-AI

---

# 📄 License

This project is intended for development, educational, and demonstration purposes.

---

# ⭐ STAR AI

**AI-powered assistance for STAR Assurances.**

```text
Clone → Install → Configure API → Start Backend → Start Frontend → 🚀
```

