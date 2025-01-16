from dotenv import load_dotenv
from chromadb import HttpClient
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from api.configs.constants import Models


def create_vectordb():
    try:
        load_dotenv()
        directory = './vectordb'
        client = HttpClient(host='localhost', port=8001)
        embeddings = OpenAIEmbeddings(model=Models.EMBEDDING_MODEL)
        vectordb = Chroma(client=client,
                          embedding_function=embeddings,
                          persist_directory=directory,
                          collection_name='documents')
        return vectordb
    except Exception as e:
        print(e)
        return None

def create_llm():
    load_dotenv()
    llm = ChatOpenAI(model=Models.LLM_MODEL)
    return llm
