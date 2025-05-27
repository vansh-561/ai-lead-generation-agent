import json
from typing import List, Dict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from src.models.llm_models import get_gemini_model

@tool
def gemini_lead_enrichment(qualified_leads: List[Dict]) -> List[Dict]:
    """Enrich leads with advanced insights using Gemini"""
    gemini_model = get_gemini_model()
    enriched_leads = []
    
    for lead in qualified_leads:
        enrichment_prompt = f"""
        Provide advanced enrichment for this qualified lead:
        Lead Profile: {json.dumps(lead, indent=2)}

        Generate comprehensive enrichment in JSON format:
        {{
            "market_intelligence": {{
                "industry_trends": "relevant trends affecting this lead",
                "competitive_landscape": "competitive context",
                "market_opportunities": "opportunities to discuss"
            }},
            "personalization_data": {{
                "communication_style": "preferred communication approach",
                "interests": ["personal", "professional", "interests"],
                "pain_points": ["likely", "challenges", "they", "face"],
                "value_drivers": ["what", "motivates", "them"]
            }},
            "outreach_strategy": {{
                "primary_message": "main value proposition",
                "conversation_starters": ["specific", "topics", "to", "discuss"],
                "social_proof": "relevant case studies or examples",
                "call_to_action": "specific next step to propose"
            }},
            "timing_intelligence": {{
                "best_contact_days": ["Monday", "Tuesday"],
                "optimal_time_slots": ["morning", "afternoon"],
                "seasonal_considerations": "timing factors",
                "urgency_indicators": "signs of immediate need"
            }},
            "risk_assessment": {{
                "engagement_likelihood": "high/medium/low",
                "potential_objections": ["likely", "objections"],
                "decision_making_factors": ["key", "decision", "criteria"],
                "timeline_expectations": "expected sales cycle length"
            }}
        }}
        """
        
        try:
            response = gemini_model.invoke([HumanMessage(content=enrichment_prompt)])
            enrichment = json.loads(response.content)
            lead['enrichment'] = enrichment
            enriched_leads.append(lead)
        except Exception as e:
            # Fallback enrichment
            lead['enrichment'] = {
                "market_intelligence": {
                    "industry_trends": "Standard trends",
                    "competitive_landscape": "Competitive market",
                    "market_opportunities": "Growth opportunities"
                },
                "personalization_data": {
                    "communication_style": "Professional",
                    "interests": ["Technology"],
                    "pain_points": ["Efficiency"],
                    "value_drivers": ["ROI"]
                },
                "outreach_strategy": {
                    "primary_message": "Value proposition",
                    "conversation_starters": ["Industry insights"],
                    "social_proof": "Case studies",
                    "call_to_action": "Schedule call"
                },
                "timing_intelligence": {
                    "best_contact_days": ["Tuesday", "Wednesday"],
                    "optimal_time_slots": ["morning"],
                    "seasonal_considerations": "Q4 budget",
                    "urgency_indicators": "None"
                },
                "risk_assessment": {
                    "engagement_likelihood": "medium",
                    "potential_objections": ["Budget"],
                    "decision_making_factors": ["ROI"],
                    "timeline_expectations": "3-6 months"
                }
            }
            enriched_leads.append(lead)
    
    return enriched_leads
