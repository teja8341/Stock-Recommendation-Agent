import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
# Import both YFinanceTools and DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

# Assuming financial data/recommendation tools are available or handled by the model + web search
# If specific tools like yfinance or similar are part of Agno, they should be added here.

load_dotenv()

class FinanceComparisonAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            model=Gemini(id="gemini-2.0-flash-001"),
            tools=[
                DuckDuckGoTools(),
                # Enable all YFinanceTools options except company_news
                YFinanceTools(
                    company_news=False, # Keep using DuckDuckGo for news
                    analyst_recommendations=True,
                    stock_price=True,
                    company_info=True,
                    stock_fundamentals=True,
                    income_statements=True,
                    key_financial_ratios=True,
                    technical_indicators=True,
                    historical_prices=True,
                )
            ],
            description="An agent that fetches latest news via web search, and retrieves comprehensive financial data (stock price, company info, fundamentals, ratios, recommendations, technicals, history) for comparison between two given stock symbols.",
            instructions=[
               "Use tables to display data."
            ],
            markdown=True,
            show_tool_calls=True,
            debug_mode=True,  
        )

if __name__ == "__main__":
    agent = FinanceComparisonAgent()

    # Example usage: Compare Apple (AAPL) and Microsoft (MSFT)
    stock1 = "AAPL"
    stock2 = "MSFT"

    prompt = f"Provide a detailed report comparing the latest news, fundamentals, and analyst recommendations for {stock1} and {stock2}."

    agent.print_response(prompt, stream=True)

    # Example usage: Compare Tesla (TSLA) and Nvidia (NVDA)
    stock1_alt = "TSLA"
    stock2_alt = "NVDA"

    prompt_alt = f"Provide a report comparing the latest news and financial data for {stock1_alt} and {stock2_alt}."
    # Uncomment the line below to run the second example
    # agent.print_response(prompt_alt, stream=True) 