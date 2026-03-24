from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "The Health Check Is Successfull..!"
