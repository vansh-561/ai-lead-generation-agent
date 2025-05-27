import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings and configuration"""
    
    # API Keys
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    
    # Model Configuration
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    GEMINI_MODEL: str = "gemini-2.0-flash"
    GROQ_TEMPERATURE: float = 0.1
    GEMINI_TEMPERATURE: float = 0.3
    
    # Search Configuration
    TAVILY_MAX_RESULTS: int = 10
    TAVILY_SEARCH_DEPTH: str = "advanced"
    
    # Lead Generation Configuration
    DEFAULT_QUALIFICATION_THRESHOLD: int = 30
    MAX_PROFILES_TO_PROCESS: int = 10
    
    # UI Configuration
    PAGE_TITLE: str = "🎯 Enhanced AI Lead Generation Agent"
    PAGE_ICON: str = "🎯"
    
    @classmethod
    def get_api_keys_status(cls) -> Dict[str, bool]:
        """Check the status of all required API keys"""
        return {
            "Tavily": bool(cls.TAVILY_API_KEY),
            "Groq": bool(cls.GROQ_API_KEY),
            "Google": bool(cls.GOOGLE_API_KEY)
        }
    
    @classmethod
    def validate_api_keys(cls) -> bool:
        """Validate that all required API keys are present"""
        return all(cls.get_api_keys_status().values())

settings = Settings()
