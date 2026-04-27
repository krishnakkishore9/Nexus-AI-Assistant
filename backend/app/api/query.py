from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.mcp.agent import get_wrapped_agent

router = APIRouter()

class QueryRequest(BaseModel):
    input: str

@router.post("/query")
async def handle_query(request: QueryRequest):
    import time
    start_time = time.time()
    try:
        agent = get_wrapped_agent()
        response = await agent.ainvoke({"input": request.input})
        
        exec_time = round(time.time() - start_time, 2)
        return {
            "status": "success",
            "data": response.get("output", "No output generated."),
            "metadata": {
                "cached": False,
                "execution_time": f"{exec_time}s"
            }
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
