"""Data loader module for reading and parsing wellness datasets."""

from __future__ import annotations

import io
from pathlib import Path
from typing import Optional, Union
import pandas as pd

from src.validation import ValidationReport, validate_wellness_data


DEFAULT_SAMPLE_PATH = Path(__file__).resolve().parent.parent / "data" / "sample_wellness.csv"


def load_csv_data(source: Optional[Union[str, Path, io.BytesIO, io.StringIO]] = None) -> pd.DataFrame:
    """
    Loads raw CSV data from a file path, file-like object, or default sample dataset.
    
    Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If the file content cannot be parsed as CSV.
    """
    if source is None:
        source = DEFAULT_SAMPLE_PATH

    if isinstance(source, (str, Path)):
        path = Path(source)
        if not path.exists():
            raise FileNotFoundError(f"Sample data file not found at: {path}")
        return pd.read_csv(path)
    
    # Handle uploaded file object or buffer
    try:
        return pd.read_csv(source)
    except Exception as exc:
        raise ValueError(f"Unable to parse CSV file: {exc}") from exc


def load_and_validate(source: Optional[Union[str, Path, io.BytesIO, io.StringIO]] = None) -> ValidationReport:
    """
    Convenience pipeline that loads CSV data and validates it against the schema.
    """
    try:
        raw_df = load_csv_data(source)
    except FileNotFoundError as fnf_err:
        return ValidationReport(
            is_valid=False,
            schema_errors=[str(fnf_err)],
        )
    except ValueError as val_err:
        return ValidationReport(
            is_valid=False,
            schema_errors=[str(val_err)],
        )
    except Exception as exc:
        return ValidationReport(
            is_valid=False,
            schema_errors=[f"Unexpected error loading dataset: {exc}"],
        )

    return validate_wellness_data(raw_df)


def get_csv_template() -> str:
    """Returns a blank CSV template with headers for users to upload their own data."""
    return "date,sleep_hours,steps,water_glasses,mood_score,activity_minutes\n"
