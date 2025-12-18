"""
TermExtractor-Pro - Main Streamlit Application
AI-powered terminology extraction with bilingual lookup and derivative discovery
"""

import streamlit as st
import os

# Configure page
st.set_page_config(
    page_title="TermExtractor-Pro",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
    .main-header {
        color: #1f77b4;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .feature-box {
        padding: 1.5em;
        border-radius: 0.5em;
        background-color: #f9f9f9;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1em;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.extraction_result = None
    st.session_state.api_stats = {}


def main():
    """Main Streamlit app"""
    
    # Sidebar
    with st.sidebar:
        st.image(
            "https://via.placeholder.com/200x60/1f77b4/ffffff?text=TermExtractor-Pro",
            use_column_width=True
        )
        
        st.markdown("---")
        st.subheader("⚙️ Configuration")
        
        # API Key
        api_key = st.text_input(
            "Anthropic API Key",
            type="password",
            value=os.getenv("ANTHROPIC_API_KEY", ""),
            help="Your Anthropic API key (https://console.anthropic.com)"
        )
        
        if api_key:
            os.environ["ANTHROPIC_API_KEY"] = api_key
        
        st.markdown("---")
        
        st.subheader("📚 About")
        st.info(
            "**TermExtractor-Pro** extracts key terminology from documents "
            "with AI, supports bilingual lookup, and discovers morphological variants."
        )
        
        st.markdown("---")
        
        # Links
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("[📖 Docs](https://github.com)")
        with col2:
            st.markdown("[🐛 Issues](https://github.com)")
        with col3:
            st.markdown("[⭐ GitHub](https://github.com)")
    
    # Main content
    st.markdown('<p class="main-header">🔍 TermExtractor-Pro</p>', unsafe_allow_html=True)
    st.markdown(
        "AI-powered terminology extraction with bilingual lookup and derivative discovery"
    )
    
    st.markdown("---")
    
    # Tabs for different pages
    tab1, tab2, tab3 = st.tabs(["📝 Extract", "📊 Results", "⚙️ Settings"])
    
    with tab1:
        st.subheader("Term Extraction")
        st.write("Upload a document and extract terminology with AI.")
        
        # Show extraction page
        from pages.extraction import show_extraction_page
        show_extraction_page()
    
    with tab2:
        st.subheader("Extraction Results")
        
        if st.session_state.extraction_result:
            from pages.results import show_results_page
            show_results_page(st.session_state.extraction_result)
        else:
            st.info("👉 Extract terms first in the **Extract** tab to see results here.")
    
    with tab3:
        st.subheader("Settings & Configuration")
        from pages.settings import show_settings_page
        show_settings_page()


if __name__ == "__main__":
    # Check API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        st.warning(
            "⚠️ **API Key Required**\n\n"
            "Please enter your Anthropic API key in the sidebar to get started.\n\n"
            "Get one at: https://console.anthropic.com"
        )
    
    main()
