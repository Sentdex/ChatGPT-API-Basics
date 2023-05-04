# Embedding用
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
# Vector 格納 / FAISS
from langchain.vectorstores import FAISS
# テキストファイルを読み込む
from langchain.document_loaders import TextLoader
from config import CHUNK_SIZE, CHUNK_OVERLAP, DOCFILE, DB_NAME

import os


def scan(document, db_name=DB_NAME):

    loader = TextLoader(document)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP
    )
    docs = text_splitter.split_documents(documents)
    # print(docs)

    embeddings = OpenAIEmbeddings()

    db = FAISS.from_documents(docs, embeddings)

    db.save_local(db_name)

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = open("authkey.txt").read().strip() 
    scan(DOCFILE, DB_NAME)
