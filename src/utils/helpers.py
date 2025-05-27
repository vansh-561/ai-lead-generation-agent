"""Utility functions for the lead generation agent"""

import re
from typing import Dict, Any, List

def clean_text(text: str) -> str:
    """Clean and normalize text input"""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Remove special characters that might cause issues
    text = re.sub(r'[^\w\s\-\.,!?]', '', text)
    
    return text

def validate_search_query(query: str) -> bool:
    """Validate search query input"""
    if not query or len(query.strip()) < 3:
        return False
    
    # Check for minimum meaningful content
    words = query.strip().split()
    return len(words) >= 2

def format_lead_data(lead: Dict[str, Any]) -> Dict[str, Any]:
    """Format lead data for consistent structure"""
    formatted_lead = {
        'name': clean_text(lead.get('name', 'N/A')),
        'bio': clean_text(lead.get('bio', 'N/A')),
        'location': clean_text(lead.get('location', 'N/A')),
        'profile_url': lead.get('profile_url', 'N/A'),
        'expertise': [clean_text(exp) for exp in lead.get('expertise', [])],
        'activity_level': lead.get('activity_level', 'medium'),
        'credibility_score': lead.get('credibility_score', 5)
    }
    
    return formatted_lead

def calculate_lead_priority(qualification: Dict[str, Any]) -> str:
    """Calculate lead priority based on qualification data"""
    try:
        score = int(qualification.get('overall_score', 0))
        
        if score >= 80:
            return "high"
        elif score >= 60:
            return "medium"
        else:
            return "low"
    except (ValueError, TypeError):
        return "medium"
