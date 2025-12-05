# src/utils/schema.py

class SchemaError(Exception):
    """Custom exception for schema validation errors."""
    pass


def validate_schema(df, required_columns):
    """
    Validates whether required_columns exist in the DataFrame.
    Raises SchemaError if missing columns are found.
    """

    missing = [c for c in required_columns if c not in df.columns]

    if missing:
        raise SchemaError(f"Missing required columns: {missing}")

    return True
