import os
import json
import time
import logging
from datetime import datetime
from typing import Dict, Any, List

import requests
from dotenv import load_dotenv

from config import RAW_DATA_PATH

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def fetch_weather(city: str) -> Dict[str, Any]:
    """Fetch current weather data from OpenWeather API for one city."""
    if not API_KEY:
        raise ValueError("OPENWEATHER_API_KEY is missing. Please add it to your .env file.")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    logging.info(f"Successfully extracted weather data for {city}")
    return response.json()


def save_raw_json(raw_records: List[Dict[str, Any]], path: str = RAW_DATA_PATH) -> None:
    """Save raw API responses for reproducibility."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    output = {"extracted_at_utc": datetime.utcnow().isoformat(), "records": raw_records}

    with open(path, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4)

    logging.info(f"Raw data saved to {path}")


def extract_all_cities(cities: List[str]) -> List[Dict[str, Any]]:
    """Extract weather data for multiple cities."""
    raw_records = []

    for city in cities:
        try:
            data = fetch_weather(city)
            raw_records.append(data)
            time.sleep(1)
        except Exception as error:
            logging.warning(f"Skipping {city} due to error: {error}")

    save_raw_json(raw_records)
    return raw_records
