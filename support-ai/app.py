from fastapi import FastAPI
from sentence_transformers import SentenceTransformer, util

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')

data = [
    "Payment failed but money deducted",
    "Order not delivered",
    "App is crashing",
    "Refund not received"
]

responses = [
    "Refund will be processed in 2 days",
    "Your order will arrive soon",
    "Please update the app",
    "Refund is under process"
]

embeddings = model.encode(data, convert_to_tensor=True)

@app.get("/")
def home():
    return {"message": "Customer Support AI Running"}

@app.get("/ask")
def ask(query: str):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, embeddings)
    best_match = scores.argmax().item()
    
    return {
        "query": query,
        "response": responses[best_match]
    }