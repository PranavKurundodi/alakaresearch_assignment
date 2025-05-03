import pandas as pd
import os
from datetime import datetime

# Define paths
input_folder = "./data/candles/BANKNIFTY/2024-01-10/"
output_folder = "./data/5min_candles/"
target_date = "2024-01-10"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all Parquet files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".parquet.gz"):
        # Read the Parquet file
        file_path = os.path.join(input_folder, filename)
        try:
            df = pd.read_parquet(file_path)
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

        # Convert 'date' column to datetime
        try:
            df['date'] = pd.to_datetime(df['date'])
        except Exception as e:
            print(f"Error converting 'date' column in {filename}: {e}")
            continue

        # Filter for January 10, 2024
        df = df[df['date'].dt.date == pd.to_datetime(target_date).date()]

        # Skip empty files
        if df.empty:
            print(f"No data for {filename} on {target_date}")
            continue

        # Resample to 5-minute intervals
        df.set_index('date', inplace=True)
        candles = df.resample('5min').agg({
            'open': 'first',   # First open in the 5-minute window
            'high': 'max',     # Maximum high in the 5-minute window
            'low': 'min',      # Minimum low in the 5-minute window
            'close': 'last',   # Last close in the 5-minute window
        })

        # Remove any rows with NaN values
        candles.dropna(inplace=True)

        # Save to CSV
        output_file = os.path.join(output_folder, f"5min_{filename.replace('.parquet.gz', '.csv')}")
        candles.to_csv(output_file)
        print(f"Processed {filename} and saved to {output_file}")

        # Bonus: Calculate Fibonacci Pivot Points for the entire day
        daily_high = df['high'].max()
        daily_low = df['low'].min()
        daily_close = df['close'].iloc[-1]  # Use iloc to fix FutureWarning

        # Pivot Point
        P = (daily_high + daily_low + daily_close) / 3

        # Resistance and Support Levels
        diff = daily_high - daily_low
        R1 = P + 0.382 * diff
        R2 = P + 0.618 * diff
        R3 = P + diff
        S1 = P - 0.382 * diff
        S2 = P - 0.618 * diff
        S3 = P - diff

        # Display results
        print(f"\nFibonacci Pivot Points for {filename} on {target_date}:")
        print(f"Pivot Point (P): {P:.2f}")
        print(f"Resistance 1 (R1): {R1:.2f}")
        print(f"Resistance 2 (R2): {R2:.2f}")
        print(f"Resistance 3 (R3): {R3:.2f}")
        print(f"Support 1 (S1): {S1:.2f}")
        print(f"Support 2 (S2): {S2:.2f}")
        print(f"Support 3 (S3): {S3:.2f}")
        print("\n")
