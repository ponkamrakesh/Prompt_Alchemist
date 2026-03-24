from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Vercel 🚀"}

@app.get("/predict")
def predict(x: int):
    return {"result": x * 2}