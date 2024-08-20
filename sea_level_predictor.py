import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", header=0)

    # Create scatter plot
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)

    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = slope1 * x_pred1 + intercept1
    plt.plot(x_pred1, y_pred1, color='red')

    # Create second line of best fit
    df_post_2k = df[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_post_2k["Year"], df_post_2k["CSIRO Adjusted Sea Level"])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = slope2 * x_pred2 + intercept2
    plt.plot(x_pred2, y_pred2, color='green')
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
