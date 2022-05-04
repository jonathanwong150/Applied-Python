# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Homework 13

import matplotlib.ticker
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("chicago.csv")
    df = df.dropna()
    fig, ax = plt.subplots(2)
    fig.suptitle('Yearly climatological data for Chicago from 2012 to 2022')
    ax[0].set(title='Last 10 years', xlabel= "Months", ylabel='temp (ºF)')
    ax[1].set(title='Current year and historical averages', xlabel='Months', ylabel='temp (ºF)')
    ten_years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    days = np.arange(0,365)

if __name__ == "__main__":
    main()
