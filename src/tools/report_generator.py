import pandas as pd
from typing import List, Dict
from datetime import datetime
from langchain_core.tools import tool

@tool
def create_comprehensive_report(enriched_leads: List[Dict], search_query: str) -> str:
    """Create comprehensive lead generation report"""
    try:
        # Prepare comprehensive data for export
        report_data = []
        for lead in enriched_leads:
            qualification = lead.get('qualification', {})
            enrichment = lead.get('enrichment', {})
            
            row = {
                'Lead_Name': lead.get('name', 'N/A'),
                'Profile_URL': lead.get('profile_url', 'N/A'),
                'Bio': lead.get('bio', 'N/A')[:200],
                'Location': lead.get('location', 'N/A'),
                'Expertise_Areas': ', '.join(lead.get('expertise', [])),
                'Activity_Level': lead.get('activity_level', 'N/A'),
                'Qualification_Score': qualification.get('overall_score', 'N/A'),
                'Lead_Category': qualification.get('category', 'N/A'),
                'Priority_Level': qualification.get('priority_level', 'N/A'),
                'Industry_Match': qualification.get('fit_analysis', {}).get('industry_match', 'N/A'),
                'Engagement_Potential': qualification.get('fit_analysis', {}).get('engagement_potential', 'N/A'),
                'Conversion_Probability': qualification.get('estimated_conversion_probability', 'N/A'),
                'Recommended_Approach': qualification.get('recommended_approach', 'N/A'),
                'Primary_Message': enrichment.get('outreach_strategy', {}).get('primary_message', 'N/A'),
                'Conversation_Starters': ', '.join(enrichment.get('outreach_strategy', {}).get('conversation_starters', [])),
                'Best_Contact_Days': ', '.join(enrichment.get('timing_intelligence', {}).get('best_contact_days', [])),
                'Pain_Points': ', '.join(enrichment.get('personalization_data', {}).get('pain_points', [])),
                'Value_Drivers': ', '.join(enrichment.get('personalization_data', {}).get('value_drivers', [])),
                'Next_Actions': ', '.join(qualification.get('next_actions', [])),
                'Risk_Level': enrichment.get('risk_assessment', {}).get('engagement_likelihood', 'N/A')
            }
            report_data.append(row)
        
        # Create DataFrame and save
        df = pd.DataFrame(report_data)
        filename = f"leads_{search_query.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)
        
        # Generate summary statistics
        total_leads = len(enriched_leads)
        hot_leads = len([l for l in enriched_leads if l.get('qualification', {}).get('category') == 'hot'])
        warm_leads = len([l for l in enriched_leads if l.get('qualification', {}).get('category') == 'warm'])
        
        summary = f"""
        Lead Generation Report Summary:
        - Total Qualified Leads: {total_leads}
        - Hot Leads: {hot_leads}
        - Warm Leads: {warm_leads}
        - Report saved to: {filename}
        """
        
        return summary
    except Exception as e:
        return f"Error creating report: {str(e)}"
