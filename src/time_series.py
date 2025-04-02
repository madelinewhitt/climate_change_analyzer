import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from scipy.stats import zscore
import matplotlib.pyplot as plt

# Function to perform ADF test (checks for stationarity by testing for unit root)
def adf_test(series):
    result = adfuller(series)
    return result[0], result[1]  # ADF Statistic and p-value

# Load data
original_df = pd.read_csv("../data/earthquakesOnlyFP.csv")
predicted_df = pd.read_csv("../data/predicted_earthquakes.csv")

# Ensure necessary columns exist
for df in [original_df, predicted_df]:
    if "Start Year" not in df or "Magnitude" not in df:
        raise ValueError("Datasets must contain 'Start Year' and 'Magnitude' columns.")

# Aggregate magnitude by year
original_magnitude = original_df.groupby("Start Year")["Magnitude"].mean()
predicted_magnitude = predicted_df.groupby("Start Year")["Magnitude"].mean()

# Perform ADF test on original data to check stationarity
adf_stat, adf_p = adf_test(original_magnitude)

# Check if original data is stationary
is_stationary_original = adf_p < 0.05  # ADF: Rejecting null means stationary

# If original data is non-stationary, apply differencing
if not is_stationary_original:
    original_diff = original_magnitude.diff().dropna()  # First difference to make it stationary
    adf_stat_diff, adf_p_diff = adf_test(original_diff)  # Re-run ADF test
    is_stationary_diff_original = adf_p_diff < 0.05  # Check if differenced data is stationary

# Perform ADF test on predicted data to check stationarity
adf_stat_predicted, adf_p_predicted = adf_test(predicted_magnitude)

# Check if predicted data is stationary
is_stationary_predicted = adf_p_predicted < 0.05  # ADF: Rejecting null means stationary

# If predicted data is non-stationary, apply differencing
if not is_stationary_predicted:
    predicted_diff = predicted_magnitude.diff().dropna()  # First difference to make it stationary
    adf_stat_diff_predicted, adf_p_diff_predicted = adf_test(predicted_diff)  # Re-run ADF test
    is_stationary_diff_predicted = adf_p_diff_predicted < 0.05  # Check if differenced data is stationary

# Anomaly detection using Z-score for original data
z_scores_original = zscore(original_magnitude.fillna(0))  # Filling NaN with 0 for Z-score calculation
anomalies_zscore_original = original_magnitude[np.abs(z_scores_original) > 2.5]  # Threshold for anomalies

# Anomaly detection using IQR (Interquartile Range) for original data
Q1_original = original_magnitude.quantile(0.25)
Q3_original = original_magnitude.quantile(0.75)
IQR_original = Q3_original - Q1_original
anomalies_iqr_original = original_magnitude[(original_magnitude < (Q1_original - 1.5 * IQR_original)) | (original_magnitude > (Q3_original + 1.5 * IQR_original))]

# Combine anomalies from both methods for original data
all_anomalies_original = pd.concat([anomalies_zscore_original, anomalies_iqr_original]).drop_duplicates()

# Anomaly detection using Z-score for predicted data
z_scores_predicted = zscore(predicted_magnitude.fillna(0))  # Filling NaN with 0 for Z-score calculation
anomalies_zscore_predicted = predicted_magnitude[np.abs(z_scores_predicted) > 2.5]  # Threshold for anomalies

# Anomaly detection using IQR (Interquartile Range) for predicted data
Q1_predicted = predicted_magnitude.quantile(0.25)
Q3_predicted = predicted_magnitude.quantile(0.75)
IQR_predicted = Q3_predicted - Q1_predicted
anomalies_iqr_predicted = predicted_magnitude[(predicted_magnitude < (Q1_predicted - 1.5 * IQR_predicted)) | (predicted_magnitude > (Q3_predicted + 1.5 * IQR_predicted))]

# Combine anomalies from both methods for predicted data
all_anomalies_predicted = pd.concat([anomalies_zscore_predicted, anomalies_iqr_predicted]).drop_duplicates()

# Combine anomalies from original and predicted data
all_anomalies = pd.concat([all_anomalies_original, all_anomalies_predicted]).drop_duplicates()

# Save only anomalies to a CSV file
all_anomalies.to_csv("../data/anomalies.csv", header=["Magnitude"])
