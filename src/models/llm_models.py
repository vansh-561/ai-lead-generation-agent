import streamlit as st
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings

@st.cache_resource
def initialize_models():
    """Initialize and cache LLM models"""
    groq_model = ChatGroq(
        model=settings.GROQ_MODEL,
        api_key=settings.GROQ_API_KEY,
        temperature=settings.GROQ_TEMPERATURE
    )
    
    gemini_model = ChatGoogleGenerativeAI(
        model=settings.GEMINI_MODEL,
        api_key=settings.GOOGLE_API_KEY,
        temperature=settings.GEMINI_TEMPERATURE
    )
    
    return groq_model, gemini_model

def get_groq_model():
    """Get Groq model instance"""
    groq_model, _ = initialize_models()
    return groq_model

def get_gemini_model():
    """Get Gemini model instance"""
    _, gemini_model = initialize_models()
    return gemini_model
