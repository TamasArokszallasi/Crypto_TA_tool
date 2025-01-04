import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import datetime
import os

# Function to fetch data for a single pair
def fetch_pair_data(pair, interval, start_ts, end_ts):
    url = "https://api.binance.com/api/v3/klines"
    all_data = []

    while start_ts < end_ts:
        params = {
            "symbol": pair,
            "interval": interval,
            "startTime": start_ts,
            "endTime": end_ts,
            "limit": 1000
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Error fetching data for {pair}: {response.text}")
            break

        data = response.json()

        if not data:
            break

        # Append to list
        all_data.extend(data)

        # Update start_ts to fetch the next batch
        start_ts = data[-1][6] + 1  # Close time of the last entry + 1 ms

    # Convert to DataFrame
    df = pd.DataFrame(all_data, columns=[
        'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close Time', 'Quote Asset Volume', 'Number of Trades',
        'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'
    ])
    if not df.empty:
        df = df[['Open Time', 'Open', 'High', 'Low', 'Close']]
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close']
        df['Date'] = pd.to_datetime(df['Date'], unit='ms')
        df['Pair'] = pair

    return df

# Function to fetch data concurrently for all pairs
def fetch_all_pairs(pairs, interval, start_date, end_date):
    start_ts = int(datetime.datetime.strptime(start_date, "%Y%m%d").timestamp() * 1000)
    end_ts = int(datetime.datetime.strptime(end_date, "%Y%m%d").timestamp() * 1000)

    results = []
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(fetch_pair_data, pair, interval, start_ts, end_ts)
            for pair in pairs
        ]
        for future in futures:
            try:
                result = future.result()
                if not result.empty:
                    results.append(result)
            except Exception as e:
                print(f"Error processing pair: {e}")
    return results

def main():
    # Define pairs, interval, and date range
    pairs = ["BTCUSDT", "ETHUSDT", "DOGEUSDT", "XRPUSDT", "CHZUSDT", "SOLUSDT", "NEOUSDT", "BNBUSDT", "ADAUSDT", "TRXUSDT", "AVAXUSDT", "TONUSDT"]
    interval = "1m"
    start_date = "20190101"
    end_date = "20250101"

    # Fetch data for all pairs
    print("Fetching data...")
    all_data = fetch_all_pairs(pairs, interval, start_date, end_date)

    # Combine data into a single DataFrame
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
    else:
        combined_df = pd.DataFrame()

    # Save to CSV
    current_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_directory, "Crypto_Data.csv")

    if not combined_df.empty:
        combined_df.to_csv(filename, index=False)
        print(f"Data successfully saved to {filename}")
    else:
        print("No data fetched. File not created.")

if __name__ == "__main__":
    main()
