from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text, LargeBinary, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer, util


DB_PATH = "sqlite:///./mydb.db"

engine = create_engine(DB_PATH, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# SentenceTransformer 모델
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class NewsVector(Base):
    __tablename__ = "news"

    news_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String(30))
    keyword = Column(String(100))
    title = Column(String(255))
    description = Column(Text)
    link = Column(String(255))
    pubDate = Column(DateTime, default=datetime.now)
    vector = Column(LargeBinary)  # 벡터는 binary로 저장
    similarity = Column(Float, default=0.0)

Base.metadata.create_all(bind=engine)

def record_news(article,user_name,user_keywords):
    """전송된 뉴스 DB에 기록"""
    text = f"{article['title']} {article['description']}"
    vec = model.encode(text, convert_to_numpy=True)
    session = SessionLocal()
    # print(article)
    # print(text)
    item = NewsVector(
        user_name=user_name, 
        keyword=user_keywords, 
        title=article['title'], 
        description=article['description'], 
        link=article['link'],
        vector=pickle.dumps(vec)
    )
    session.add(item)
    session.commit()
    session.close()


def find_similar_news(user_name, text, threshold=0.82):
    """입력 문장과 가장 유사한 기존 뉴스 반환"""
    session = SessionLocal()
    existing = session.query(NewsVector).filter(NewsVector.user_name == user_name).all()
    query_vec = model.encode(text, convert_to_numpy=True)
    best_score = 0
    best_news = None
    for item in existing:
        vec = pickle.loads(item.vector)
        score = util.cos_sim(query_vec, vec).item()
        if score > best_score:
            best_score = score
            best_news = item
    session.close()

    if best_news and best_score >= threshold:
        return {"id": best_news.news_id, "title": best_news.title, "score": best_score}
    return None

def get_user_news_ids(user_name: str):
    """사용자가 이미 받은 뉴스 ID 목록"""
    session = SessionLocal()
    rows = session.query(NewsVector.news_id).filter(NewsVector.user_name == user_name).all()
    session.close()
    return [r[0] for r in rows]


def embed(text):
    # 벡터화 예시 (실제로는 sentence_transformers 사용)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode(text, convert_to_numpy=True)