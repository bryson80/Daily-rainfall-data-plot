import pandas as pd
import matplotlib as plt

# data
df = pd.read_excel(
    '/Users/mac/Documents/Documents/KADI GYM/Daily-rainfall-data-plot/Project1.xlsx')

# plot
plt.figure(figsize=(10, 6))
plt.bar(df['STATION'], df['RAINFALL'], color='lightgreen', edgecolor='black')
plt.title('DAILY Rainfall')
plt.xlabel('Day')
plt.ylabel('Rainfall (mm)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
