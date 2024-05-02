"""
Functions for live (dynamic) visualization for the multi-group public goods game
"""

# ====================================================================================================================
# Imports
# ====================================================================================================================


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
plt.rcParams["font.family"] = "Times New Roman"


# ====================================================================================================================
# Average Total Investments Across Periods 
# ====================================================================================================================


def plot_avg_total_investment_periods(data):
    plt.figure(figsize=(7,6))
    # Filter the DataFrame for all three groups
    data_all = data[data['treatment'].isin(['Single Group', 'Multi-Split', 'Multi-Shared'])]

    # Plotting all groups
    sns.lineplot(data=data_all[data_all['treatment'] == 'Single Group'], 
                x="period", y="player_total_investment", 
                label='Single Group', color="#191919", linestyle="--", ci=None)

    sns.lineplot(data=data_all[data_all['treatment'] == 'Multi-Split'], 
                x="period", y="player_total_investment", 
                label='Multi-Split', color="#666", linestyle="--", ci=None)

    sns.lineplot(data=data_all[data_all['treatment'] == 'Multi-Shared'], 
                x="period", y="player_total_investment", 
                label='Multi-Shared', color="#999", linestyle="-.", ci=None)

    plt.ylabel("Average Total\nPublic Good Investment", fontsize=16)
    plt.xlabel("Period", fontsize=16)
    plt.ylim(0, 20)
    plt.xticks(ticks=[1, 5, 10, 15, 20])
    plt.grid(linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


# ====================================================================================================================
# Joint and Marginal Distribution Interactive Plots
# ====================================================================================================================


def plot_joint_distribution(data, period, palette):
    # Filtering data for the specific period
    data_period = data[data['period'] == period]

    # Create joint plot with feasibility regions
    g = sns.jointplot(data=data_period, x='blue_investment', y='green_investment', hue='treatment', kind='scatter', palette=palette)
    
    # Rename axes and update legend for clarity
    g.ax_joint.set_xlabel('Blue Investment')
    g.ax_joint.set_ylabel('Green Investment')
    g.ax_joint.set_xlim(-1, 21)
    g.ax_joint.set_ylim(-1, 21)
    g.ax_joint.set_xticks(range(0, 21, 2))
    g.ax_joint.set_yticks(range(0, 21, 2))

    # Multi-Split bounds
    g.ax_joint.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0], linestyle="--", color=palette["Multi-Split"], label='Multi-Split Boundary')
    # Multi-Shared budget line
    g.ax_joint.plot([0, 20], [20, 0], linestyle="--", color=palette["Multi-Shared"], label='Multi-Shared Budget')
    
    g.ax_joint.legend()


# ====================================================================================================================
# Joint and Marginal Distribution Interactive Plots
# ====================================================================================================================


def update_facet_grid(data, period, palette):
    # Filter data for the specific period and treatments of interest
    filtered_data = data[(data['treatment'].isin(['Multi-Split', 'Multi-Shared'])) & (data['period'] == period)]
    
    # Set up the plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=filtered_data, x='blue_investment', y='green_investment', hue='treatment', style='treatment', palette=palette)
    
    # Add feasibility regions and update labels
    plt.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0], linestyle="--", color=palette["Multi-Split"], label='Multi-Split Boundary')
    plt.plot([0, 20], [20, 0], linestyle="--", color=palette["Multi-Shared"], label='Multi-Shared Budget')
    
    plt.xlabel('Blue Investment')
    plt.ylabel('Green Investment')
    plt.xlim(-1, 21)
    plt.ylim(-1, 21)
    plt.xticks(range(0, 21, 2))
    plt.yticks(range(0, 21, 2))
    plt.grid(True)
    plt.legend()
    plt.show()

