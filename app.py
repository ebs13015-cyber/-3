import streamlit as st
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.title("🌍 다국어 RAG 문서 검색 및 요약 시스템")
st.write("부산외국어대학교 프로젝트 - 다국어 AI 서비스")

# 샘플 문서 로드
docs = [
    Document(page_content="Global Business Strategy: Foreign market entry requires localized marketing and compliance with local regulations. [English]", metadata={"source": "eng_doc"}),
    Document(page_content="グローバルビジネス戦略: 海外市場への参入には、現地の法律遵守とローカライズされたマーケティングが不可欠です。 [Japanese]", metadata={"source": "jpn_doc"}),
    Document(page_content="全球业务战略: 进入海外市场需要本地化营销以及遵守当地的法律法规。 [Chinese]", metadata={"source": "chn_doc"}),
    Document(page_content="글로벌 비즈니스 전략: 해외 시장 진출을 위해서는 현지 규정 준수와 다국어 소통 능력이 중요합니다. [Korean]", metadata={"source": "kr_doc"})
]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 사용자가 웹에서 입력하는 공간
query = st.text_input("검색할 키워드를 입력하세요 (예: 海外市場, Global, 규정)", "Global")

if st.button("검색 및 분석 실행"):
    relevant_docs = retriever.invoke(query)
    st.subheader("🔍 검색된 다국어 문서 결과")
    for i, doc in enumerate(relevant_docs):
        st.write(f"**{i+1}. 출처: {doc.metadata['source']}**")
        st.info(doc.page_content)
