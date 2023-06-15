# For embedding 
from langchain.embeddings.openai import OpenAIEmbeddings
# Vector store
from langchain.vectorstores import FAISS
# For Q&A
from langchain.chains.question_answering import load_qa_chain
# ChatOpenAI GPT 3.5
from langchain.chat_models import ChatOpenAI
from config import DB_NAME, DOCFILE, AUTHPATH
import os
from scanner import scan

def jarvis(query:str, DB_NAME=DB_NAME) -> str:
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(DB_NAME, embeddings)
    embedding_vector = embeddings.embed_query(query)

    docs_and_scores = db.similarity_search_by_vector(embedding_vector)

    chain = load_qa_chain(ChatOpenAI(temperature=0), chain_type="stuff")

    ans = chain({"input_documents": docs_and_scores, "question": query})
    return ans["output_text"]

if __name__ == '__main__':
    os.environ["OPENAI_API_KEY"] = open(AUTHPATH).read().strip() 
    scan(DOCFILE, DB_NAME)
    jarvis(DB_NAME)