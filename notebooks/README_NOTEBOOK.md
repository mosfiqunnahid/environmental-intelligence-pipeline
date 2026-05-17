# EDA Notebook Guide

Create `01_eda_environmental_analysis.ipynb` and run:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed/weather_data.csv")
df.head()
df.info()
df.describe()
df.isnull().sum()

df.groupby("city")["temperature_c"].mean().sort_values().plot(kind="bar")
plt.title("Average Temperature by City")
plt.ylabel("Temperature °C")
plt.show()

df.plot.scatter(x="humidity", y="temperature_c")
plt.title("Humidity vs Temperature")
plt.show()
```
