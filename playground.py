import os
from phi.agent import Agent
from phi.model.groq import Groq # for model
from phi.tools.yfinance import YFinanceTools # for financial tools
from phi.tools.duckduckgo import DuckDuckGo # for websearch
from dotenv import load_dotenv
import phi.api
import phi
from phi.playground import Playground, serve_playground_app
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")
Groq.api_key = os.getenv("GROQ_API_KEY")

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

app = Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)


