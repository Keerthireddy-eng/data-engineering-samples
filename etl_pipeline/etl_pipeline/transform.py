def transform_data(df):
    """
    Cleans and standardizes the dataset
    """
    df.columns = df.columns.str.lower()
    df = df.dropna()
    return df
