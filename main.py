import argparse
from datetime import datetime
import yfinance as yf

class Stock:
    def __init__(self, name: str):
        self.name = name

    def price(self, date: datetime) -> float:
        # Format the date to match yfinance's expected format
        date_str = date.strftime("%Y-%m-%d")

        try:
            # Fetch historical data for the given stock symbol
            stock_data = yf.Ticker(self.name)
            historical_data = stock_data.history(start=date_str, end=None)

            if historical_data.empty:
                raise ValueError(f"{self.name}: No price data available for {date_str}")

            # Extract the closing price for the first date
            return float(historical_data['Close'].iloc[0])

        except Exception as e:
            print(f"Error occurred: {e}")
            raise

class Portfolio:
    def __init__(self):
        self.stocks = []  # List of tuples (Stock, quantity)

    def add_stock(self, stock: Stock, quantity: int):
        self.stocks.append((stock, quantity))

    def profit(self, start_date: datetime, end_date: datetime) -> float:
        start_value = sum(stock.price(start_date) * quantity for stock, quantity in self.stocks)
        end_value = sum(stock.price(end_date) * quantity for stock, quantity in self.stocks)
        return end_value - start_value

    def annualized_return(self, start_date: datetime, end_date: datetime) -> float:
        profit = self.profit(start_date, end_date)
        start_value = sum(stock.price(start_date) * quantity for stock, quantity in self.stocks)
        
        days = (end_date - start_date).days
        if days <= 0 or start_value <= 0:
            return 0.0
        
        annualized_return = ((profit / start_value) + 1) ** (365 / days) - 1
        return annualized_return

# portfolio = Portfolio()
# portfolio.add_stock(Stock("AAPL"), 10)
# portfolio.add_stock(Stock("MSFT"), 5)

# start_date = datetime(2023, 1, 1)
# end_date = datetime(2023, 12, 31)

# print("Profit:", portfolio.profit(start_date, end_date))
# print("Annualized Return:", portfolio.annualized_return(start_date, end_date))

def main():
    parser = argparse.ArgumentParser(description="Calculate Portfolio Profit and Annualized Return.")
    parser.add_argument('--stocks', nargs='+', required=True, help="Stock tickers and quantities in the format 'TICKER:QUANTITY'.")
    parser.add_argument('--start_date', type=str, required=True, help="Start date in YYYY-MM-DD format.")
    parser.add_argument('--end_date', type=str, required=True, help="End date in YYYY-MM-DD format.")

    args = parser.parse_args()

    # Parse dates
    try:
        start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(args.end_date, "%Y-%m-%d")
    except Exception as e:
        raise Exception(f"Error parsing dates: {e}")


    # Create portfolio and add stocks
    portfolio = Portfolio()
    for stock_entry in args.stocks:
        ticker, quantity = stock_entry.split(':')
        portfolio.add_stock(Stock(ticker), int(quantity))

    # Calculate and display profit and annualized return
    print("Profit:", portfolio.profit(start_date, end_date))
    print("Annualized Return:", portfolio.annualized_return(start_date, end_date))

if __name__ == "__main__":
    main()
