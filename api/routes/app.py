# api/routes/app.py

from fastapi import APIRouter, HTTPException
from typing import Dict
from .books import books  # Import books dictionary

router = APIRouter()

@router.get("/api/v1/{book_id}")
async def get_book(book_id: int) -> Dict:
    """Retrieve a book by its ID."""
    book = books.get(book_id)  # Get book from dictionary
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"book_id": book_id, "book": book}
