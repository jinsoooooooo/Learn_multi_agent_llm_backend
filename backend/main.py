from fastapi import FastAPI
from routes.health_check import router as health_router
from routes.chat_routes import router as chat_router
from routes.meeting_routes import router as meeting_router
from routes.naver_news_routes import router as naver_news_router
from routes.news_routes import router as news_router
from routes.langchain_chat_routes import router as langchain_router


app = FastAPI(title="RAG Multi-Agent Backend")
app.include_router(health_router, prefix="/api")
app.include_router(chat_router, prefix="/api")
app.include_router(meeting_router, prefix="/api")
app.include_router(naver_news_router, prefix="/api")
app.include_router(news_router, prefix="/api")
app.include_router(langchain_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to RAG Multi-Agent Backend"}


@app.on_event("startup")
def on_startup():
    # 서버 시작 시 등록된 모든 라우트를 콘솔에 출력하는 디버그용 코드
    print("\n Registered Routes:")
    for route in app.routes:
        methods = ', '.join(route.methods or [])
        print(f"  {route.path:30s} → [{methods}]")



# # NAVER 뉴스 API --> main.py test
# import requests
# import urllib.parse

# # ✅ 네이버 API 인증 정보
# CLIENT_ID = "jFgOLYH8gUFQ2_0DhekQ"
# CLIENT_SECRET = "Y1xqeZZfF4"

# def search_naver_news(keyword, display=5, sort="sim"):
#     base_url = "https://openapi.naver.com/v1/search/news.json"
#     query = urllib.parse.quote(keyword)
#     url = f"{base_url}?query={query}&display={display}&start=1&sort={sort}"

#     headers = {
#         "X-Naver-Client-Id": CLIENT_ID,
#         "X-Naver-Client-Secret": CLIENT_SECRET,
#         "Accept": "*/*",
#         "Host": "openapi.naver.com",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }

#     response = requests.get(url, headers=headers, verify=False)
    
#     if response.status_code == 200:
#         result = response.json()
#         articles = []
#         for item in result['items']:
#             articles.append({
#                 "title": item['title'].replace("<b>", "").replace("</b>", ""),
#                 "link": item['link'],
#                 "description": item['description'].replace("<b>", "").replace("</b>", ""),
#                 "pubDate": item['pubDate']
#             })
#         return articles
#     else:
#         print("Error Code:", response.status_code)
#         return []

# # ✅ 테스트 실행
# if __name__ == "__main__":
#     keyword = "인공지능"
#     news_list = search_naver_news(keyword)
#     for news in news_list:
#         print(f"[{news['title']}]({news['link']})")
#         print(f"→ {news['description']}\n")
