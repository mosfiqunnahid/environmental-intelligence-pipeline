from datetime import datetime
from typing import Dict, Any, List
import pandas as pd


def transform_weather_record(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Transform one raw OpenWeather JSON response into a flat dictionary."""
    return {
        "city": raw_data.get("name"),
        "country": raw_data.get("sys", {}).get("country"),
        "latitude": raw_data.get("coord", {}).get("lat"),
        "longitude": raw_data.get("coord", {}).get("lon"),
        "temperature_c": raw_data.get("main", {}).get("temp"),
        "feels_like_c": raw_data.get("main", {}).get("feels_like"),
        "humidity": raw_data.get("main", {}).get("humidity"),
        "pressure": raw_data.get("main", {}).get("pressure"),
        "wind_speed": raw_data.get("wind", {}).get("speed"),
        "weather_condition": raw_data.get("weather", [{}])[0].get("main"),
        "weather_description": raw_data.get("weather", [{}])[0].get("description"),
        "collected_at": datetime.utcnow().isoformat()
    }


def transform_weather_data(raw_records: List[Dict[str, Any]]) -> pd.DataFrame:
    """Transform multiple raw API records into a Pandas DataFrame."""
    return pd.DataFrame([transform_weather_record(record) for record in raw_records])
