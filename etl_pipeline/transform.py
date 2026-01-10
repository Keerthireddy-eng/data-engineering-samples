import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans column names and removes duplicate rows
    """
    df.columns = [c.lower().strip() for c in df.columns]
    df = df.drop_duplicates()
    return df
