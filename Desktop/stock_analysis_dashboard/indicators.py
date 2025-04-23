import pandas as pd
import ta  # Technical Analysis Library in Python

def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators to the stock data.
    """
    # Ensure df['Close'] is a 1D pandas Series
    if isinstance(df['Close'], pd.Series) and df['Close'].ndim == 1:
        print("Close column is already a 1D Series")
    else:
        print("Flattening the Close column to 1D")
        df['Close'] = df['Close'].values.flatten()  # Flatten to 1D if necessary

    print("After Flattening:")
    print(f"Shape of 'Close': {df['Close'].shape}")
    print(f"Type of 'Close': {type(df['Close'])}")

    # Moving Averages
    df['SMA20'] = df['Close'].rolling(window=20).mean()
    df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()

    # RSI (Relative Strength Index) - Ensure df['Close'] is a pandas Series
    try:
        rsi = ta.momentum.RSIIndicator(df['Close'], window=14)  # Use pandas Series directly
        df['RSI'] = rsi.rsi()
    except Exception as e:
        print(f"Error in calculating RSI: {e}")

    # MACD (Moving Average Convergence Divergence)
    try:
        macd = ta.trend.MACD(df['Close'])
        df['MACD'] = macd.macd()
    except Exception as e:
        print(f"Error in calculating MACD: {e}")

    # Stochastic Oscillator (%K and %D)
    try:
        stoch = ta.momentum.StochasticOscillator(df['High'], df['Low'], df['Close'], window=14, smooth_window=3)
        df['Stochastic'] = stoch.stoch().iloc[:, 0]  # Only %K value (first column)
    except Exception as e:
        print(f"Error in calculating Stochastic Oscillator: {e}")

    # Bollinger Bands
    try:
        bollinger = ta.volatility.BollingerBands(df['Close'], window=20, window_dev=2)
        df['BB_upper'] = bollinger.bollinger_hband()
        df['BB_lower'] = bollinger.bollinger_lband()
    except Exception as e:
        print(f"Error in calculating Bollinger Bands: {e}")

    return df
