# backend/routes/langchain_chat_routes.py
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from agents.langchain_chat_agent import LangchainChatAgent
import asyncio

router = APIRouter(prefix="/chat/langchain", tags=["Agent API"])
agent = LangchainChatAgent()

@router.post("/")
async def chat_stream(request: Request):
    body = await request.json()
    user_input = body.get("message", "")

    async def event_generator():
        answer = agent.chat(user_input)
        for ch in answer:
            yield f"data: {ch}\n\n"
            await asyncio.sleep(0.02)
        yield "data: [END]\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
