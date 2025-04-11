import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_processor import load_disaster

"""
This file contains the training, and prediction for the multi model algorithm
It outputs the resulting files to /data/multipredictions.csv
"""

def prep(df):
    """
    This function creates multiple learning models in attempt to 
    predict the Total Deaths as well as the event location

    1) Drops rows and columns with invalid values (empty, infinite and total deaths > 5000)
    2) Splits training and testing data: 80% and 20% respectively
    3) Sets the rng split seed at 42 for consistency
    4) Sets up 400 decision trees with a learning rate of 0.03
    5) Creates a dictionary of trained ml learning models for each target
    6) Mean squared error is produced after testing each model for each event
    """


    df = df.dropna(axis=1, how="all")    
    features = ["Start Year", "Latitude", "Longitude", "Total Deaths"]
    targets = ["Latitude", "Longitude", "Total Deaths"]

    df = df.dropna(subset=features)
    df = df[~df[features].isin([np.inf, -np.inf]).any(axis=1)]

    #in attempt to lower the variange for total deaths,
    #rows with total deaths over 5000 were dropped 
    df["Total Deaths"] = np.clip(df["Total Deaths"], 0, 5000)

    X_train, X_test = train_test_split(df[features], test_size=0.2, random_state=42)


    #models is a dictionary that contains the learning model for each target
    #this is also the return for this function to be used in the "prep" function
    
    models = {}


    for target in targets:

        y_train = df.loc[X_train.index, target]
        y_test = df.loc[X_test.index, target]
        model = xgb.XGBRegressor(n_estimators=400, learning_rate=0.03)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"MSE for {target}: {mse}")

        models[target] = model

    return models

def pred(df, disType):

    """
    Generates initial synthetic coordinates and death rates for the future years
    The synthetic data is overwritten by the predicted values in the following order:
    Latitude, Longitude, Total Death
    """
    future_years = np.arange(2025, 2035)
    num_samples = len(future_years) * 12

    #the synthetic data used for the future predictions
    future_latitudes = np.random.uniform(-90, 90, num_samples)
    future_longitudes = np.random.uniform(-180, 180, num_samples)
    future_deaths = np.random.uniform(0, 5000, num_samples)

    future_df = pd.DataFrame(
        {
            "Start Year": np.repeat(future_years, 12),
            "Latitude": future_latitudes,
            "Longitude": future_longitudes,
            "Total Deaths": future_deaths,
        }
    )
    
    models = prep(df)
    
    future_df = future_df[["Start Year", "Latitude", "Longitude", "Total Deaths"]]
    
    for target in ["Latitude", "Longitude", "Total Deaths"]:
        input_features = ["Start Year", "Latitude", "Longitude", "Total Deaths"]
        if target in models:
            future_df[f"{target}"] = models[target].predict(future_df[input_features])

    future_df["Disaster Type"] = disType

    future_df["Total Deaths"] = future_df["Total Deaths"].astype(int)

    future_df["Start Year"] = future_df["Start Year"].astype(int)

    future_df = future_df.dropna(subset=input_features)

    return future_df


if __name__ == "__main__":

    """
    Runs the multi model algorithm for each event
    Outputs the prediction results into multipredictions.csv
    """
    dfs = []
    csv_filename = f"../data/generated_data/multipredictions.csv"
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
        future_df = pred(df, disType)

        dfs.append(future_df)

    future_df = pd.concat(dfs, ignore_index=True)
    future_df.to_csv(csv_filename, index=False)
    print(f"Predictions saved to {csv_filename}")
