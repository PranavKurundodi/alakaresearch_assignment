# Alaka Research Assignment: BANKNIFTY 5-Minute Candles and Fibonacci Pivot Points

## Overview

This repository contains the solution for the Alaka Research assignment. The task involves downloading financial data for BANKNIFTY options dated January 10, 2024, processing the data to create 5-minute candlestick data, calculating Fibonacci Pivot Points for the same date, and storing the results in a GitHub repository.

## Assignment Requirements

- **Download Data**: Use `s3cmd` to download Parquet files from a Cloudflare R2 bucket.
- **Process Data**:
  - Filter the data for January 10, 2024.
  - Generate 5-minute candles (Open, High, Low, Close) from 1-minute candlestick data.
  - Save the 5-minute candles as CSV files in the `data/5min_candles/` directory.
- **Bonus Feature**: Calculate Fibonacci Pivot Points (P, R1, R2, R3, S1, S2, S3) for January 10, 2024, and display them.
- **Store in a Repository**: Commit the script and output CSVs to a GitHub repository and share the link.

## Repository Structure

- **`process_candles.py`**: The Python script that processes the Parquet files, generates 5-minute candles, and calculates Fibonacci Pivot Points.
- **`data/5min_candles/`**: Directory containing the output CSV files (e.g., `5min_46900PE.csv`, `5min_47100CE.csv`).
- **`README.md`**: This file, providing an overview, setup instructions, and usage details.

## Prerequisites

To run the script, you’ll need the following:

- **Python 3.x**: Ensure Python is installed on your system.
- **Required Libraries**:
  - `pandas`: For data processing.
  - `pyarrow`: For reading Parquet files.
  - Install them using:
    ```bash
    pip install pandas pyarrow
    ```
- **s3cmd**: To download the input data from Cloudflare R2.
  - Install using:
    ```bash
    pip install s3cmd
    ```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PranavKurundodi/alakaresearch_assignment.git
   cd alakaresearch_assignment
   ```

2. **Download the Input Data using s3cmd**:
   
   This creates the directory `data/candles/BANKNIFTY/2024-01-10/` with Parquet files (e.g., `46900PE.parquet.gz`).

3. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install pandas pyarrow
   ```

## Running the Script

1. **Process the Data**:
   Run the `process_candles.py` script to generate 5-minute candles and calculate Fibonacci Pivot Points:
   ```bash
   python process_candles.py
   ```

2. **Script Output**:
   - **5-Minute Candles**:
     - The script generates CSV files in `data/5min_candles/` (e.g., `5min_46900PE.csv`).
     - Each CSV contains the following columns:
       - `date`: 5-minute intervals for January 10, 2024 (e.g., `2024-01-10 09:15:00`).
       - `open`: First `open` price in the 5-minute window.
       - `high`: Maximum `high` price in the 5-minute window.
       - `low`: Minimum `low` price in the 5-minute window.
       - `close`: Last `close` price in the 5-minute window.
   - **Fibonacci Pivot Points**:
     - The script prints Fibonacci Pivot Points (P, R1, R2, R3, S1, S2, S3) for each file to the console.
     - Example output:
       ```
       Fibonacci Pivot Points for 46900PE.parquet.gz on 2024-01-10:
       Pivot Point (P): 123.45
       Resistance 1 (R1): 130.67
       Resistance 2 (R2): 135.89
       Resistance 3 (R3): 145.00
       Support 1 (S1): 116.23
       Support 2 (S2): 111.01
       Support 3 (S3): 101.90
       ```

## Author

- **Name**: Pranav Kurundodi
- **Email**: pranavkurundodi@gmail.com
