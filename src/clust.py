from data_processor import load_disaster
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def distance_to_line(p, a, b):
    """
    Calculates the shortest perpendicular distance from
    point p to a line defined by two other points a and b. 
    It is used to calculate the distance from the clusters and data
    """
    return np.abs(np.cross(b - a, a - p)) / np.linalg.norm(b - a)


def scale(features):
    """
    Scales the features to be used in the elbow method
    """

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features


def elbow_method(scaled_features):
    """
    Runs the KMeans algorithm 10 times to calculate the ideal number of clusters
    based on inertia 
    """
    inertia = []
    k_range = range(1, 11)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(scaled_features)
        inertia.append(kmeans.inertia_)

    x = np.array(list(k_range))
    y = np.array(inertia)
    point1 = np.array([x[0], y[0]])
    point2 = np.array([x[-1], y[-1]])

    distances = [
        distance_to_line(np.array([x[i], y[i]]), point1, point2) for i in range(len(x))
    ]
    optimal_k = x[np.argmax(distances)]
    return optimal_k, x, y


def final_clustering(optimal_k, df, disaster_type, model):
    """
    Runs the algorithm 10 times with different
    centroid seeds and chooses the best result 
    based on inertia
    """
    kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df["Cluster"] = kmeans_final.fit_predict(scaled_features)
    name = f"../data/generated_data/{model}_clustering_{disaster_type}.csv"
    df.to_csv(name)
    print(f"saved to {name}")



def elbow_curve(optimal_k, x, y, disaster_type,model):
    """
    Graphs the elbow curve to visualize the ideal number
    of clusters based on their inertia values
    image saved to ../data/generated_data/images/
    """
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker="o", label="Inertia")
    plt.axvline(optimal_k, color="r", linestyle="--", label=f"Optimal k = {optimal_k}")
    plt.title(f"Elbow Method for Optimal Clusters for {disaster_type}")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Inertia")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(f"../data/generated_data/images/{model}_elbow_curve_{disaster_type}.png")


def clustered_event(df, disaster_type, model):
    """
    Graphs the cluster map saved to ../data/generated_data/images/name as a png
    """
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

    plt.savefig(f"../data/generated_data/images/{model}_cluster_map_{disaster_type}.png")




if __name__ == "__main__":


    disaster_types = [
        "Earthquake",
        "Flood",
        "Storm",
        "Drought",
        "Volcanic activity",
        "Wildfire",
    ]


    for disasterType in disaster_types:
        model = "multi"
        print(f"running for {disasterType}")
        df = pd.read_csv("../data/generated_data/multipredictions.csv")
        df = df[df["Disaster Type"]==disasterType]
        features = df[["Latitude", "Longitude", "Total Deaths"]]
        scaled_features = scale(features)
        optimal_k, x, y = elbow_method(scaled_features)
        final_clustering(optimal_k, df, model, disasterType)
        elbow_curve(optimal_k, x, y, disasterType,model)
        clustered_event(df, disasterType, model)

    for disasterType in disaster_types:
        model = "single"
        print(f"running for {disasterType}")
        df = pd.read_csv("../data/generated_data/predictions.csv")
        df = df[df["Disaster Type"]==disasterType]
        features = df[["Latitude", "Longitude", "Total Deaths"]]
        scaled_features = scale(features)
        optimal_k, x, y = elbow_method(scaled_features)
        final_clustering(optimal_k, df, model, disasterType)
        elbow_curve(optimal_k, x, y, disasterType,model)
        clustered_event(df, disasterType, model)




    
