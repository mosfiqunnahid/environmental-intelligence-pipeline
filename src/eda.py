import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/processed/weather_data.csv"
FIGURE_DIR = "reports/figures"


def run_eda():
    os.makedirs(FIGURE_DIR, exist_ok=True)
    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)
    print("\nDescriptive statistics:")
    print(df.describe())

    city_temp = df.groupby("city")["temperature_c"].mean().sort_values()

    plt.figure(figsize=(10, 5))
    city_temp.plot(kind="bar")
    plt.title("Average Temperature by City")
    plt.xlabel("City")
    plt.ylabel("Temperature °C")
    plt.tight_layout()
    plt.savefig(f"{FIGURE_DIR}/average_temperature_by_city.png")
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.scatter(df["humidity"], df["temperature_c"])
    plt.title("Humidity vs Temperature")
    plt.xlabel("Humidity")
    plt.ylabel("Temperature °C")
    plt.tight_layout()
    plt.savefig(f"{FIGURE_DIR}/humidity_vs_temperature.png")
    plt.show()


if __name__ == "__main__":
    run_eda()
