from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Prompt Alchemist is alive 🚀"}

@app.get("/predict")
def predict(x: int):
    return {"input": x, "output": x * 2}

# IMPORTANT: expose handler correctly
handler = Mangum(app)
