import os
import pandas as pd


def save_to_csv(df: pd.DataFrame, path: str) -> None:
    """Save transformed data to CSV. Append if file already exists."""
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if os.path.exists(path):
        df.to_csv(path, mode="a", header=False, index=False)
    else:
        df.to_csv(path, index=False)
