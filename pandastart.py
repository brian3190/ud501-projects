import pandas as pd

def get_max_close(symbol):
    """Return the maximum closing value"""

    df = pd.read_csv("data/{}.csv".format(symbol)) #read in data
    return df['Close'].max()
    # return mean volume of stock
    # return df['Volume'].mean()

def test_run():
    """Funciton called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print "Max close"
        print symbol, get_max_close(symbol)

if __name__ == "__main__": #if run standalone
    test_run()
