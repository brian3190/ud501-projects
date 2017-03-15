import pandas as pd

def test_run():
    start_date="2010-01-22"
    end_date="2010-01-26"
    dates=pd.date_range(start_date, end_date)
    ### First element
    # print dates[0]

    ### Create Empty dataframe
     df1=pd.DataFrame(index=dates)
    # print df1

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True
                        usecols=['Date','Adj Close'], na_values=['nan'])

    # Join the two dataframes using DataFrame.join()
    # df1 = df1.join(dfSPY)

    # Drop NaN Values
    # df1 = df1.dropna()

    # Rename 'Adj Close' column to 'SPY' to prevent clash
    # Error: Index 'Adj Close' has overlap
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    # Method 3: retains rows common to both df1 and dfSPY
    df1 = df1.join(dfSPY, how="inner")

    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp=pd.read_csv("data/{}.csv".format(symbol), index_col='Date',
                            parse_dates=True,usecols=['Date','Adj Close']
                            na_values=['nan'])
        # rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df=df1.join(df_temp) #use default how='left'

    print df1


if __name__ == "__main__":
    test_run()
