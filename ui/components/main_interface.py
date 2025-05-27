import streamlit as st

def render_main_interface():
    """Render the main lead generation interface"""
    st.header("🔍 Lead Generation Configuration")
    
    search_query = st.text_input(
        "Target Audience Description",
        placeholder="e.g., AI developers interested in automation tools",
        help="Describe your ideal customer profile"
    )
    
    target_industry = st.selectbox(
        "Primary Industry",
        ["Technology", "Marketing", "Finance", "Healthcare", "Education", "E-commerce", "Consulting", "Other"]
    )
    
    experience_level = st.selectbox(
        "Experience Level",
        ["Entry Level", "Mid Level", "Senior Level", "Executive", "Any"]
    )
    
    geographic_focus = st.selectbox(
        "Geographic Focus",
        ["North America", "Europe", "Asia", "Global", "Any"]
    )
    
    return search_query, target_industry, experience_level, geographic_focus
