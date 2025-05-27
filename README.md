# 🧠 News-bot Backend - RAG Chatbot API

This is the backend for the Verifast RAG-powered chatbot, built using Flask. It integrates:
- Jina Embeddings API (text embeddings)
- Qdrant Cloud (vector DB)
- Gemini API (LLM response generation)
- Redis Cloud (caching + session memory)

---

## 🚀 Features

- Embedding generation and indexing of news articles
- Contextual Q&A over indexed news using RAG
- Session-based history with Redis
- Modular Flask codebase for scalability
---

## ⚙️ Setup Instructions

```bash
# Clone the backend repo
git clone https://github.com/yourname/verifast_backend.git
cd verifast_backend

# Create a virtual environment (recommended)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Add environment variables
```
REDIS_URL=your_redis_url
QDRANT_API_KEY=your_qdrant_key
QDRANT_URL=https://your-qdrant-url
GEMINI_API_KEY=your_gemini_key
PORT=8000
```
### Run the app
```bash
python -m main
```

## 🧪 API Endpoints
```
POST /api/chat/message
```
- Accepts a user message
- Returns a response from the LLM based on vector-retrieved context

```
GET /api/history/<sessionId>
```
- Gets the chat history of previous conversations.

```
DELETE /api/clear/<sessionId>
```
- Deletes a conversation from the redis database
## 📌 Notes
- All context is fetched from Qdrant before querying the Gemini model.
- Redis is used to store session context for smoother user interaction.

---

# News-bot Frontend

This is the frontend interface for the **Verifast** project — a RAG-powered news chatbot. It is built with **React** and styled using **Tailwind CSS**, providing users with a seamless chat experience.

## ✨ Features

- Modern chat UI with Tailwind styling
- Sends user queries to backend API
- Displays streaming chat responses
- Maintains chat history
- Responsive design

## 🧰 Tech Stack

- **React** (with Create React App)
- **Tailwind CSS** for styling
- **Fetch** for API calls
- **GCP VM** for deployment

## 🚀 Getting Started
### 1. Clone the repo
```
git clone https://github.com/yourname/verifast_frontend.git
cd verifast_frontend
```

### 2. Install dependencies
```
npm install
```

### 3. Set up environment variables
Create a .env file in the root and define:
```
REACT_APP_BACKEND_URL=http://<your-backend-ip>:8000
```
### 4. Run the development server
```
npm start
```
