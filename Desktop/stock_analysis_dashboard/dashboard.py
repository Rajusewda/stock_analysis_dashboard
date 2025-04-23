import streamlit as st
from data_fetcher import fetch_stock_data
from indicators import add_technical_indicators
from utils import plot_price_with_indicators, plot_rsi, plot_macd

# Streamlit interface
st.title('Stock Market Analysis Dashboard')

# User input for stock symbol
stock_symbol = st.text_input('Enter Stock Symbol', 'AAPL')

# Fetch stock data
if stock_symbol:
    df = fetch_stock_data(stock_symbol)  # Fetch stock data from Yahoo Finance
    df = add_technical_indicators(df)  # Add technical indicators

    # Show data in the dashboard
    st.write(f"Showing data for {stock_symbol}")
    st.dataframe(df.tail())  # Display the last few rows of data with indicators

    # Plot the indicators
    st.subheader('Price with SMA and EMA')
    plot_price_with_indicators(df)

    st.subheader('RSI Indicator')
    plot_rsi(df)

    st.subheader('MACD Indicator')
    plot_macd(df)

    # Optional: You can add more visualizations for other indicators like Stochastic and Bollinger Bands here.
