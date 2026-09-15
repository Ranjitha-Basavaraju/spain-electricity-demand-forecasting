from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Live APIs.
ENTSOE_API_KEY = os.getenv("ENTSOE_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Spain's ENTSO-E bidding zone and representative weather cities.
COUNTRY_CODE = os.getenv("COUNTRY_CODE", "ES")
CITIES = ["Madrid", "Valencia", "Bilbao", "Barcelona", "Seville"]

# Runtime and generated artifacts.
DB_PATH = os.getenv("DB_PATH", str(BASE_DIR / "live_data.db"))
MODEL_PATH = str(BASE_DIR / "xgb_model.pkl")
IMPUTER_PATH = str(BASE_DIR / "imputer.pkl")
SCALER_PATH = str(BASE_DIR / "scaler.pkl")
FEATURES_PATH = str(BASE_DIR / "feature_names.pkl")
PEAK_THRESHOLD_PATH = str(BASE_DIR / "peak_threshold.pkl")

# The setting is expressed in minutes: 60 means hourly.
FETCH_INTERVAL_MIN = int(os.getenv("FETCH_INTERVAL_MIN", "60"))
FORECAST_HOURS = int(os.getenv("FORECAST_HOURS", "24"))


def validate_live_credentials() -> None:
    """Raise a clear error before a live API job starts without credentials."""
    missing = [
        name
        for name, value in {
            "ENTSOE_API_KEY": ENTSOE_API_KEY,
            "OPENWEATHER_API_KEY": OPENWEATHER_API_KEY,
        }.items()
        if not value
    ]
    if missing:
        joined = ", ".join(missing)
        raise RuntimeError(f"Missing required environment variable(s): {joined}")
