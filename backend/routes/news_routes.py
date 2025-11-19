from fastapi import APIRouter, Request
from backend.agents.news_agent import NewsAgent

router = APIRouter(tags=["Agent API"])
agent = NewsAgent()

@router.post("/news")
async def news(request: Request):
    data = await request.json()
    # user_input = data.get("message", "")
    # user_name = data.get("user_name", "")
    response = agent.handle(data)
    return {"agent": agent.name, "reply": response}
