from agents.base_agent import BaseAgent
from core.naver_news_api import search_naver_news
from core.news_db_manager import embed, record_news, find_similar_news

class NewsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="NewsAgent",
            role_prompt=(
                "당신은 뉴스 큐레이션을 담당하는 AI 에이전트입니다. "
                "새로운 뉴스 중 중복되지 않은 기사만 요약해 중요도 순으로 정리하세요."
            ),
        )

    def handle(self, data) -> str:
        user_input = data.get("message", "")
        user_keywords = data.get("keywords", "")
        user_name = data.get("user_name", "")
    
        """네이버 API를 통해 검색 결과 회신"""
        fetch_news = search_naver_news(user_keywords,20) if user_keywords else "입력한 키워드가 없습니다."
        
        record_count = 0
        new_aticles = []

        for article in fetch_news:
            
            text = f"{article['title']} {article['description']}" # 기사를 벡터화
            similar = find_similar_news(user_name, text)    # DB에서 유사한 기사가 있는지 검색
            if similar is None:
                # 유사한 기사가 없을경우 DB 저장
                record_news(article,user_name,user_keywords)
                new_aticles.append(article)
                record_count+=1
                # print(f"[+] 기사 저장 [{record_count}] {user_name} , {article['title']}")
                info = (
                    f" 제목: {article['title']}\n"
                    f" 설명: {article.get('description', '설명 없음')}\n"
                    f" 날짜: {article.get('pubDate', '날짜 정보 없음')}\n"
                    f" 링크: {article.get('link', '링크 없음')}\n"
                    f"{'-'*60}\n"
                )
                print(f"기사저장 ({record_count}) Title: {article['title']}")
                print(f"-"*60)
                new_aticles.append(info)
            else:
                pass    
                
            if record_count >= 3:
                break
        
        if record_count == 0:
            return "신규 기사가 없습니다."
        
        response = (
        f"총 {record_count}개의 새 기사를 저장했습니다.\n\n"
        + "".join(str(item) for item in new_aticles)
        )
        return response 
       
        # llm_reply = self._llm_reply(prompt)