from fastapi import FastAPI
from fastapi.responses import JSONResponse

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


# 👇 THIS is the key part (no Mangum)
def handler(request):
    return JSONResponse({"message": "Vercel function is alive 🚀"})
