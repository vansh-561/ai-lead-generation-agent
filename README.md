# 🎯 Enhanced AI Lead Generation Agent

A powerful AI-driven lead generation system that combines multiple AI models and advanced search capabilities to find, qualify, and enrich potential leads automatically.

## 🚀 Features

- **Multi-AI Integration**: Combines Groq Llama 3.3 70B and Google Gemini 2.0 Flash
- **Advanced Search**: Powered by Tavily AI for comprehensive lead discovery
- **Intelligent Qualification**: AI-powered lead scoring and categorization
- **Lead Enrichment**: Advanced insights and personalization data
- **Comprehensive Reporting**: Detailed CSV reports with actionable insights
- **Real-time Streaming**: Live progress tracking with Streamlit interface

## 🛠️ Technology Stack

- **AI Models**: Groq Llama 3.3 70B, Google Gemini 2.0 Flash
- **Search Engine**: Tavily AI
- **Framework**: LangGraph for multi-agent orchestration
- **Interface**: Streamlit
- **Language**: Python 3.13+

## 📋 Prerequisites

- Python 3.13 or higher
- Poetry for dependency management
- API keys for:
  - Groq API
  - Google AI API
  - Tavily Search API

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-lead-generation-agent
   ```

2. **Install Poetry** (if not already installed)
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies**
   ```bash
   poetry install
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file with your API keys

5. **Activate virtual environment**
   ```bash
   poetry shell
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   poetry run python main.py
   ```

## 🔑 API Keys Setup

Create a `.env` file with the following keys:

```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## 📊 Output

The system generates comprehensive CSV reports containing:

- Lead contact information
- Qualification scores and categories
- Personalization insights
- Outreach strategies
- Timing recommendations
- Risk assessments
