# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Lab 12

import numpy as np
import matplotlib.pyplot as plt

# Description: Sets the axis, title, and coordinates of the graph
# Inputs: Axis, title string, coordinates array with the x and y input
# Returns: None
# Side effects: Set the basic information for a graph
def set_graph(axis, title, coordinates):
    axis.set(title=title, xlabel='x', ylabel='y')
    # Plots the x and y coordinates
    axis.plot(coordinates[0], coordinates[1])

def main():
    # Create a graph with 2 rows and 3 columns
    fig, ax = plt.subplots(2, 3)
    fig.suptitle('Trig!')
    # sin
    sin_x = np.arange(-1*np.pi, np.pi, 0.1)
    sin_y = np.sin(sin_x)
    # cos
    cos_x = np.arange(-1*np.pi, np.pi, 0.1)
    cos_y = np.cos(cos_x)
    # tan
    tan_x = np.arange(-1*np.pi, np.pi, 0.1)
    tan_y = np.tan(tan_x)
    # sinh
    sinh_x = np.arange(-1 * np.pi, np.pi, 0.1)
    sinh_y = np.sinh(sinh_x)
    # cosh
    cosh_x = np.arange(-1 * np.pi, np.pi, 0.1)
    cosh_y = np.cosh(cosh_x)
    # tanh
    tanh_x = np.arange(-1 * np.pi, np.pi, 0.1)
    tanh_y = np.tanh(tanh_x)

    # Create arrays with plot names and inputs
    titles = ["sin(x)","cos(x)","tan(x)","sinh(x)","cosh(x)","tanh(x)"]
    inputs = [(sin_x,sin_y),(cos_x, cos_y),(tan_x, tan_y),(sinh_x, sinh_y),(cosh_x, cosh_y),(tanh_x, tanh_y)]

    i=0
    j=0
    index=0
    for index in range(len(titles)):
        set_graph(ax[i, j], titles[index], inputs[index])
        # When we reach the end of the first row, move to second row
        if j==2:
            i=1
            j=0
        # Increment j value otherwise
        else:
            j+=1
    # Format correctly and show plot
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
