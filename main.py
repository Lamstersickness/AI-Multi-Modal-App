import streamlit as st
from Summarizer.Summarizer_app import show_summarizer_ui
from Generator.generator_app import show_generator_ui
from Assistant.assistant_app import show_assistant_ui

# Set App Config
st.set_page_config(
    page_title="GenAI Multi-Modal App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme Toggle
theme_mode = st.sidebar.selectbox("🎨 Select Theme", ["Light", "Dark"])

def apply_theme(mode):
    if mode == "Dark":
        st.markdown("""
        <style>
        body { background-color: #121212; color: white; }
        .stTextInput > div > div > input,
        .stTextArea > div > textarea {
            background-color: #333; color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        body { background-color: #f9f9f9; color: black; }
        </style>
        """, unsafe_allow_html=True)

apply_theme(theme_mode)

# ------------------- Sidebar -------------------
with st.sidebar:
    st.image("static/logo.jpg", width=150)
    
    with st.expander("ℹ️ About this App"):
        st.markdown("""
        **GenAI Multi-Modal App** combines:
        - 🧠 Summarization tools
        - 🎨 Generative AI (images, code, speech, captions)
        - 📚 LangChain-based Assistant

        Built with [Streamlit](https://streamlit.io/), [OpenAI](https://openai.com), and [HuggingFace](https://huggingface.co).
        """)

    st.markdown("---")
    st.markdown("🔗 [GitHub Repo](https://github.com/Lamstersickness/GenAI_App)")
    st.markdown("🛠 Maintained by Archit Kumar [LinkedIn](https://www.linkedin.com/in/archit-kumar-aa6375259?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    st.subheader("🔑 OpenAI API Key")
    api_key = st.text_input("Enter your OpenAI API key:", type="password", 
                          help="Get your key from https://platform.openai.com/api-keys")
    st.markdown("---")
    
    if not api_key:
        st.warning("Please enter your OpenAI API key to use the app")
        st.stop()

# ------------------- Main Interface -------------------
st.markdown("<h1 style='text-align: center; color:#BF40BF;'>🧠 GenAI Multi-Modal App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Your all-in-one AI app for summarization, generation, and more.</p>", unsafe_allow_html=True)

# Tabbed UI
tabs = st.tabs([
    "📝 Summarizer Tool",
    "🎨 Generator Tool",
    "📚 Assistant Tool"
])

with tabs[0]:
    show_summarizer_ui(api_key)

with tabs[1]:
    show_generator_ui(api_key)

with tabs[2]:
    show_assistant_ui(api_key)
