import json
from typing import List, Dict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from src.models.llm_models import get_groq_model
from config.settings import settings

@tool
def advanced_lead_qualification(profiles: List[Dict], criteria: Dict) -> List[Dict]:
    """Qualify leads using advanced AI scoring"""
    groq_model = get_groq_model()
    qualified_leads = []
    
    for profile in profiles:
        qualification_prompt = f"""
        Analyze this lead profile for qualification:
        Profile: {json.dumps(profile, indent=2)}

        Qualification Criteria:
        - Target Industry: {criteria.get('industry', 'Technology')}
        - Experience Level: {criteria.get('experience', 'Professional')}
        - Engagement Required: {criteria.get('engagement', 'Medium')}
        - Geographic Focus: {criteria.get('location', 'Any')}

        Provide detailed qualification analysis in JSON:
        {{
            "overall_score": "1-100",
            "category": "hot/warm/cold/unqualified",
            "fit_analysis": {{
                "industry_match": "1-10 with explanation",
                "expertise_relevance": "1-10 with explanation",
                "engagement_potential": "1-10 with explanation",
                "accessibility": "1-10 with explanation"
            }},
            "strengths": ["key", "strengths"],
            "concerns": ["potential", "concerns"],
            "recommended_approach": "personalized outreach strategy",
            "priority_level": "high/medium/low",
            "next_actions": ["specific", "action", "items"],
            "estimated_conversion_probability": "percentage",
            "ideal_contact_timing": "timing recommendation"
        }}
        """
        
        try:
            response = groq_model.invoke([HumanMessage(content=qualification_prompt)])
            qualification = json.loads(response.content)
            profile['qualification'] = qualification
            
            # Only include leads with score > threshold
            if int(qualification.get('overall_score', 0)) > settings.DEFAULT_QUALIFICATION_THRESHOLD:
                qualified_leads.append(profile)
        except Exception as e:
            # Fallback qualification
            profile['qualification'] = {
                "overall_score": 50,
                "category": "warm",
                "fit_analysis": {
                    "industry_match": 5,
                    "expertise_relevance": 5,
                    "engagement_potential": 5,
                    "accessibility": 5
                },
                "strengths": ["Profile found"],
                "concerns": ["Limited data"],
                "recommended_approach": "Standard outreach",
                "priority_level": "medium",
                "next_actions": ["Research further"],
                "estimated_conversion_probability": "25%",
                "ideal_contact_timing": "Business hours"
            }
            qualified_leads.append(profile)
    
    # Sort by qualification score
    qualified_leads.sort(
        key=lambda x: int(x['qualification'].get('overall_score', 0)), 
        reverse=True
    )
    
    return qualified_leads
