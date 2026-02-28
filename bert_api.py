from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()

MODEL_PATH = "navya473/emo-bert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

print("MODEL TYPE:", type(model))

# Input schema
class TextInput(BaseModel):
    text: str

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Prediction endpoint
@app.post("/predict")
def predict(data: TextInput):
    # Tokenize input text
    inputs = tokenizer(
        data.text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)
        
        # Multi-label: apply sigmoid
        probs = torch.sigmoid(outputs.logits)  # shape: [batch_size, num_labels]
        preds = (probs > 0.5).int()           # multi-hot predictions

    # Only first example in batch
    pred = preds[0]
    prob = probs[0]

    # Map indices to 5 core emotion names
    label_names_5 = ["joy", "sadness", "anger", "fear", "surprise"]
    predicted_emotions = [label_names_5[i] for i, val in enumerate(pred) if val == 1]
    predicted_confidences = [round(float(prob[i]), 2) for i, val in enumerate(pred) if val == 1]

    return {
        "prediction": predicted_emotions,
        "confidence": predicted_confidences
    }
