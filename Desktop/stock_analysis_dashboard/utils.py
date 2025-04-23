import matplotlib.pyplot as plt

def plot_price_with_sma(df):
    """
    Plot the stock price along with its 20-period Simple Moving Average (SMA).
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Stock Price', color='blue')
    plt.plot(df['Date'], df['SMA20'], label='20 Period SMA', color='red')
    plt.title('Stock Price with 20 Period Simple Moving Average (SMA)')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
