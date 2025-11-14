# backend\routes\langchain_chatstream_routes.py
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from agents.langchain_chatstream_agent import LangchainChatStreamAgent
from pydantic import BaseModel

router = APIRouter(tags=["LangChain Chat"])

class LangchaStreamRequest(BaseModel):
    user_id: str = 'guest'
    message: str

@router.post("/langchain/chatstream")
async def chat_with_stream(data: LangchaStreamRequest):
    """
    LangChain 기반 Streaming Chat API:
    - user_id 별로 Redis에 대화 이력 저장
    - 이전 대화를 자동으로 참고
    - 응답을 StreamingRespnse르 리턴함 -> SSE 
    """
    # data = await request.json()
    user_id = data.user_id
    message = data.message

    agent = LangchainChatStreamAgent(user_id=user_id)
    stream = agent.handle_stream(message)

    return StreamingResponse(stream, media_type="text/event-stream")
