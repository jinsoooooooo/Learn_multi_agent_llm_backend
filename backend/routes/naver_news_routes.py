from fastapi import APIRouter, Request
from agents.naver_news_agent import NaverNewsAgent

router = APIRouter(tags=["Agent API"])
agent = NaverNewsAgent()

@router.post("/naver_news")
async def never_news(request: Request):
    data = await request.json()
    # user_input = data.get("message", "")
    response = agent.handle(data)
    return {"agent": agent.name, "reply": response}
