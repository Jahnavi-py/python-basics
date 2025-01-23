#data_cleaner.py: Functions to remove duplicates and handle missing values.
import pandas as pd

def remove_duplicates(data, subset=None):
    """
    Removes duplicate rows from the data.
    :param data: A list of dictionaries or a Pandas DataFrame.
    :param subset: Optional; a list of column names to check for duplicates.
    :return: A new DataFrame or list with duplicates removed.
    """
    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, pd.DataFrame):
        df = data
    else:
        raise ValueError("Data must be a list of dictionaries or a Pandas DataFrame.")

    cleaned_data = df.drop_duplicates(subset=subset)
    return cleaned_data if isinstance(data, pd.DataFrame) else cleaned_data.to_dict(orient='records')

def handle_missing_values(data, fill_value=None, method=None):
    """
    Handles missing values in the data.
    :param data: A list of dictionaries or a Pandas DataFrame.
    :param fill_value: Value to replace missing values. Ignored if `method` is specified.
    :param method: Strategy to fill missing values ('mean', 'median', or 'mode').
    :return: A new DataFrame or list with missing values handled.
    """
    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, pd.DataFrame):
        df = data
    else:
        raise ValueError("Data must be a list of dictionaries or a Pandas DataFrame.")

    # Ensure numeric columns are converted properly
    for column in df.select_dtypes(include=['object', 'string']).columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    if method == "mean":
        filled_data = df.fillna(df.mean(numeric_only=True))
    elif method == "median":
        filled_data = df.fillna(df.median(numeric_only=True))
    elif method == "mode":
        filled_data = df.fillna(df.mode().iloc[0])
    elif fill_value is not None:
        filled_data = df.fillna(fill_value)
    else:
        raise ValueError("Either `fill_value` or `method` must be specified.")

    return filled_data if isinstance(data, pd.DataFrame) else filled_data.to_dict(orient='records')
