import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    print(GROQ_API_KEY)
    # LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    print(ASTRA_DB_API_ENDPOINT)
    print(ASTRA_DB_APPLICATION_TOKEN)
    print(ASTRA_DB_KEYSPACE)
    EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
    RAG_MODEL = "llama-3.1-8b-instant"