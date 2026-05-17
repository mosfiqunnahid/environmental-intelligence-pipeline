import pandas as pd

REQUIRED_COLUMNS = [
    "city", "country", "latitude", "longitude", "temperature_c",
    "humidity", "pressure", "wind_speed", "collected_at"
]


def validate_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply basic data quality checks and return cleaned DataFrame."""
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df = df.drop_duplicates()
    df = df.dropna(subset=["city", "temperature_c", "humidity", "collected_at"])

    df = df[
        (df["temperature_c"] > -50) &
        (df["temperature_c"] < 60) &
        (df["humidity"] >= 0) &
        (df["humidity"] <= 100) &
        (df["wind_speed"] >= 0)
    ]

    return df
