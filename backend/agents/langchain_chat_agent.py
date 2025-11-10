# backend/agents/langchain_chat_agent.py
from agents.base_agent import BaseAgent
from core.chat_memory import get_conversation_chain

class LangchainChatAgent(BaseAgent):
    """
    Redis 기반 LangChain 메모리를 사용하는 대화형 Agent
    """

    def __init__(self, user_id: str = "guest"):
        super().__init__(
            name="LangchainChatAgent",
            role_prompt=("Redis 기반 LangChain Memory를 사용하는 대화형 AI 비서 입니다."
                         "이전 대화를 고려하여 사용자에게 정확한 답변을 해주세요"
            ),
        )    
        self.chain = get_conversation_chain(user_id)

    def handle(self, user_input: str) -> str:
        """
        대화 입력 처리
        - Redis에 자동으로 대화 이력을 저장
        - 이전 대화 문맥을 자동으로 기억
        """
        response = self.chain.run(input=user_input)
        return response
