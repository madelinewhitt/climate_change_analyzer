from src.data_processor import load_disaster
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# from algorithms import future_df, disaster_type

disaster_type = "Earthquake"


def distance_to_line(p, a, b):
    return np.abs(np.cross(b - a, a - p)) / np.linalg.norm(b - a)


def scale(features):

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features


def elbow_method(scaled_features):
    # Scale features

    # Elbow method to determine optimal k
    inertia = []
    k_range = range(1, 11)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(scaled_features)
        inertia.append(kmeans.inertia_)

    # Manual elbow detection (max distance from line)
    x = np.array(list(k_range))
    y = np.array(inertia)
    point1 = np.array([x[0], y[0]])
    point2 = np.array([x[-1], y[-1]])

    distances = [
        distance_to_line(np.array([x[i], y[i]]), point1, point2) for i in range(len(x))
    ]
    optimal_k = x[np.argmax(distances)]
    return optimal_k, x, y


def final_clustering(optimal_k, df):
    kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df["Cluster"] = kmeans_final.fit_predict(scaled_features)


def elbow_curve(optimal_k, x, y):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker="o", label="Inertia")
    plt.axvline(optimal_k, color="r", linestyle="--", label=f"Optimal k = {optimal_k}")
    plt.title(f"Elbow Method for Optimal Clusters for {disaster_type}")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Inertia")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def clustered_event(df):
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        df["Longitude"],
        df["Latitude"],
        c=df["Cluster"],
        s=df["Total Deaths"] / 10,
        alpha=0.7,
        edgecolors="k",
    )
    plt.title(f"{disaster_type} Clusters by Location and Death Impact")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.colorbar(label="Cluster")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def clustered_on_map(df):
    plt.figure(figsize=(14, 7))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_global()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=":")

    # Scatter plot of clustered earthquakes
    scatter = ax.scatter(
        df["Longitude"],
        df["Latitude"],
        c=df["Cluster"],
        s=df["Total Deaths"] / 10,
        cmap="tab10",
        edgecolor="k",
        alpha=0.7,
        transform=ccrs.PlateCarree(),
    )

    plt.title("Clustered Earthquake Predictions on World Map")
    plt.colorbar(scatter, label="Cluster")
    plt.show()


if __name__ == "__main__":

    # df = future_df
    print(f"running for {disaster_type}")
    df = pd.read_csv("../data/multipredictions.csv")

    features = df[["Latitude", "Longitude", "Total Deaths"]]

    scaled_features = scale(features)
    optimal_k, x, y = elbow_method(scaled_features)
    final_clustering(optimal_k, df)
    elbow_curve(optimal_k, x, y)
    clustered_event(df)
    clustered_on_map(df)
