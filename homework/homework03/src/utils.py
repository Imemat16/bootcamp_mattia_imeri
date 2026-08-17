import pandas as pd

def get_summary_stats(df):
    """Returns the describe summary and a grouped mean summary."""
    describe_df = df.describe()
    group_df = df.groupby('category').mean(numeric_only=True)
    return describe_df, group_df