# backend/routes/langchain_chat_routes.py
from fastapi import APIRouter, Request
from agents.langchain_chat_agent import LangchainChatAgent

router = APIRouter(tags=["LangChain Chat"])

@router.post("/langchain/chat")
async def chat_with_memory(request: Request):
    """
    LangChain 기반 대화 API
    - user_id 별로 Redis에 대화 이력 저장
    - 이전 대화를 자동으로 참고
    """
    data = await request.json()
    user_id = data.get("user_id", "guest")
    message = data.get("message", "")

    agent = LangchainChatAgent(user_id=user_id)
    response = agent.handle(message)

    return {"user_id": user_id, "reply": response}
