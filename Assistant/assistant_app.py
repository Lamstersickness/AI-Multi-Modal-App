import streamlit as st
from .document_qna import show_document_qna
from .url_qna import show_url_qna

def show_assistant_ui(api_key=None):
    st.header("🧠 LangChain Assistant Tools")
    st.markdown("Interact with uploaded documents or news URLs using LLM-powered QnA.")
    
    if not api_key:
        st.error("OpenAI API key is required")
        return

    tabs = st.tabs(["📄 Document QnA", "🌐 News Article QnA"])

    with tabs[0]:
        st.subheader("📎 Ask Questions from Uploaded Documents")
        
        uploaded_files = st.file_uploader(
            "Upload up to 3 PDF/DOCX files",
            type=["pdf", "docx"],
            accept_multiple_files=True
        )

        if uploaded_files:
            show_document_qna(uploaded_files, api_key)
        else:
            st.info("Please upload at least one document to begin.")

    with tabs[1]:
        st.subheader("📰 Ask Questions from News URLs")
        show_url_qna(api_key)