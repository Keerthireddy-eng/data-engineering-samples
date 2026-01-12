# Daily Sales ETL Validation

## Business Context
Sales data is ingested daily from source files into a database.
Any missing or incorrect data can lead to inaccurate revenue reporting.

This project simulates validating daily ETL loads using SQL-based checks.

## Validation Checks
- Row count comparison between days
- Duplicate transaction detection
- Null value checks
- Negative sales amount detection
