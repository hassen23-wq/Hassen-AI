# STAR AI 🤖

An AI-powered assistant for **STAR Assurances**, built with Python, FastAPI, Tkinter, Google Gemini, and a document-based knowledge system (RAG).

The assistant is designed to answer questions about STAR Assurances products and services using the company's documentation.

---

## ✨ Features

* 🤖 AI chatbot powered by Google Gemini
* 🏢 STAR Assurances-specific knowledge base
* 📚 RAG (Retrieval-Augmented Generation)
* 🔎 Document-based information retrieval
* 🌍 Multilingual support: French, English, and Arabic
* 💬 Chat interface built with Tkinter
* ⚡ FastAPI backend
* 🔐 API key stored securely using environment variables
* 🧠 Conversation history
* 🏥 STARCARE insurance information
* 🚫 Prevents the AI from inventing information outside the provided documentation

---

## 🛠️ Technologies

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

## 📁 Project Structure

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
│   └── .env                 # Not included in GitHub
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

# 🚀 Installation

## 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/hassen23-wq/Hassen-AI.git
```

Then enter the project directory:

```bash
cd Hassen-AI
```

The project is currently available on the `master` branch:

```bash
git checkout master
```

---

## 2. Create a virtual environment

It is recommended to use a virtual environment.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

You should see something similar to:

```text
(venv) C:\...\Hassen-AI>
```

---

## 3. Install dependencies

Install the backend dependencies:

```bash
pip install -r backend/requirements.txt
```

If `pip` is not recognized, use:

```bash
python -m pip install -r backend/requirements.txt
```

---

# 🔐 Configuration

The project requires a **Google Gemini API key**.

The API key must NOT be placed directly inside the Python source code or uploaded to GitHub.

## 1. Create the `.env` file

Inside the `backend` folder, create a file named:

```text
.env
```

The structure should be:

```text
Hassen-AI/
└── backend/
    └── .env
```

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own Gemini API key.

### ⚠️ Important

Never commit or upload the `.env` file.

The repository already uses `.gitignore` to prevent the `.env` file from being uploaded.

---

# ▶️ Running the Backend

Open a terminal in the project directory:

```bash
cd Hassen-AI
```

Activate the virtual environment if it is not already active:

```bash
venv\Scripts\activate
```

Then start the FastAPI server:

```bash
python -m uvicorn backend.app:app --reload
```

The backend should start on:

```text
http://127.0.0.1:8000
```

You can also open the FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

Keep this terminal running.

---

# 🖥️ Running the Frontend

Open a **second terminal**.

Go to the project directory:

```bash
cd Hassen-AI
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Then run the Tkinter interface:

```bash
python frontend/demo_interface.py
```

The STAR AI desktop interface should open.

---

# 🔄 How the Application Works

The application follows this architecture:

```text
User
  │
  ▼
Tkinter Frontend
  │
  │ HTTP Request
  ▼
FastAPI Backend
  │
  ▼
Chatbot
  │
  ├── Retrieve STAR documentation
  │
  ├── RAG / Knowledge Retrieval
  │
  └── Google Gemini
  │
  ▼
AI Response
  │
  ▼
Tkinter Frontend
```

The frontend communicates with the backend through the `/chat` API endpoint.

---

# 📚 Knowledge Base

The assistant uses STAR Assurances documentation stored in:

```text
knowledge/products/
```

For example:

```text
knowledge/products/starcare.md
```

The knowledge base contains information about STAR insurance products and services.

The assistant is instructed to use the available STAR documentation and avoid inventing information that is not present in the knowledge base.

---

# 🔌 API

## POST `/chat`

The frontend sends user messages to the FastAPI backend through:

```text
POST /chat
```

The API processes the request and returns the AI-generated response.

FastAPI interactive documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Troubleshooting

## Backend connection error

If the frontend displays:

```text
HTTPConnectionPool(host='127.0.0.1', port=8000)
```

make sure the FastAPI backend is running:

```bash
python -m uvicorn backend.app:app --reload
```

Keep the backend terminal open while using the frontend.

---

## Gemini API key error

If you see:

```text
API key not valid
```

check that:

1. `backend/.env` exists.
2. The variable is named exactly:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

3. The API key is valid.
4. The Google Gemini API is available for the account/project being used.

---

## Module not found

If you get:

```text
ModuleNotFoundError
```

make sure the virtual environment is activated and install the dependencies again:

```bash
python -m pip install -r backend/requirements.txt
```

---

## Port 8000 already in use

If port `8000` is already being used, stop the existing FastAPI/Uvicorn process or run the server on another port:

```bash
python -m uvicorn backend.app:app --reload --port 8001
```

If you change the port, make sure the frontend API URL is updated accordingly.

---

# 🔒 Security

Sensitive information must never be committed to the repository.

Do not upload:

```text
.env
API keys
Passwords
Private credentials
Access tokens
```

Use environment variables instead.

---

# 👨‍💻 Development

To get the latest version of the project:

```bash
git pull origin master
```

After making changes:

```bash
git add .
git commit -m "Describe your changes"
git push origin master
```

---

# 📌 Requirements

Before running the project, make sure you have:

* Python 3.10 or newer
* Git
* Internet connection
* A valid Google Gemini API key

---

# 👤 Author

**Hassen**

STAR AI — AI Assistant for STAR Assurances

GitHub:

https://github.com/hassen23-wq/Hassen-AI

---

## 📄 License

This project is intended for development and demonstration purposes.
