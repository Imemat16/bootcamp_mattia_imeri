import pandas as pd

def fill_missing_median(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Fills missing (NaN) values in a specific column with the median of that column.
    Operates on a copy of the dataframe to prevent modifying the original data unexpectedly.
    """
    df_clean = df.copy()
    median_val = df_clean[column].median()
    df_clean[column] = df_clean[column].fillna(median_val)
    return df_clean

def drop_missing(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    """
    Drops rows containing missing values. If a subset list of columns is provided, 
    it only checks those specific columns for missing values.
    """
    df_clean = df.copy()
    return df_clean.dropna(subset=subset)

def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Normalizes specified numeric columns to a 0-to-1 scale using Min-Max scaling.
    Formula: (X - X_min) / (X_max - X_min)
    """
    df_clean = df.copy()
    for col in columns:
        min_val = df_clean[col].min()
        max_val = df_clean[col].max()
        # Avoid division by zero if all values in the column are the same
        if max_val != min_val:
            df_clean[col] = (df_clean[col] - min_val) / (max_val - min_val)
        else:
            df_clean[col] = 0.0
    return df_clean