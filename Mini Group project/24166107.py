# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:02:41 2026
@author: John Kefas
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD DATA

df = pd.read_csv('data.csv')

# 2. DATA CLEANING & STATS
# Grouping data to see the difference between Rural and Urban averages
summary_stats = df.groupby('ResidenceType')[['CarDriver', 'BusOther']].mean()
print("--- Average Trips per Person (2002-2023) ---")
print(summary_stats)

# 3. VISUALIZATION 1: BAR CHART (Urban vs Rural 2023)
data_2023 = df[df['Year'] == '2023']
data_2023.plot(kind='bar', x='ResidenceType', y=['CarDriver', 'BusOther'], color=['#1f77b4', '#ff7f0e'])
plt.title('Transport Mode Choice: Car vs Bus (2023)')
plt.ylabel('Average Trips per Person')
plt.xlabel('Area Classification')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('urban_rural_comparison.png')
plt.show()
plt.close()

# 4. VISUALIZATION 2: TREND LINE CHART

trend_df = df[df['ResidenceType'] == 'All areas']
plt.figure(figsize=(8, 5))
plt.plot(trend_df['Year'], trend_df['CarDriver'], marker='o', label='Car Driver')
plt.plot(trend_df['Year'], trend_df['BusOther'], marker='s', label='Local Bus (Non-London)')
plt.title('UK National Travel Trends: 2002 vs 2023')
plt.ylabel('Trips per Person per Year')
plt.legend()
plt.grid(True, linestyle='--')
plt.savefig('travel_trends_line.png')
plt.show()
plt.close()

# 5. VISUALIZATION 3: SCATTER PLOT (Relationship between Walking and Driving)
plt.figure(figsize=(8, 6))
# Plotting walking vs driving to see the correlation across different residence types
for label, df_group in df.groupby('ResidenceType'):
    plt.scatter(df_group['Walk'], df_group['CarDriver'], label=label, s=100, alpha=0.7)

plt.title('Correlation: Walking vs. Driving Trips')
plt.xlabel('Average Walking Trips per Year')
plt.ylabel('Average Driving Trips per Year')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('walking_vs_driving_scatter.png')
plt.show()
plt.close()

print("\nSuccess: Three plots (Bar, Line, Scatter) generated and saved.")
