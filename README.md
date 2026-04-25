# 🧠 DocMind – RAG Chatbot

> A Retrieval-Augmented Generation (RAG) chatbot built as a B.Tech CSE Minor Project.  
> Upload documents and ask questions — the AI answers using **only** your document as context.

![DocMind Screenshot](screenshots/demo.png)

---

## 🚀 Live Demo

Open `index.html` in any browser. No server needed — it runs entirely in the browser!

---

## 📌 What is RAG?

**Retrieval-Augmented Generation (RAG)** is an AI architecture where:

1. **Documents** are uploaded as the knowledge base
2. **User query** triggers retrieval of relevant context from those documents
3. **LLM** generates an answer grounded strictly in the retrieved context

This prevents hallucination and ensures answers are sourced from your data.

```
User Query
    │
    ▼
┌─────────────────┐
│  Document Store │  ← Your uploaded .txt / .md files
└────────┬────────┘
         │ Context Injection
         ▼
┌─────────────────┐
│  Claude LLM     │  ← Generates answer using ONLY your docs
└────────┬────────┘
         │
         ▼
    Cited Answer
```

---

## ✨ Features

- 📄 Upload `.txt` and `.md` documents
- 💬 Chat interface with conversation history
- 📍 Source citations in every response
- 🔑 API key entry (stored in localStorage)
- 🚫 Hallucination prevention — AI answers only from your docs
- ⚡ Fully client-side — no backend needed

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| AI Model | Claude claude-sonnet-4-20250514 (Anthropic) |
| API | Anthropic Messages API |
| Fonts | Sora, JetBrains Mono (Google Fonts) |
| Hosting | GitHub Pages (static) |

---

## ⚙️ Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/docmind-rag.git
cd docmind-rag
```

### 2. Get an Anthropic API Key
- Sign up at [console.anthropic.com](https://console.anthropic.com)
- Create an API key under **API Keys**

### 3. Run the app
Simply open `index.html` in your browser — no installation needed!

```bash
# Optional: serve locally
npx serve .
# or
python -m http.server 8080
```

### 4. Use the chatbot
1. Enter your API key in the banner at the top
2. Upload a `.txt` or `.md` file
3. Ask questions about your document!

---

## 📁 Project Structure

```
docmind-rag/
├── index.html          # Main app (single-file, no dependencies)
├── README.md           # Project documentation
├── docs/
│   └── sample.txt      # Sample document for testing
└── screenshots/
    └── demo.png        # Demo screenshot
```

---

## 🔮 Future Improvements

- [ ] PDF support (via PDF.js)
- [ ] Semantic chunking with embeddings (OpenAI / sentence-transformers)
- [ ] FAISS / ChromaDB vector store integration
- [ ] Python FastAPI backend
- [ ] Multi-document cross-referencing
- [ ] Chat history export

---

## 📚 Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Prompt Engineering with context injection
- LLM API integration
- Client-side document parsing
- Conversational AI with memory

---

## 👨‍💻 Author

**[Your Name]**  
B.Tech Computer Science & Engineering  
[Your College Name]  
[Your GitHub Profile](https://github.com/YOUR_USERNAME)

---

## 📄 License

MIT License — free to use, modify, and distribute.
