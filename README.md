# Finance Comparison Agent

A powerful financial analysis tool that provides detailed comparisons between stocks using real-time data and news. Built with Python using the Agno framework, this agent leverages Google's Gemini AI model to deliver comprehensive stock comparison reports.

## Features

- Real-time stock price comparisons
- Company fundamental analysis
- Technical indicators comparison
- Analyst recommendations
- Latest news integration
- Financial ratios analysis
- Historical price data
- Income statement comparisons

## Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini AI model

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd FinanceAgent
```

2. Install the required dependencies:
```bash
pip install agno python-dotenv
```

3. Create a `.env` file in the root directory:
```bash
# Create .env file
touch .env
```

4. Add your Google API Key to the `.env` file:
```
GOOGLE_API_KEY="your-google-api-key"
```

## Usage

### Basic Usage

Run the default comparison between Apple (AAPL) and Microsoft (MSFT):

```bash
python finance_comparison_agent.py
```

### Custom Comparisons

To compare different stocks, modify the stock symbols in `finance_comparison_agent.py`:

```python
stock1 = "TSLA"  # Tesla
stock2 = "NVDA"  # NVIDIA

prompt = f"Provide a detailed report comparing the latest news, fundamentals, and analyst recommendations for {stock1} and {stock2}."
agent.print_response(prompt, stream=True)
```

## Output Format

The agent provides structured output including:
- Tabulated financial data
- Recent news comparisons
- Technical analysis
- Fundamental metrics
- Analyst recommendations

## Configuration Options

The agent can be customized by modifying the following parameters in `finance_comparison_agent.py`:

- `company_news`: Toggle news fetching (Default: False, uses DuckDuckGo instead)
- `analyst_recommendations`: Include analyst recommendations (Default: True)
- `stock_fundamentals`: Include fundamental analysis (Default: True)
- `technical_indicators`: Include technical analysis (Default: True)
- And more...

## Environment Variables

Required environment variables:
- `GOOGLE_API_KEY`: Your Google API key for Gemini AI model

## Troubleshooting

Common issues and solutions:

1. API Key Error:
   - Ensure your `.env` file exists and contains the correct API key
   - Verify the API key is valid and has necessary permissions

2. Data Fetching Issues:
   - Check your internet connection
   - Verify the stock symbols are valid
   - Ensure you're not hitting API rate limits

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

[Your chosen license]

## Acknowledgments

- Built with [Agno Framework](https://github.com/agno)
- Uses Google's Gemini AI model
- Financial data provided by YFinance
- News data from DuckDuckGo 