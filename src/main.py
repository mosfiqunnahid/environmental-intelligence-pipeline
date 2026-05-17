import logging

from config import CITIES, PROCESSED_DATA_PATH
from extract import extract_all_cities
from transform import transform_weather_data
from validate import validate_weather_data
from load import save_to_csv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def run_pipeline() -> None:
    """Run the complete API ETL pipeline."""
    logging.info("Starting Urban Climate ETL Pipeline")

    raw_records = extract_all_cities(CITIES)
    if not raw_records:
        logging.warning("No records extracted. Pipeline stopped.")
        return

    transformed_df = transform_weather_data(raw_records)
    validated_df = validate_weather_data(transformed_df)
    save_to_csv(validated_df, PROCESSED_DATA_PATH)

    logging.info(f"Pipeline completed. {len(validated_df)} records saved.")


if __name__ == "__main__":
    run_pipeline()
