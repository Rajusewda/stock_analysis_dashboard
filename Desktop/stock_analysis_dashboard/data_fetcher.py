import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "6mo", interval: str = "1d") -> pd.DataFrame:
    """
    Fetch stock data using yfinance.

    Args:
        ticker (str): Stock symbol (e.g., 'RELIANCE.NS').
        period (str): Time period (default: 6 months).
        interval (str): Data frequency (default: 1 day).

    Returns:
        pd.DataFrame: Historical stock data.
    """
    data = yf.download(ticker, period=period, interval=interval)
    data.dropna(inplace=True)
    return data
