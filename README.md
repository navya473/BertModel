##  Emo-BERT API
This project provides a RESTful API for multi-label emotion classification using a fine-tuned BERT model. It detects five core emotions: Joy, Sadness, Anger, Fear, and Surprise.

 ##  Live Demo
Try the model instantly on Hugging Face Spaces: https://huggingface.co/spaces/navya473/emo-bert
Emo-BERT Gradio App

##  Features
FastAPI Framework: High-performance asynchronous API.
Multi-label Classification: Supports overlapping emotions (e.g., Joy + Surprise).
Dockerized: Fully containerized for easy deployment.

##  How Model Weights are Loaded
This project utilizes the Hugging Face Hub for seamless model management:
Dynamic Fetching: On startup, the AutoTokenizer and AutoModel classes use the MODEL_PATH (navya473/emo-bert) to check for weights locally.
Automatic Download: If the weights aren't found in the local cache, they are automatically pulled from the Hugging Face repository.
Consistency: This ensures the API always runs the latest version of the fine-tuned model without needing to manually manage large .bin or .safetensors files in your git repo.

##  Installation & Setup
1. Local Environment
Bash
pip install fastapi uvicorn torch transformers pydantic
python bert_api.py
2. Docker Deployment
Bash
docker build -t emo-bert-api .
docker run -p 8000:8000 emo-bert-api

##  API Endpoints
GET /health
Returns {"status": "ok"} if the model is loaded and ready.
POST /predict

Payload: {"text": "I am so surprised and happy about the news!"}

Response:
JSON
{
  "prediction": ["joy", "surprise"],
  "confidence": [0.98, 0.85]
}

## CI/CD

This project uses Azure Pipelines for automated:
- Testing
- Docker image builds
- Deployment workflows

Pipeline configuration is maintained in a private Azure DevOps repository and cannot be shared publicly.
