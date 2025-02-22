import geodatasets
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt 

# Load the EMDAT Excel file
file_path = "../data/gpkgData/public_emdat_incl_hist_2025-02-22.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Isolating each disaster
floods_df = df[df["Disaster Type"] == "Flood"].dropna(subset=["Latitude", "Longitude"])
storms_df = df[df["Disaster Type"] == "Storm"].dropna(subset=["Latitude", "Longitude"])
earthquakes_df = df[df["Disaster Type"] == "Earthquake"].dropna(subset=["Latitude", "Longitude"])
# extreme_temp_df = df[df["Disaster Type"] == "Extreme temperature"].dropna(subset=["Latitude", "Longitude"])
volcanos_df = df[df["Disaster Type"] == "Volcanic activity"].dropna(subset=["Latitude", "Longitude"])
# drought_df = df[df["Disaster Type"] == "Drought"].dropna(subset=["Latitude", "Longitude"])

# Convert each to a GeoDataFrame
floods_gdf = gpd.GeoDataFrame(floods_df, geometry=gpd.points_from_xy(floods_df.Longitude, floods_df.Latitude), crs="EPSG:4326")
storms_gdf = gpd.GeoDataFrame(storms_df, geometry=gpd.points_from_xy(storms_df.Longitude, storms_df.Latitude), crs="EPSG:4326")
earthquakes_gdf = gpd.GeoDataFrame(earthquakes_df, geometry=gpd.points_from_xy(earthquakes_df.Longitude, earthquakes_df.Latitude), crs="EPSG:4326")
# extreme_temp_df = gpd.GeoDataFrame(extreme_temp_df, geometry=gpd.points_from_xy(extreme_temp_df.Longitude, extreme_temp_df.Latitude), crs="EPSG:4326")
volcanos_df = gpd.GeoDataFrame(volcanos_df, geometry=gpd.points_from_xy(volcanos_df.Longitude, volcanos_df.Latitude), crs="EPSG:4326")
# drought_df = gpd.GeoDataFrame(drought_df, geometry=gpd.points_from_xy(drought_df.Longitude, drought_df.Latitude), crs="EPSG:4326")


# Load world map
world = gpd.read_file(geodatasets.get_path("naturalearth.land"))

# Plot the world map
fig, ax = plt.subplots(figsize=(12, 8))
world.plot(ax=ax, color="#93E9BE", edgecolor="white")

# Plot disasters using GeoDataFrames, not DataFrames**
floods_gdf.plot(ax=ax, color="#1e56ff", markersize=10, alpha=0.6, label="Floods")
storms_gdf.plot(ax=ax, color="#708090", markersize=10, alpha=0.6, label="Storms")
earthquakes_gdf.plot(ax=ax, color="#D2691E", markersize=10, alpha=0.6, label="Earthquakes")
# extreme_temp_df.plot(ax=ax, color="#FF0000", markersize=10, alpha=0.6, label="Extreme Temperatures")
volcanos_df.plot(ax=ax, color="#FC4508", markersize=10, alpha=0.6, label="Volcanoes")
# drought_df.plot(ax=ax, color="#DAA520", markersize=10, alpha=0.6, label="Droughts")


# Add title and legend
plt.title("Disaster Locations from EMDAT")
plt.legend()

# Show the final plot
plt.show()
