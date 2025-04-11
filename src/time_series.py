import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from scipy.stats import zscore
from data_processor import load_disaster

"""
Performs the Augmented Dickey-Fuller test for stationarity.
If the series is constant the test is skipped.
Otherwise, the ADF test is applied.
"""
def adf_test(series):
    if len(series.unique()) == 1:
        print("Series is constant. Skipping ADF test.")
        return None, None
    result = adfuller(series)
    return result[0], result[1]

"""
Detects anomalies in the specified column of a DataFrame using the Z-score method.
Values with a Z-score greater than 4 are considered anomalies.
"""
def detect_anomalies_zscore(df, column, threshold=4):
    z_scores = zscore(df[column].fillna(0))
    return df[np.abs(z_scores) > threshold]

"""
Detects anomalies using the Interquartile Range (IQR) method.
Data points outside the defined range based on Q1, Q3, and IQR are flagged as anomalies.
"""
def detect_anomalies_iqr(df, column, multiplier=4):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[
        (df[column] < (Q1 - multiplier * IQR)) |
        (df[column] > (Q3 + multiplier * IQR))
    ]

"""
This function detects anomalies in a given dataframe using a specified anomaly detection method.
It ensures that the detected anomalies are copied to prevent unintended modifications to the original dataframe 
slice. Additionally, it retains the 'Disaster Type' for each anomaly by mapping it from the original dataframe.
"""
def detect_and_label_anomalies(df, method, column, **kwargs):
    anomalies = method(df, column, **kwargs)
    anomalies = anomalies.copy()  # Ensure anomalies is a copy to avoid modifying the original slice
    anomalies['Disaster Type'] = df.loc[anomalies.index, 'Disaster Type'].values  # Add disaster type to anomalies
    return anomalies

"""
Detect anomalies for a given dataset and save to CSV Combines anomalies detected 
from original and predicted datasets.
"""
def detect_anomalies_for_dataset(original_df, predicted_df, output_path):
    anomalies_zscore_original = detect_and_label_anomalies(original_df, detect_anomalies_zscore, 'Total Deaths')
    anomalies_iqr_original = detect_and_label_anomalies(original_df, detect_anomalies_iqr, 'Total Deaths')

    anomalies_zscore_predicted = detect_and_label_anomalies(predicted_df, detect_anomalies_zscore, 'Total Deaths')
    anomalies_iqr_predicted = detect_and_label_anomalies(predicted_df, detect_anomalies_iqr, 'Total Deaths')

    all_anomalies = pd.concat([
        anomalies_zscore_original,
        anomalies_iqr_original,
        anomalies_zscore_predicted,
        anomalies_iqr_predicted
    ]).drop_duplicates()

    all_anomalies.to_csv(output_path, index=False)

if __name__ == "__main__":
    algorithms_path = "../data/generated_data/predictions.csv"
    multialgorithms_path = "../data/generated_data/multipredictions.csv"
    
    disaster_types = [
        "Earthquake", "Flood", "Storm", "Drought", "Air", "Volcanic activity", "Wildfire"
    ]

    all_original = []
    all_algorithms = []
    all_multialgorithms = []

    algorithms_df = pd.read_csv(algorithms_path)
    multialgorithms_df = pd.read_csv(multialgorithms_path)

    for disaster_type in disaster_types:
        original_df = load_disaster(
            disaster_type,
            ["Disaster Type", "Start Year", "Start Month", "Latitude", "Longitude", "Total Deaths"]
        )
        all_original.append(original_df)
        all_algorithms.append(algorithms_df)
        all_multialgorithms.append(multialgorithms_df)

    combined_original_df = pd.concat(all_original, ignore_index=True)
    combined_algorithms_df = pd.concat(all_algorithms, ignore_index=True)
    combined_multialgorithms_df = pd.concat(all_multialgorithms, ignore_index=True)

    for df in [combined_original_df, combined_algorithms_df, combined_multialgorithms_df]:
        if "Start Year" not in df or "Total Deaths" not in df:
            raise ValueError("Datasets must contain 'Start Year' and 'Total Deaths' columns.")

    # Perform stationarity test (using ADF test)
    adf_stat, p_value = adf_test(combined_original_df['Total Deaths'])
    if p_value is not None:
        print(f"ADF Statistic: {adf_stat}")
        print(f"p-value: {p_value}")
        print("The time series is likely", "non-stationary." if p_value > 0.05 else "stationary.")

    # Generate two separate CSV files
    detect_anomalies_for_dataset(combined_original_df, combined_algorithms_df, '../data/generated_data/anomalies_algorithms.csv')
    detect_anomalies_for_dataset(combined_original_df, combined_multialgorithms_df, '../data/generated_data/anomalies_multialgorithms.csv')
