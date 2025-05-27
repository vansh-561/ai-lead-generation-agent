from typing import TypedDict, Annotated, List, Dict, Any
import operator

class AgentState(TypedDict):
    """Define the agent state structure"""
    messages: Annotated[List[Any], operator.add]
    search_query: str
    search_results: List[Dict]
    extracted_leads: List[Dict]
    qualified_leads: List[Dict]
    enriched_leads: List[Dict]
    current_step: str
    lead_count: int
