import yfinance as yf
import pandas as pd
from indicators import add_technical_indicators
import streamlit as st
import matplotlib.pyplot as plt

def main():
    # Streamlit Interface
    st.title("Stock Market Analysis Dashboard")
    stock_symbol = st.text_input("Enter Stock Symbol", "AAPL")  # Default to AAPL

    if stock_symbol:
        # Download stock data using yfinance
        data = yf.download(stock_symbol, period="1y", interval="1d")

        # Add technical indicators to the stock data
        data = add_technical_indicators(data)

        # Display the data and technical indicators
        st.write(data.tail())  # Show the last few rows of the DataFrame

        # Plot the stock data and technical indicators
        plot_price_with_sma(data)

def plot_price_with_sma(df: pd.DataFrame):
    """
    Plot the stock price along with Simple Moving Average (SMA) and Exponential Moving Average (EMA).
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], label='Stock Price', color='blue')
    plt.plot(df['SMA20'], label='SMA 20', color='red')
    plt.plot(df['EMA20'], label='EMA 20', color='green')

    plt.title('Stock Price with SMA and EMA')
    plt.legend(loc='best')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

if __name__ == "__main__":
    main()
