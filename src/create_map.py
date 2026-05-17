import pandas as pd
import folium

DATA_PATH = "data/processed/weather_data.csv"
OUTPUT_MAP = "reports/figures/weather_city_map.html"


def create_weather_map():
    df = pd.read_csv(DATA_PATH)
    m = folium.Map(location=[51.16, 10.45], zoom_start=6)

    latest_df = df.sort_values("collected_at").groupby("city").tail(1)

    for _, row in latest_df.iterrows():
        popup_text = (
            f"<b>{row['city']}</b><br>"
            f"Temperature: {row['temperature_c']} °C<br>"
            f"Humidity: {row['humidity']}%<br>"
            f"Wind Speed: {row['wind_speed']} m/s<br>"
            f"Condition: {row['weather_description']}"
        )

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=popup_text,
            tooltip=row["city"]
        ).add_to(m)

    m.save(OUTPUT_MAP)
    print(f"Map saved to {OUTPUT_MAP}")


if __name__ == "__main__":
    create_weather_map()
