# Python ETL Pipeline
This project demonstrates a simple, modular ETL (Extract, Transform, Load) pipeline built using Python.

## Project Structure
- extract.py: Reads raw CSV data
- transform.py: Cleans data and removes duplicates
- load.py: Writes transformed data to an output file
- main.py: Orchestrates the full ETL workflow
- sample_data.csv: Example input dataset

## How It Works
1. Extract data from a CSV file
2. Transform data by cleaning and deduplicating
3. Load cleaned data into an output CSV

## How to Run
From the etl_pipeline folder:
```bash
python main.py
