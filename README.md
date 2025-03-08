# Financial-AI-Agent
This is a financial AI Agent made using Phidata. It is your personal AI assistant for financial matters.

Financial AI Agent is an AI-powered assistant designed to provide real-time financial insights, stock market analysis, and web search capabilities using LLM models and external financial data sources. It leverages Groq LLM models, phi framework, and various tools like YFinanceTools and DuckDuckGo.

## 🚀 Features

- Stock Market Insights: Fetch real-time stock prices, analyst recommendations, and company fundamentals.

- Latest Financial News: Get the latest company news updates.

- Web Search Agent: Searches the web for additional financial information.

- AI-Powered Responses: Uses llama-3.3-70b-versatile from Groq for intelligent analysis.

- Table-based Data Representation: Displays financial data in structured tables.

- Fast and Scalable: Optimized for quick responses and efficient processing

## 🛠 Installation

1. Clone the Repository
```
git clone https://github.com/Nishhh3/Financial-AI-Agent.git
```
2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. ⚙️ Configuration
Environment Variables
Before running the project, set up the required API keys in a .env file:
```
PHI_API_KEY="your_phi_api_key"
GROQ_API_KEY="your_groq_api_key"
```
5. Run and Test
```
python playground.py
```
After running the file, open Phidata Playground on web and select the session (localhost). There you can interact with the agent smoothly.

## Note 
1. 'Finance-agent.py' file contains same agents (without UI/Playground connectivity)
2. 'models.py' file is used to see which models are available. (Select models that is suitable for you from the list)
