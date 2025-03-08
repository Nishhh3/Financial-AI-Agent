from phi.agent import Agent
from phi.model.groq import Groq # for model
from phi.tools.yfinance import YFinanceTools # for financial tools
from phi.tools.duckduckgo import DuckDuckGo # for websearch
# import openai
import os
from dotenv import load_dotenv

Groq.api_key = os.getenv("GROQ_API_KEY")
load_dotenv()

# Web Search Agent
web_search_agent = Agent(
    name = "Web search Agent", 
    role = "Search the web for the information", # role that this agent will be performing
    model = Groq(id="llama-3.3-70b-versatile"), # model used for using tools
    tools = [DuckDuckGo()], # tools used
    instructions = ["Always include sources"], # instructions for the agent
    show_tool_calls = True,
    markdown = True,
)

# Financial Agent 
finance_agent = Agent(
    name = "Financial AI Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions = ["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Multi-AI-Agent (combining Web Search Agent and Financial Agent)
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],  # Add both agents
    model=Groq(id="llama-3.3-70b-versatile"),  # Explicitly set Groq model
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)


multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for the NVDA",stream=True)