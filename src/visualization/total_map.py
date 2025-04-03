import geodatasets
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# TODO: Understand why there are errors with graphing extreme temp and drought

# Load the EMDAT Excel file
file_path = "../../data/gpkgData/public_emdat_incl_hist_2025-02-22.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Isolating each disaster
floods_df = df[df["Disaster Type"] == "Flood"].dropna(subset=["Latitude", "Longitude"])
storms_df = df[df["Disaster Type"] == "Storm"].dropna(subset=["Latitude", "Longitude"])
earthquakes_df = df[df["Disaster Type"] == "Earthquake"].dropna(
    subset=["Latitude", "Longitude"]
)
volcanos_df = df[df["Disaster Type"] == "Volcanic activity"].dropna(
    subset=["Latitude", "Longitude"]
)

# Convert each to a GeoDataFrame
floods_gdf = gpd.GeoDataFrame(
    floods_df,
    geometry=gpd.points_from_xy(floods_df.Longitude, floods_df.Latitude),
    crs="EPSG:4326",
)
storms_gdf = gpd.GeoDataFrame(
    storms_df,
    geometry=gpd.points_from_xy(storms_df.Longitude, storms_df.Latitude),
    crs="EPSG:4326",
)
earthquakes_gdf = gpd.GeoDataFrame(
    earthquakes_df,
    geometry=gpd.points_from_xy(earthquakes_df.Longitude, earthquakes_df.Latitude),
    crs="EPSG:4326",
)
volcanos_gdf = gpd.GeoDataFrame(
    volcanos_df,
    geometry=gpd.points_from_xy(volcanos_df.Longitude, volcanos_df.Latitude),
    crs="EPSG:4326",
)

# Load world map
world = gpd.read_file(geodatasets.get_path("naturalearth.land"))

# Plot the world map
fig, ax = plt.subplots(figsize=(12, 8))
world.plot(ax=ax, color="#93E9BE", edgecolor="white")

# Plot disasters using GeoDataFrames
if not floods_gdf.empty:
    floods_gdf.plot(ax=ax, color="#1e56ff", markersize=10, alpha=0.6, label="Floods")

if not storms_gdf.empty:
    storms_gdf.plot(ax=ax, color="#708090", markersize=10, alpha=0.6, label="Storms")

if not earthquakes_gdf.empty:
    earthquakes_gdf.plot(
        ax=ax, color="#D2691E", markersize=10, alpha=0.6, label="Earthquakes"
    )

if not volcanos_gdf.empty:
    volcanos_gdf.plot(ax=ax, color="#FC4508", markersize=10, alpha=0.6, label="Volcanoes")

# Add title and legend
plt.title("Disaster Locations from EMDAT")
plt.legend()

# Show the final plot
plt.show()
