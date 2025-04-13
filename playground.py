from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import phi.api

import os
import phi
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
load_dotenv()

phi.api=os.getenv("AGNO_API_KEY")

web_search_agent=Agent(
    name="Web search Agent",
    role="Search the web for the information",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,

)


##Financial Agent

finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()


if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)