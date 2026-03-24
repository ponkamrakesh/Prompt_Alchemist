from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Clean deploy working 🚀"}

handler = Mangum(app)
