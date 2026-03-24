from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Working 🚀"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/predict")
async def predict(x: int = 1):
    return {"input": x, "output": x * 2}

# IMPORTANT: explicit handler name
handler = Mangum(app)
