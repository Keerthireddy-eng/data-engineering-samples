from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("Starting ETL pipeline...")

    # Extract
    df = extract_data("sample_data.csv")
    print("Data extracted")

    # Transform
    df_clean = transform_data(df)
    print("Data transformed")

    # Load
    load_data(df_clean, "output_data.csv")
    print("Data loaded to output_data.csv")

if __name__ == "__main__":
    run_pipeline()
