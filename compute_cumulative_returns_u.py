import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """ Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols: # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        ## Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY': #drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df

def compute_cumulative_returns(df):
    '''Compute and return the daily return values.'''
    cumulative_returns = df.copy() # copy given DataFrame to match size and column names
    # Compute daily returns for row 1 onwards
    # Formula: daily_ret[t] = (price[t]/price[t-1]) - 1
    # daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    # daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    # Formula: cumulative_ret[t] = (price[t]/price[0]) - 1
    ### Using Pandas
    cumulative_returns = df.cumsum()
    return cumulative_returns

def normalize_data(df):
    return df/ df.ix[0,:]

def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def test_run():
    # Read data
    dates = pd.date_range('2010-07-01', '2010-07-31')
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute cumulative returns
    cumulative_returns = compute_cumulative_returns(df)
    plot_data(cumulative_returns, title="Cumulative returns", ylabel="Cumulative returns")

if __name__ == "__main__":
    test_run()
