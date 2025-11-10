# backend/core/llm_core
import os
from openai import OpenAI
from core.env_loader import load_dotenv

# .env 파일 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
default_model = os.getenv("DEFAULT_LLM_MODEL", "gpt-4o-mini")

client = OpenAI(api_key=api_key)

def call_llm(prompt: str, model: str = None, temperature: float = 0.3):
    """공통 LLM 호출 함수"""
    model = model or default_model
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "당신은 유능한 비서형 AI입니다."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()