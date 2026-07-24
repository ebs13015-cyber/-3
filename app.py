import streamlit as st

st.title("🌍 다국어 RAG 문서 검색 및 요약 시스템")
st.write("부산외국어대학교 프로젝트 - 다국어 AI 서비스")

# 샘플 데이터
sample_data = {
    "Global": "Global Business Strategy: Foreign market entry requires localized marketing and compliance with local regulations. [English]",
    "海外市場": "グローバルビジネス戦略: 海外市場への参入には、現地の法律遵守とローカライズされたマーケティングが不可欠です。 [Japanese]",
    "全球": "全球业务战略: 进入海外市场需要本地化营销以及遵守当地的法律法规。 [Chinese]",
    "글로벌": "글로벌 비즈니스 전략: 해외 시장 진출을 위해서는 현지 규정 준수와 다국어 소통 능력이 중요합니다. [Korean]"
}

query = st.text_input("검색할 키워드를 입력하세요 (예: Global, 海外市場, 全球, 글로벌)", "Global")

if st.button("검색 및 분석 실행"):
    st.subheader("🔍 검색된 다국어 문서 결과")
    found = False
    for key, text in sample_data.items():
        if key.lower() in query.lower() or query.lower() in text.lower():
            st.write(f"**매칭 키워드: {key}**")
            st.info(text)
            found = True
            
    if not found:
        st.warning("관련 다국어 문서를 찾았습니다.")
        st.info(list(sample_data.values())[0])
