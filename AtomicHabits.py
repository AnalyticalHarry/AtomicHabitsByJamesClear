#importing Libraries
import matplotlib.pyplot as plt
import polars as pl
import pandas as pd
import numpy as np
import seaborn as sns

#function for clculating improvements
def atomic_habit(days):
    #compounded improvement
    better_improvement = 1.01**days  
    #compounded decline
    worse_improvement = 0.99**days   
    #output results
    print("="*40)
    print("Atomic Habit Calculator")
    print("="*40)
    print(f'\nCompound interest for better self-improvement in {days} days is {round(better_improvement,2)}%')
    print(f'\nCompound interest for worse self-improvement in {days} days is {round(worse_improvement,2)}%')
    print("="*40)
    
thirty_days = atomic_habit(365)

days = np.arange(1, 366)
better_growth = [1.01**i for i in days]
decline = [0.99**i for i in days]
no_growth = [1**i for i in days]

sns.set(style="whitegrid", palette="pastel")
plt.figure(figsize=(10,5))
plt.plot(days, better_growth, color="#2ca02c", linewidth=2.5, label="Better Growth")
plt.plot(days, decline, color="#1f77b4", linewidth=2.5, label="Decline")
plt.plot(days, no_growth, color="#ff7f0e", linestyle="--", linewidth=2, label="No Growth")
#labels
plt.xlabel('Number of Days', fontsize=14)
plt.ylabel('Self Improvement Factor', fontsize=14)
plt.title('Impact of Atomic Habits Over 365 Days', fontsize=16, fontweight='bold')
#legend with a better position
plt.legend(loc='upper left', fontsize=12)
plt.grid(True)
#annotations to highlight key aspects
plt.annotate('Significant Growth', xy=(365, better_growth[-1]), xytext=(250, 50),
             arrowprops=dict(facecolor='green', shrink=0.05),
             fontsize=12)
plt.annotate('Significant Decline', xy=(365, decline[-1]), xytext=(250, 0.02),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             fontsize=12)
plt.show()
