from data_processor import load_disaster
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def prep(df):
    df = df.dropna(axis=1, how="all")

    features = ["Start Year", "Start Month", "Latitude", "Longitude"]
    target = "Magnitude"

    df = df.dropna(subset=["Magnitude"])

    df = df[~df["Magnitude"].isin([np.inf, -np.inf])]

    df["Magnitude"] = np.clip(df["Magnitude"], 0, 10)

    X_train, X_test, y_train, y_test = train_test_split(
        df[features], df[target], test_size=0.2, random_state=42
    )

    model = xgb.XGBRegressor(n_estimators=400, learning_rate=0.03)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    return model


def pred(df, model):
    future_years = np.arange(2025, 2035)
    future_months = np.tile(np.arange(1, 13), len(future_years))

    future_latitudes = np.random.uniform(
        df["Latitude"].min(), df["Latitude"].max(), len(future_years) * 12
    )
    future_longitudes = np.random.uniform(
        df["Longitude"].min(), df["Longitude"].max(), len(future_years) * 12
    )

    future_df = pd.DataFrame(
        {
            "Start Year": np.repeat(future_years, 12),
            "Start Month": future_months,
            "Latitude": future_latitudes,
            "Longitude": future_longitudes,
        }
    )

    future_df["Predicted Magnitude"] = model.predict(future_df)

    print(future_df["Start Year"].value_counts())

    print(future_df.head())
    return future_df


def vis(future_df, dis_type):
    plt.scatter(
        future_df["Longitude"],
        future_df["Latitude"],
        c=future_df["Predicted Magnitude"],
        cmap="coolwarm",
        alpha=0.5,
    )
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title(f"Predicted {dis_type} Magnitudes (Next 10 Years)")
    plt.colorbar(label="Predicted Magnitude")
    plt.show()


if __name__ == "__main__":
    disaster_type = "Flood"
    df = load_disaster(
        disaster_type,
        ["Start Year", "Start Month", "Latitude", "Longitude", "Magnitude"],
    )
    print(f"running for {disaster_type}")
    model = prep(df)
    future_df = pred(df, model)
    vis(future_df, disaster_type)
