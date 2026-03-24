from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Prompt Alchemist"}

handler = Mangum(app)        return {"message": "Hello from Prompt Alchemist!"}
    except Exception as e:
        logger.error(f"Root endpoint error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

# ---------- Path parameter with validation ----------
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    try:
        # Simulate retrieving an item
        if item_id <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Item ID must be positive"
            )
        # Pretend we have items only for ids 1-10
        if item_id > 10:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )
        return {"item_id": item_id, "query": q}
    except HTTPException:
        # Re-raise HTTP exceptions as is
        raise
    except Exception as e:
        logger.error(f"Error reading item {item_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

# ---------- POST endpoint with request body ----------
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    try:
        # Simulate validation
        if item.price <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price must be positive"
            )
        # Simulate saving to database
        # For demo, just return the created item
        return {
            "id": 123,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "message": "Item created successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating item: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create item"
        )

# ---------- Example of catching a specific error ----------
@app.get("/error-test")
async def error_test():
    try:
        # Simulate an unexpected error
        raise ValueError("Something went wrong")
    except ValueError as ve:
        logger.warning(f"Caught ValueError: {ve}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request due to invalid operation"
        )
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

# ---------- Vercel handler ----------
handler = Mangum(app)
