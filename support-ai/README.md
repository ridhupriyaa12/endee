📌 Project Title

    AI Customer Support Intelligence using Endee

🚀 Overview

    This project builds an AI system that understands customer queries and provides relevant responses using semantic search.

⚙️ System Design
    Embedding Model: Sentence Transformers
    Backend: FastAPI
    Vector Search: Endee

✨ Features

    - 🔍 Semantic search for customer queries
    - 🤖 AI-based response generation
    - ⚡ FastAPI backend for quick responses
    - 🧠 Uses embeddings for similarity matching
    - 📦 Easy setup with requirements.txt

📁 Project Structure

    support-ai/
    │── app.py              # Main FastAPI application
    │── requirements.txt    # Dependencies
    │── README.md           # Project documentation



🧠 Use of Endee
    Endee is used as a vector database to store and retrieve embeddings for similarity search.

▶️ Setup
    git clone <repo>
    pip install fastapi uvicorn sentence-transformers
    uvicorn app:app --reload

🧪 Sample Output

### Input:

    http://127.0.0.1:8000/ask?query=payment
    
### Output:
{
  "query": "payment issue",
  "response": "Refund will be processed in 2 days"
}