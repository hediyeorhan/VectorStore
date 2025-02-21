from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.documents import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyMuPDFLoader
from langchain_chroma import Chroma
from langserve import add_routes
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key = os.getenv("GEMINI_API_KEY"))

# 1.secenek : dokuman icerigi bu sekilde kod icerisine gomulerek verilebilir.
"""
documents = [
    Document(
        page_content="Osmanlı İmparatorluğu, 1299 yılında Osman Gazi tarafından kurulmuş ve 600 yılı aşkın bir süre hüküm sürmüştür.",
        metadata={"source": "osmanli-tarihi"},
    ),
    Document(
        page_content="Malazgirt Meydan Muharebesi, 1071 yılında gerçekleşmiş ve Anadolu'nun kapılarını Türklere açmıştır.",
        metadata={"source": "selcuklu-tarihi"},
    ),
    Document(
        page_content="Cumhuriyet, 29 Ekim 1923'te ilan edilmiş ve Türkiye'nin yönetim şekli olarak kabul edilmiştir.",
        metadata={"source": "turkiye-cumhuriyeti"},
    ),
    Document(
        page_content="İstanbul, 1453 yılında II. Mehmet tarafından fethedilmiş ve Osmanlı İmparatorluğu’nun başkenti olmuştur.",
        metadata={"source": "osmanli-tarihi"},
    ),
    Document(
        page_content="Türkler, Orta Asya'dan batıya doğru göç ederek tarih boyunca birçok devlet kurmuşlardır.",
        metadata={"source": "orta-asya-turkleri"},
    ),
]
"""

# 2.secenek : dokuman icerigi bir dosyadan yuklenebilir.

file_path = "documents.pdf"

loader = PyMuPDFLoader(file_path)
documents = loader.load()


vectorstore = Chroma.from_documents(
    documents,
    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
)

retriever = RunnableLambda(vectorstore.similarity_search).bind(k=1)

message = """
Bu soruyu yalnızca verilen bağlamı kullanarak cevaplayın.

{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([("human", message)])

rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | model

if __name__ == "__main__":
    text = input("Lütfen bilgi almak istediğiniz konuyu söyler misiniz : ")
    response = rag_chain.invoke(text)
    print(response.content)
