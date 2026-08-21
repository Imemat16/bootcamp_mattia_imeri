import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardizes DataFrame column names to lowercase with underscores."""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def missing_values(df: pd.DataFrame):
    return df.isna().sum()


def split_cabin(df: pd.DataFrame)-> pd.DataFrame:
    
    df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)
    df['Num'] = df['Num'].astype(float)
    
    return df


def add_total_spend(df):

    amenities = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    df['TotalSpend'] = df[amenities].sum(axis=1)

    return df


def add_group_size(df):

    df['GroupSize'] = df.groupby('Group')['Group'].transform('count')

    return df