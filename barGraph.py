import matplotlib.pyplot as plt
import pandas as pd


# Data
station = [
    'Kakamega', 'Kisumu', 'Eldoret', 'Kericho'
]
Rainfall = [
    20, 8, 26, 0.3
]

df = pd.read_excel('rainfall.xlsx')

plt.figure(figsize=(10, 6))
plt.bar(station, Rainfall, color='skyblue', edgecolor='black')

plt.title('Daily Rainfall')
plt.xlabel('station')
plt.ylabel('Rainfall')

plt.show()
