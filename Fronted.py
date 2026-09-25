import streamlit as st
from backend import TranslationBackend

# Initialize Backend Service
backend = TranslationBackend()

# Page Configuration
st.set_page_config(
    page_title="PolyGlot Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stTextArea textarea { font-size: 16px; border-radius: 10px; }
    div[data-testid="stForm"] { border-radius: 15px; }
    .stat-box { font-size: 0.85rem; color: #888; margin-top: -10px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🌐 PolyGlot AI Translator")
st.caption("Translate text seamlessly across languages with a clean, dual-pane interface.")
st.divider()

# Layout Columns
col1, col2 = st.columns(2, gap="large")

# State Management for text clearing
if "source_input" not in st.session_state:
    st.session_state["source_input"] = ""

with col1:
    st.subheader("Source")
    source_lang_label = st.selectbox(
        "Select Input Language",
        options=list(backend.get_supported_languages().keys()),
        index=0,
        key="src_lang"
    )
    
    source_text = st.text_area(
        "Input Text",
        height=220,
        placeholder="Type or paste text to translate here...",
        label_visibility="collapsed",
        key="source_input"
    )
    
    # Text statistics via backend helper
    words, chars = backend.get_word_and_char_count(source_text)
    st.markdown(f"<div class='stat-box'>Words: {words} | Characters: {chars}</div>", unsafe_allow_html=True)

with col2:
    st.subheader("Target")
    target_lang_label = st.selectbox(
        "Select Output Language",
        options=backend.get_target_languages(),
        index=0,
        key="target_lang"
    )

    # Process Translation via Backend
    translated_text = ""
    if source_text.strip():
        translated_text, error = backend.translate_text(
            text=source_text,
            source_label=source_lang_label,
            target_label=target_lang_label
        )
        if error:
            st.error(error)

    st.text_area(
        "Translated Text",
        value=translated_text or "",
        height=220,
        placeholder="Translation will automatically appear here...",
        disabled=True,
        label_visibility="collapsed"
    )

# Footer Controls
st.divider()
c1, c2, c3 = st.columns([2, 1, 1])

with c1:
    st.info("💡 **Tip:** Selecting 'Auto Detect' lets the backend auto-identify the input language.")

# Callback function to clear input state before widget instantiation
def clear_source_text():
    st.session_state["source_input"] = ""

with c3:
    st.button("🧹 Clear Text", use_container_width=True, on_click=clear_source_text)