from langgraph.graph import StateGraph, START, END
from .state import AgentState
from .nodes import (
    search_node,
    extraction_node,
    qualification_node,
    enrichment_node,
    output_node
)

def create_enhanced_lead_generation_graph():
    """Build the enhanced lead generation workflow graph"""
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("search", search_node)
    workflow.add_node("extract", extraction_node)
    workflow.add_node("qualify", qualification_node)
    workflow.add_node("enrich", enrichment_node)
    workflow.add_node("output", output_node)
    
    # Add edges
    workflow.add_edge(START, "search")
    workflow.add_edge("search", "extract")
    workflow.add_edge("extract", "qualify")
    workflow.add_edge("qualify", "enrich")
    workflow.add_edge("enrich", "output")
    workflow.add_edge("output", END)
    
    return workflow.compile()
