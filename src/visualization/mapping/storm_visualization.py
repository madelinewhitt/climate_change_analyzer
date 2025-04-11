import geodatasets
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import os

# Load the EMDAT Excel file
file_path = "../../data/gpkgData/public_emdat_incl_hist_2025-02-22.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Ensure output folder exists for storms
output_dir_storm = "../outputs/storm_maps"
os.makedirs(output_dir_storm, exist_ok=True)

# Get year range
start_year = df["Start Year"].min()
end_year = df["Start Year"].max()

# Load world map once
world = gpd.read_file(geodatasets.get_path("naturalearth.land"))

# Define fixed map boundaries (adjust as necessary)
xmin, ymin, xmax, ymax = -180, -90, 180, 90  # Global bounds

for year in range(start_year, end_year + 1):
    storms_df = df[
        (df["Disaster Type"] == "Storm") &
        (df["Start Year"] == year)
    ].dropna(subset=["Latitude", "Longitude"])

    # Create GeoDataFrame with or without storm data
    if not storms_df.empty:
        storms_gdf = gpd.GeoDataFrame(
            storms_df,
            geometry=gpd.points_from_xy(storms_df.Longitude, storms_df.Latitude),
            crs="EPSG:4326"
        )
    else:
        # If no storms, create an empty GeoDataFrame with the same CRS
        storms_gdf = gpd.GeoDataFrame(
            columns=["Latitude", "Longitude", "Disaster Type", "Start Year", "geometry"],
            crs="EPSG:4326"
        )

    # Plot and save
    fig, ax = plt.subplots(figsize=(12, 8))
    world.plot(ax=ax, color="#93E9BE", edgecolor="white")

    if not storms_gdf.empty:
        storms_gdf.plot(ax=ax, color="#FFD700", markersize=10, alpha=0.6, label=f"Storms ({year})")

    # Set fixed axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Maintain the aspect ratio
    ax.set_aspect('equal', adjustable='box')

    plt.title(f"Storm Locations from EMDAT - {year}")
    plt.legend()

    output_path = os.path.join(output_dir_storm, f"storms_{year}.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory

    print(f"Saved: {output_path}")
