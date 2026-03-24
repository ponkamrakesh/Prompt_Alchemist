try:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse

    app = FastAPI()

    @app.get("/")
    async def home():
        return {"message": "FastAPI working 🚀"}

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    @app.get("/predict")
    async def predict(x: int = 1):
        return {"input": x, "output": x * 2}

except Exception as e:
    # If FastAPI fails to import or crashes
    def handler(request):
        return {
            "statusCode": 500,
            "body": f"Startup Error: {str(e)}"
        }
