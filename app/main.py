from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Prompt Alchemist is alive 🔥"}