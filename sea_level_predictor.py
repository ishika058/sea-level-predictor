import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Import data
df = pd.read_csv("epa-sea-level.csv")


def draw_scatter():
    fig, ax = plt.subplots(figsize=(10,6))
    
    # Scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')
    
    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    return fig, ax


def draw_fit_all_years(ax):
    # Get slope and intercept for line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Predict years through 2050
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_levels = intercept + slope * years_extended
    
    # Plot line
    ax.plot(years_extended, sea_levels, 'r', label='Fit (All years)')
    
    return slope, intercept



def draw_fit_recent_years(ax):
    # Filter data from year 2000 onwards
    recent = df[df['Year'] >= 2000]
    
    # Line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    
    # Predict years through 2050
    years_extended = np.arange(2000, 2051)
    sea_levels = intercept + slope * years_extended
    
    # Plot line
    ax.plot(years_extended, sea_levels, 'green', label='Fit (2000 onwards)')
    
    return slope, intercept



def draw_plot():
    fig, ax = draw_scatter()
    draw_fit_all_years(ax)
    draw_fit_recent_years(ax)
    
    ax.legend()
    
    # Save figure
    fig.savefig('sea_level_plot.png')
    return fig


