import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        df['Year'], 
        df['CSIRO Adjusted Sea Level'], 
        color='#4169E1', 
        alpha=0.7, 
        label='Observed Data (1880–2013)'
    )

    # Create first line of best fit
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = np.arange(1880, 2051)
    y_all = res_all.intercept + res_all.slope * x_all
    ax.plot(x_all, y_all, color='#dc143c', linewidth=2, label='Fit: All Data (1880–2050)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = np.arange(2000, 2051)
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    ax.plot(x_recent, y_recent, color='#228B22', linewidth=2, label='Fit: Recent Rate (2000–2050)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend(loc='upper left')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()