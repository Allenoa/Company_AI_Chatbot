import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env 파일 로드
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API 키가 없습니다. .env 파일을 확인해주세요.")
else:
    print(f"🔑 API Key: {api_key[:5]}*****")
    print("📡 구글 서버에 사용 가능한 모델 목록을 조회 중입니다...\n")
    
    try:
        genai.configure(api_key=api_key)
        
        found_embedding_model = False
        print("--- [사용 가능한 임베딩 모델 목록] ---")
        for m in genai.list_models():
            # 임베딩 기능(embedContent)이 있는 모델만 출력
            if 'embedContent' in m.supported_generation_methods:
                print(f"✅ 발견됨: {m.name}")
                found_embedding_model = True
        
        if not found_embedding_model:
            print("\n❌ 사용 가능한 임베딩 모델이 하나도 없습니다.")
            print("👉 구글 AI Studio에서 'Payment'(결제) 설정을 확인하거나, API 키를 새로 발급받아 보세요.")
            
    except Exception as e:
        print(f"❌ 오류 발생: {e}")