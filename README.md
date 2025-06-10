# Text Analyzer 

**A powerful Named Entity Recognition (NER) and AI analysis tool** that extracts entities from text and provides intelligent insights using local LLMs.

![App Screenshot](https://github.com/Dwaipayan-Mondal/NER-AI-Assistant/blob/main/NER_Image_1.jpg)
![App Screenshot](https://github.com/Dwaipayan-Mondal/NER-AI-Assistant/blob/main/NER_Image_2.jpg)

## Features

- **Named Entity Recognition** using spaCy's `en_core_web_sm` model
- **AI-powered analysis** via local LLM (Ollama)
- **Beautiful visualization** of detected entities with color coding
- **Real-time processing** with loading indicators
- **Modern UI** with responsive design
- **Console logging** for development tracking

## Tech Stack 

**Backend:**
- Python 3.11+
- FastAPI (REST API)
- spaCy (NER)
- Requests (Ollama API calls)

**Frontend:**
- HTML5
- CSS3 (with modern animations)
- JavaScript (Fetch API)

**Local AI:**
- Ollama (running LLM models locally)

## Installation 

### Prerequisites
- Python 3.11+
- Ollama installed and running (with at least one model downloaded)(tested with llama 2)

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/text-analyzer-pro.git
cd text-analyzer-pro/backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Download spaCy model
python -m spacy download en_core_web_sm

# Start FastAPI server
uvicorn main:app --reload
