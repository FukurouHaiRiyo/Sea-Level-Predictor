import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    #read data from the csv file
    df = pd.read_csv('epa-sea-level.csv')

    #create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    #create first line of best fit
    bestLine = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xA = np.arange(df['Year'].min(), 2050, 1)
    yA = xA*bestLine.slope + bestLine.intercept

    plt.plot(xA, yA)

    #create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    bestLineB = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    xB = np.arange(2000,2050,1)
    yB = xB*bestLineB.slope + bestLineB.intercept

    plt.plot(xB,yB)

    #add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()