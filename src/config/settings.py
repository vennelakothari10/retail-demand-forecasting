from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    ROOT: Path = Path(__file__).resolve().parents[2]

    RAW_DATA_DIR: Path = ROOT / "data" / "raw"
    PROCESSED_DATA_DIR: Path = ROOT / "data" / "processed"

    STORE_ID: str = "CA_3"
    DEPT_ID: str = "FOODS_3"

    FORECAST_HORIZON: int = 28
    LAST_TRAIN_DAY: int = 1913

    BACKTEST_ORIGINS: tuple = (1802, 1830, 1858)
    HOLDOUT_ORIGIN: int = 1885


settings = Settings()