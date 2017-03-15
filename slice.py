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


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD'] # SPY will be added in get_data()

    # Get stock data
    df = get_data(symbols, dates)

    # Slice by row range (dates), by column (symbols) using DataFrame.ix[] selector
    print df.ix['2010-01-01':'2010-01-31', ['GOOG', 'IBM']] # the month of January

if __name__ == "__main__":
    test_run()
