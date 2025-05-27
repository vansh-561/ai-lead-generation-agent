import streamlit as st
from config.settings import settings
from src.tools.tavily_search import initialize_tavily

def render_sidebar():
    """Render the sidebar with configuration options"""
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Check API keys
        api_keys_status = settings.get_api_keys_status()
        
        st.subheader("API Keys Status")
        for service, status in api_keys_status.items():
            st.write(f"{service}: {'✅' if status else '❌'}")
        
        if not settings.validate_api_keys():
            st.error("Please set all required API keys in your .env file")
            st.stop()
        
        # Test Tavily connection
        if st.button("🧪 Test Tavily Connection"):
            try:
                tavily_tool = initialize_tavily()
                test_result = tavily_tool.invoke({"query": "test search"})
                st.success("✅ Tavily connection successful!")
            except Exception as e:
                st.error(f"❌ Tavily connection failed: {str(e)}")
