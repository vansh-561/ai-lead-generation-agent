import streamlit as st
from config.settings import settings
from ui.components import render_sidebar, render_main_interface, track_progress
from src.workflow.graph import create_enhanced_lead_generation_graph

def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title=settings.PAGE_TITLE,
        page_icon=settings.PAGE_ICON,
        layout="wide"
    )
    
    st.title(settings.PAGE_TITLE)
    st.markdown("**Powered by Tavily Search, LangGraph, Groq Llama, and Gemini 2.0 Flash**")
    
    # Render sidebar
    render_sidebar()
    
    # Render main interface
    search_query, target_industry, experience_level, geographic_focus = render_main_interface()
    
    if st.button("🚀 Start Enhanced Lead Generation", type="primary"):
        if search_query:
            # Initialize the enhanced graph
            graph = create_enhanced_lead_generation_graph()
            
            # Enhanced initial state
            initial_state = {
                "messages": [],
                "search_query": f"{search_query} {target_industry} {experience_level}",
                "search_results": [],
                "extracted_leads": [],
                "qualified_leads": [],
                "enriched_leads": [],
                "current_step": "starting",
                "lead_count": 0
            }
            
            # Track progress
            track_progress(graph, initial_state)
            
        else:
            st.warning("⚠️ Please enter a target audience description")
    
    # Footer with enhanced information
    st.markdown("---")
    st.markdown("""
    **🔧 Technology Stack:**
    - **Search Engine**: Tavily AI (1,000 free searches/month)
    - **AI Models**: Groq Llama 3.3 70B + Google Gemini 2.0 Flash
    - **Framework**: LangGraph for multi-agent orchestration
    - **Interface**: Streamlit with real-time streaming
    """)

if __name__ == "__main__":
    main()
