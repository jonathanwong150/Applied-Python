# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Lab 13

import matplotlib.pyplot as plt
import pandas as pd


def main():
    # import data and set up figure params
    data = pd.read_csv("penguins.csv")
    fig, ax = plt.subplots(2, 1)

    # clean data, group by species, and set up colors list
    data = data.dropna()
    species = data["species"].unique()
    group = data.groupby("species")
    colors = ["orange", "magenta", "cyan"]

    # bar plot
    data.round({"flipper_length_mm": 0})
    count = []
    for item in species:
        count.append(group.get_group(item)["flipper_length_mm"].value_counts())
    for i, item in enumerate(species):
        ax[0].bar(count[i].index, count[i].values,
                  width=1, label=species, alpha=0.4, color=colors[i])
    ax[0].set(title="Penguin flipper lengths (BAR)",
              xlabel="Flipper length (mm)", ylabel="Frequency")
    ax[1].grid(which='major', color='#999999', alpha=0.2)
    ax[0].legend()

    # histogram
    for i, species in enumerate(species):
        ax[1].hist(group.get_group(species)["flipper_length_mm"],
                   bins=36, alpha=0.4, color=colors[i], label=species)
    ax[1].set(title="Penguin flipper lengths (HIST)",
              xlabel="Flipper length (mm)", ylabel="Frequency")
    ax[1].grid(which='major', color='#999999', alpha=0.2)
    ax[1].legend()

    # format and show
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()