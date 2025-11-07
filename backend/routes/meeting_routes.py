# backend/routes/meeting_routes.py
from fastapi import APIRouter, Request
from agents.meeting_agent import MeetingAgent

router = APIRouter(tags=["Agent API"])
agent = MeetingAgent()

@router.post("/meeting")
async def meeting(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    response = agent.handle(user_input)
    return {"agent": agent.name, "reply": response}
