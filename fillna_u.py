# Fill forward first
# Fill backward later

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# Function to get path of the symbol
def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

# Reads CSV
def get_data(symbollist,dates):
    df_final=pd.DataFrame(index=dates)
    if "SPY" not in symbollist:
        symbollist.insert(0, "SPY")
    for symbol in symbollist:
        file_path=symbol_to_path(symbol)
        df_temp=pd.read_csv(file_path,parse_dates=True,index_col="Date",
                            usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df_final = df_final.join(df_temp)
        if symbol == "SPY":
            df_final = df_final.dropna(subset=["SPY"])
    return df_final

def plot(df_data):
    ax = df_data.plot(title="Incomplete Data", fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

if __name__ == "__main__":
    # List of symbols
    #symbollist=["PSX", "FAKE1", "FAKE2"]
    symbollist=["FAKE2"]
    # Date range
    start_date="2005-12-31"
    end_date="2014-12-07"

    # Create date range
    idx = pd.date_range(start_date, end_date)

    # Get adjusted close of each symbol
    df_data = get_data(symbollist, idx)
    df_data.fillna(method="ffill", inplace="TRUE") #FILL FORWARD
    df_data.fillna(method="bfill", inplace="TRUE") #BACKWARD FILL 
    plot(df_data)
