import pandas as pd

def load_data(df: pd.DataFrame, output_path: str):
    """
    Saves transformed data to a CSV file
    """
    df.to_csv(output_path, index=False)
