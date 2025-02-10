from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .openai_service import analyze_code

app = FastAPI()

@app.post("/analyze-code/")
async def analyze_code_endpoint(code_snippet: str, db: AsyncSession = Depends(get_db)):
    
    analysis_result = analyze_code(code_snippet)
    if analysis_result:
        return {"result": analysis_result}
    else:
        raise HTTPException(status_code=500, detail="Error processing your request")
