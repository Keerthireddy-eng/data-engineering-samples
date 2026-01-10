import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extracts data from a CSV file and returns a DataFrame
    """
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = extract_data("sample_data.csv")
    print(df.head())
