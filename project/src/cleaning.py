import pandas as pd

def fill_missing_numeric(df: pd.DataFrame, columns: list, strategy: str = 'median') -> pd.DataFrame:
    """Fills missing values in specified numeric columns using median or mean."""
    df_clean = df.copy()
    for col in columns:
        if strategy == 'median':
            fill_val = df_clean[col].median()
        else:
            fill_val = df_clean[col].mean()
        df_clean[col] = df_clean[col].fillna(fill_val)
    return df_clean

def drop_missing_categorical(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    """Drops rows with missing data in categorical or critical target columns."""
    df_clean = df.copy()
    return df_clean.dropna(subset=subset)

def normalize_features(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Normalizes specified numeric columns using Min-Max scaling."""
    df_clean = df.copy()
    for col in columns:
        min_val = df_clean[col].min()
        max_val = df_clean[col].max()
        if max_val != min_val:
            df_clean[col] = (df_clean[col] - min_val) / (max_val - min_val)
        else:
            df_clean[col] = 0.0
    return df_clean