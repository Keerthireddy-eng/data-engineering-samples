import pandas as pd

def extract_data(file_path):
    """
    Reads data from a CSV file and returns a DataFrame
    """
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = extract_data("data/input.csv")
    print(df.head())
