from fastapi import Depends, FastAPI
from .database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

@app.get("/items/")
async def read_items(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute("SELECT * FROM items")
        items = result.fetchall()
        return items
