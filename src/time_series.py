import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from scipy.stats import zscore
from data_processor import load_disaster

def adf_test(series):
    if len(series.unique()) == 1:
        print("Series is constant. Skipping ADF test.")
        return None, None
    result = adfuller(series)
    return result[0], result[1]

def detect_anomalies_zscore(df, column, threshold=3):
    z_scores = zscore(df[column].fillna(0))
    return df[np.abs(z_scores) > threshold]

def detect_anomalies_iqr(df, column, multiplier=3):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[
        (df[column] < (Q1 - multiplier * IQR)) |
        (df[column] > (Q3 + multiplier * IQR))
    ]

def load_and_prepare_data(disaster_type, predicted_data_path):
    original_df = load_disaster(
        disaster_type,
        ["Start Year", "Start Month", "Latitude", "Longitude", "Total Deaths"],
    ).dropna()
    predicted_df = pd.read_csv(predicted_data_path).dropna()
    return original_df, predicted_df

def main():
    disaster_type = "Earthquake"
    predicted_data_path = "../data/predictions.csv"

    original_df, predicted_df = load_and_prepare_data(disaster_type, predicted_data_path)

    for df in [original_df, predicted_df]:
        if "Start Year" not in df or "Total Deaths" not in df:
            raise ValueError("Datasets must contain 'Start Year' and 'Total Deaths' columns.")

    adf_stat, p_value = adf_test(original_df['Total Deaths'])
    if p_value is not None:
        print(f"ADF Statistic: {adf_stat}")
        print(f"p-value: {p_value}")
        if p_value > 0.05:
            print("The time series is likely non-stationary.")
        else:
            print("The time series is likely stationary.")

    anomalies_zscore_original = detect_anomalies_zscore(original_df, 'Total Deaths', threshold=3)
    anomalies_iqr_original = detect_anomalies_iqr(original_df, 'Total Deaths', multiplier=3)
    all_anomalies_original = pd.concat([anomalies_zscore_original, anomalies_iqr_original]).drop_duplicates()
    
    anomalies_zscore_predicted = detect_anomalies_zscore(predicted_df, 'Total Deaths', threshold=4)
    anomalies_iqr_predicted = detect_anomalies_iqr(predicted_df, 'Total Deaths', multiplier=3)
    all_anomalies_predicted = pd.concat([anomalies_zscore_predicted, anomalies_iqr_predicted]).drop_duplicates()

    all_anomalies = pd.concat([all_anomalies_original, all_anomalies_predicted]).drop_duplicates()
    all_anomalies.to_csv('../data/anomalies.csv', index=False)

if __name__ == "__main__":
    main()

