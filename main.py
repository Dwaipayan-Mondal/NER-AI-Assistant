# backend/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import spacy
import requests
from pydantic import BaseModel

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    text: str

@app.post("/process-prompt")
async def process_prompt(request: PromptRequest):
    # Process NER with spaCy
    doc = nlp(request.text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Call local LLM (Ollama)
    llm_response = call_ollama(request.text)
    
    return JSONResponse({
        "entities": entities,
        "llm_response": llm_response
    })

def call_ollama(prompt: str):
    try:
        # Adjust model name as needed (e.g., "llama2", "mistral")
        ollama_url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(ollama_url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "No response from LLM")
    except Exception as e:
        return f"Error calling LLM: {str(e)}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)