from fastapi import APIRouter, Request
from agents.chat_agent import ChatAgent

router = APIRouter(tags=["Agent API"])
agent = ChatAgent()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    response = agent.handle(user_input)
    return {"agent": agent.name, "reply": response}
