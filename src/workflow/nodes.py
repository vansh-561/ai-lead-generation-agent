import streamlit as st
import time
from langchain_core.messages import AIMessage
from src.workflow.state import AgentState
from src.tools import (
    tavily_lead_search,
    extract_profile_data,
    advanced_lead_qualification,
    gemini_lead_enrichment,
    create_comprehensive_report
)

def search_node(state: AgentState):
    """Search for potential leads using Tavily"""
    st.info("🔍 Searching for potential leads...")
    
    # Perform Tavily search
    search_results = tavily_lead_search.invoke({
        "query": state['search_query'],
        "platform": "quora"
    })
    
    return {
        "messages": [AIMessage(content=f"Found {len(search_results)} potential leads from search")],
        "search_results": search_results,
        "current_step": "search_completed",
        "lead_count": len(search_results)
    }

def extraction_node(state: AgentState):
    """Extract structured profile data"""
    st.info("📊 Extracting profile data...")
    
    extracted_profiles = extract_profile_data.invoke({
        "search_results": state.get('search_results', [])
    })
    
    return {
        "messages": [AIMessage(content=f"Extracted {len(extracted_profiles)} structured profiles")],
        "extracted_leads": extracted_profiles,
        "current_step": "extraction_completed"
    }

def qualification_node(state: AgentState):
    """Qualify and score leads"""
    st.info("🎯 Qualifying leads with AI scoring...")
    
    # Define qualification criteria
    criteria = {
        "industry": "Technology",
        "experience": "Professional",
        "engagement": "Medium",
        "location": "Any"
    }
    
    qualified_leads = advanced_lead_qualification.invoke({
        "profiles": state.get('extracted_leads', []),
        "criteria": criteria
    })
    
    return {
        "messages": [AIMessage(content=f"Qualified {len(qualified_leads)} high-potential leads")],
        "qualified_leads": qualified_leads,
        "current_step": "qualification_completed"
    }

def enrichment_node(state: AgentState):
    """Enrich leads with advanced insights"""
    st.info("✨ Enriching leads with AI insights...")
    
    enriched_leads = gemini_lead_enrichment.invoke({
        "qualified_leads": state.get('qualified_leads', [])
    })
    
    return {
        "messages": [AIMessage(content=f"Enriched {len(enriched_leads)} leads with advanced insights")],
        "enriched_leads": enriched_leads,
        "current_step": "enrichment_completed"
    }

def output_node(state: AgentState):
    """Generate final comprehensive report"""
    st.info("📋 Generating comprehensive report...")
    
    report_summary = create_comprehensive_report.invoke({
        "enriched_leads": state.get('enriched_leads', []),
        "search_query": state['search_query']
    })
    
    return {
        "messages": [AIMessage(content=f"Process completed! {report_summary}")],
        "current_step": "completed"
    }
