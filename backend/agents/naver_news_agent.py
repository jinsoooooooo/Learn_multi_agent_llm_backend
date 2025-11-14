from agents.base_agent import BaseAgent
from core.naver_news_api import search_naver_news

class NaverNewsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="NaverNewsAgent",
            role_prompt=(
                "당신은 사용자의 요청 Keywrod로 네이버 뉴스를 검색 해주는 AI 비서 입니다."
            ),
        )

    def handle(self, data) -> str:
        """네이버 API를 통해 검색 결과 회신"""
        user_input = data.message
        keyword_list = data.keywords
        user_keywords = ",".join(keyword_list)
        user_id = data.user_id
    
        """네이버 API를 통해 검색 결과 회신"""
        fetch_news = search_naver_news(user_keywords,3) if user_keywords else "입력한 키워드가 없습니다."
        
        # naver news api는 llm을 호출 하지 않는다.
        # prompt = f"""
        # 사용자 요청: "{user_input}"
        # """
        # llm_reply = self._llm_reply(prompt)
        
        return fetch_news
