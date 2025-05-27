import streamlit as st
from typing import List, Dict
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from config.settings import settings

@st.cache_resource
def initialize_tavily():
    """Initialize and cache Tavily Search"""
    return TavilySearch(
        max_results=settings.TAVILY_MAX_RESULTS,
        topic="general",
        include_answer=True,
        include_raw_content=True,
        search_depth=settings.TAVILY_SEARCH_DEPTH,
        api_key=settings.TAVILY_API_KEY
    )

@tool
def tavily_lead_search(query: str, platform: str = "quora") -> List[Dict]:
    """Search for potential leads using Tavily Search API"""
    try:
        tavily_tool = initialize_tavily()
        # Construct optimized search query for lead generation
        search_query = f"site:{platform}.com {query} profile expert professional"
        
        # Perform search
        results = tavily_tool.invoke({"query": search_query})
        
        # Process results to extract lead information
        lead_data = []
        if isinstance(results, dict) and 'results' in results:
            for result in results['results'][:settings.TAVILY_MAX_RESULTS]:
                lead_info = {
                    'url': result.get('url', ''),
                    'title': result.get('title', ''),
                    'content': result.get('content', ''),
                    'raw_content': result.get('raw_content', ''),
                    'score': result.get('score', 0)
                }
                lead_data.append(lead_info)
        
        return lead_data
    except Exception as e:
        st.error(f"Tavily search error: {str(e)}")
        return []
