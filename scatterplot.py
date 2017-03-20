import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data, plot_data

def compute_daily_returns(df):
    """Compute and return the daily return values"""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0 # Set daily returns for row 0 to 0
    return daily_returns

def test_run():
    # Read data
    dates = pd.date_range('2010-01-01', '2010-12-31')
    symbols = ['SPY', 'XOM','GLD']
    df = get_data(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Scatterplot SPY cs XOM
    daily_returns.plot(kind='scatter', x="SPY", y='XOM')
    # takes in x coords and y coords to fit the scatterplot, 1 denotes degree of r? function
    # returns polynomial coefficient and the fit function
    beta_XOM,alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
    print "beta_XOM=", beta_XOM
    print "alpha_XOM=", alpha_XOM
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY']+alpha_XOM, '-',color='r')
    plt.show()

    # Scatterplot SPY vs GOLD
    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    beta_GLD,alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    print "beta_GLD=", beta_GLD
    print "alpha_GLD=", alpha_GLD
    plt.plot(daily_returns['SPY'], beta_GLD*daily_returns['SPY']+alpha_GLD, '-',color='r')
    plt.show()

    # Calculate correlation coefficient
    print daily_returns.corr(method='pearson')

    # Distribution of stocks to the market were very similar to a Gaussian, the returns are normally distributed
    # in many cases, we assume the returns to be normally distributed but it is dangerous, because it ignores kurtosis
    # which is the probability in the tails
    # In the housing loan crisis, assumed returns of mortgages to be independent and
    # the returns should be normally distribued. both the assumptions were wrong
    # 



if __name__ == "__main__":
    test_run()
