import pandas as pd
import talib

# Function to determine if the expected movement happened within 5 days
def check_movement(index, expectation, df):
    for day in range(1, 6):
        if index + day >= len(df):
            break
        if expectation == 'bullish' and df['Close'][index + day] > df['Close'][index]:
            return f'True on day {day}', day
        elif expectation == 'bearish' and df['Close'][index + day] < df['Close'][index]:
            return f'True on day {day}', day
    return 'False', None

# Analyze data with talib
def analyze_data(df):
    # Define expected movements for the top 20 patterns
    pattern_expectations = {
        'Hammer': ('bullish', 'CDLHAMMER'),
        'Shooting Star': ('bearish', 'CDLSHOOTINGSTAR'),
        'Bullish Engulfing': ('bullish', 'CDLENGULFING'),
        'Bearish Engulfing': ('bearish', 'CDLENGULFING'),
        'Evening Star': ('bearish', 'CDLEVENINGSTAR'),
        'Morning Star': ('bullish', 'CDLMORNINGSTAR'),
        'Bullish Harami': ('bullish', 'CDLHARAMI'),
        'Bearish Harami': ('bearish', 'CDLHARAMI'),
        'Three Black Crows': ('bearish', 'CDL3BLACKCROWS'),
        'Three White Soldiers': ('bullish', 'CDL3WHITESOLDIERS'),
        'Gravestone Doji': ('bearish', 'CDLGRAVESTONEDOJI'),
        'Dragonfly Doji': ('bullish', 'CDLDRAGONFLYDOJI'),
        'Bullish Long Legged Doji': ('bullish','CDLLONGLEGGEDDOJI'),
        'Bearish Long Legged Doji': ('bearish','CDLLONGLEGGEDDOJI'),
        'Hanging Man': ('bearish', 'CDLHANGINGMAN'),
        'Inverted Hammer': ('bullish', 'CDLINVERTEDHAMMER'),
        'Piercing Line': ('bullish', 'CDLPIERCING'),
        'Dark Cloud Cover': ('bearish', 'CDLDARKCLOUDCOVER'),
    }

    # Prepare a list to store detected patterns
    detected_patterns = []

    # Detect each pattern and add corresponding rows to the detected_patterns list
    for pattern_name, (expectation, pattern_function) in pattern_expectations.items():
        pattern_detection = getattr(talib, pattern_function)(
            df['Open'].astype(float),
            df['High'].astype(float),
            df['Low'].astype(float),
            df['Close'].astype(float)
        )
        for i in range(len(df)):
            if pattern_detection[i] != 0:
                # Apply condition for bullish patterns
                if expectation == 'bullish' and float(df['Close'][i]) <= float(df['Open'][i]):
                    continue
                # Apply condition for bearish patterns
                if expectation == 'bearish' and float(df['Close'][i]) >= float(df['Open'][i]):
                    continue
                # For indecision patterns, we don't check for close vs. open
                outcome, day = check_movement(i, expectation, df)
                percentage_movement = None
                if outcome != 'False' and day is not None:
                    percentage_movement = ((float(df['Close'][i + day]) - float(df['Close'][i])) / float(df['Close'][i])) * 100
                # Use the correct Pair value from the current row
                detected_patterns.append([
                    df['Date'][i],
                    df['Pair'][i],
                    pattern_name,
                    expectation,
                    outcome,
                    percentage_movement
                ])

    # Convert the list to a DataFrame
    patterns_df = pd.DataFrame(
        detected_patterns,
        columns=['Date', 'Pair', 'Pattern', 'Signal', 'Outcome', 'Percentage Movement']
    )
    return patterns_df


def main():
    # Load data from CSV
    file_path = "Crypto_Data.csv"
    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])  # Ensure the Date column is in datetime format
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Analyze the data
    analyzed_df = analyze_data(df)

    # Save the analyzed data to a CSV file
    output_file = "Analyzed_Data.csv"
    analyzed_df.to_csv(output_file, index=False)
    print(f"Analysis complete. Results saved to {output_file}.")

if __name__ == "__main__":
    main()
