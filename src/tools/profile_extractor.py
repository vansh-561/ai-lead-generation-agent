import json
from typing import List, Dict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from src.models.llm_models import get_groq_model

@tool
def extract_profile_data(search_results: List[Dict]) -> List[Dict]:
    """Extract structured profile data from search results using AI"""
    groq_model = get_groq_model()
    extracted_profiles = []
    
    for result in search_results:
        if not result.get('content'):
            continue
            
        extraction_prompt = f"""
        Extract lead profile information from this content:
        URL: {result.get('url', 'N/A')}
        Title: {result.get('title', 'N/A')}
        Content: {result.get('content', 'N/A')[:1000]}...

        Extract and return JSON with these fields:
        {{
            "name": "extracted name or username",
            "bio": "professional bio or description",
            "expertise": ["list", "of", "expertise", "areas"],
            "location": "location if mentioned",
            "activity_level": "high/medium/low based on content",
            "topics_discussed": ["topics", "they", "discuss"],
            "engagement_indicators": ["signs", "of", "engagement"],
            "contact_hints": "any contact information or social links",
            "profile_url": "original URL",
            "credibility_score": "1-10 based on content quality"
        }}

        If information is not available, use "N/A" or empty array.
        """
        
        try:
            response = groq_model.invoke([HumanMessage(content=extraction_prompt)])
            profile_data = json.loads(response.content)
            profile_data['source_score'] = result.get('score', 0)
            extracted_profiles.append(profile_data)
        except Exception as e:
            # Fallback extraction
            fallback_profile = {
                "name": result.get('title', 'Unknown').split(' - ')[0],
                "bio": result.get('content', 'N/A')[:200],
                "expertise": [],
                "location": "N/A",
                "activity_level": "medium",
                "topics_discussed": [],
                "engagement_indicators": [],
                "contact_hints": "N/A",
                "profile_url": result.get('url', 'N/A'),
                "credibility_score": 5,
                "source_score": result.get('score', 0)
            }
            extracted_profiles.append(fallback_profile)
    
    return extracted_profiles
