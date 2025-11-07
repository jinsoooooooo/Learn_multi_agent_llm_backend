# backend/agents/langchain_chat_agent.py
from core.redis_cache import RedisChatMemory
from agents.base_agent import BaseAgent

class LangchainChatAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="langchainChat",
            role_prompt=[
                ("system", "당신은 친절한 대화형 AI 비서입니다. 이전 대화를 고려하여 답변하세요."),
                ("chat_history","get chat history from redis"),
                ("human", "{question}")
            ]
        )          
      

    def handle(self, user_input: str) -> str:
        """ 대화 처리"""
        return self._llm_reply(user_input)



