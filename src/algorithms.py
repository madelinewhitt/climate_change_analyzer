from data_processor import load_disaster
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
This file contains the training, and prediction for the single model algorithm
It outputs the resulting files to /data/predictions.csv
"""


def prep(df):
    """
    1) Drops rows and columns with invalid values
    2) Splits training and testing data: 80% and 20% respectively
    3) Sets the rng split seed at 42 for consistency
    4) Sets up 400 decision trees with a learning rate of 0.03
    5) Trains the machine learning algorithm for "Total Deaths"
    6) Mean squared error is produced after testing
    """

    df = df.dropna(axis=1, how="all")
    features = ["Start Year", "Start Month", "Latitude", "Longitude"]
    target = "Total Deaths"

    df = df.dropna(subset=["Total Deaths"])
    df = df[~df["Total Deaths"].isin([np.inf, -np.inf])]
    df["Total Deaths"] = np.clip(df["Total Deaths"], 0, np.inf)

    #sets the testing data to be 20% "test_size = 0.2"
    #"random_state = 42" ensures the same testing data is used every time

    X_train, X_test, y_train, y_test = train_test_split(
        df[features], df[target], test_size=0.2, random_state=42
    )

    #sets the number of decision trees to be 400 "n_estimators=400"
    #"learning_rate=0.03" indicates the rate at which trees can correct each others'
    #output 
    model = xgb.XGBRegressor(n_estimators=400, learning_rate=0.03)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    return model


def pred(df, model, disType):
    """
    Generates synthetic coordinate data to predict 
    the total deaths during each event at the generated location
    12 events are predicted per year
    """

    future_years = np.arange(2025, 2035)
    future_months = np.tile(np.arange(1, 13), len(future_years))

    future_latitudes = np.random.uniform(
        df["Latitude"].min(), df["Latitude"].max(), len(future_years) * 12
    )
    future_longitudes = np.random.uniform(
        df["Longitude"].min(), df["Longitude"].max(), len(future_years) * 12
    )

    future_latitudes = np.round(future_latitudes, 6)
    future_longitudes = np.round(future_longitudes, 6)

    future_df = pd.DataFrame(
        {
            "Start Year": np.repeat(future_years, 12),
            "Start Month": future_months,
            "Latitude": future_latitudes,
            "Longitude": future_longitudes,
        }
    )
    
    future_df = future_df[["Start Year", "Start Month", "Latitude", "Longitude"]]

    future_df["Total Deaths"] = model.predict(future_df)


    future_df["Total Deaths"] = np.clip(future_df["Total Deaths"], 0, np.inf)

    future_df["Total Deaths"] = future_df["Total Deaths"].astype(int)

    future_df["Disaster Type"] = disType

    print(future_df["Start Year"].value_counts())
    print(future_df.head())

    return future_df



if __name__ == "__main__":

    """
    Runs the single model algorithm for each event
    Outputs the prediction results into predictions.csv
    """
    dfs = []
    csv_filename = f"../data/generated_data/predictions.csv"
    disaster_types = [
        "Earthquake",
        "Flood",
        "Storm",
        "Drought",
        "Volcanic activity",
        "Wildfire",
    ]
    for disType in disaster_types:
        df = load_disaster(
            disType,
            [
                "Disaster Type",
                "Start Year",
                "Start Month",
                "Latitude",
                "Longitude",
                "Total Deaths",
            ],
        )
        print(f"running for {disType}")
        model = prep(df)
        future_df = pred(df, model, disType)
        dfs.append(future_df)

    future_df = pd.concat(dfs, ignore_index=True)
    future_df.to_csv(csv_filename, index=False)
    print(f"Predictions saved to {csv_filename}")
