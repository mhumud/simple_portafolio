# Portfolio Profit and Annualized Return Calculator

This tool allows you to calculate the profit and annualized return of a stock portfolio over a specified date range. It fetches historical stock prices using the Yahoo Finance API via the `yfinance` library.

## Features

- Add multiple stocks to your portfolio with specified quantities.
- Calculate total profit over a given date range.
- Calculate annualized return based on the profit and initial investment.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/mhumud/portfolio_calculator.git
    cd portfolio_calculator
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

To use the portfolio calculator, run the script with the following command-line arguments:
```
python main.py --stocks TICKER1:QUANTITY1 TICKER2:QUANTITY2 ... --start_date YYYY-MM-DD --end_date YYYY-MM-DD
```

## Parameters

- `--stocks`: A space-separated list of stock tickers and their corresponding quantities in the format TICKER:QUANTITY. For example, `AAPL:10 MSFT:5`.
- `--start_date`: The start date for the calculation in the format `YYYY-MM-DD`.
- `--end_date`: The end date for the calculation in the format `YYYY-MM-DD`.

## Example

To calculate the profit and annualized return for a portfolio containing 10 shares of Apple (AAPL) and 5 shares of Microsoft (MSFT) from January 1, 2023, to December 31, 2023, run:
```
python main.py --stocks AAPL:10 MSFT:5 --start_date 2023-01-01 --end_date 2023-12-31
```

## Output

The tool will output the calculated profit and annualized return:
```
Profit: <calculated profit>
Annualized Return: <calculated annualized return>
```

## Why yfinance?

I chose the `yfinance` library for its simplicity and ease of use. It provides straightforward access to historical stock data without requiring API keys, making it accessible for quick calculations and prototyping. The library handles data retrieval seamlessly, allowing for a focus on portfolio analysis rather than setup complexities.
