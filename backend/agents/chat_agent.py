# backend/agnet/chat_agent.py
from agents.base_agent import BaseAgent

class ChatAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ChatAgent",
            role_prompt=(
                "당신은 사용자의 일상 업무를 도와주는 AI 어시스턴트입니다. "
                "짧고 명확하게 대답하세요."
            ),
        )

    def handle(self, user_input: str) -> str:
        """일반 대화 처리"""
        return self._llm_reply(user_input)
