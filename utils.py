import pandas as pd

# Centralized safe_get helper function
def safe_get(event, field, default=""):
    """Safely gets a value from an event, handling None/NaN and stripping whitespace."""
    value = event.get(field, default)
    if pd.isna(value) or value is None:
        return default
    return str(value).strip()