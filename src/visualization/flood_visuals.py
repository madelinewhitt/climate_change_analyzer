import geodatasets
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import os

# Load the EMDAT Excel file
file_path = "../../data/gpkgData/public_emdat_incl_hist_2025-02-22.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Ensure output folder exists
output_dir_flood = "../outputs/flood_maps"
os.makedirs(output_dir_flood, exist_ok=True)

# Get year range
start_year = df["Start Year"].min()
end_year = df["Start Year"].max()

# Load world map once
world = gpd.read_file(geodatasets.get_path("naturalearth.land"))

# Define fixed map boundaries (adjust as necessary)
xmin, ymin, xmax, ymax = -180, -90, 180, 90  # Global bounds

for year in range(start_year, end_year + 1):
    floods_df = df[
        (df["Disaster Type"] == "Flood") &
        (df["Start Year"] == year)
    ].dropna(subset=["Latitude", "Longitude"])

    # Create GeoDataFrame with or without flood data
    if not floods_df.empty:
        floods_gdf = gpd.GeoDataFrame(
            floods_df,
            geometry=gpd.points_from_xy(floods_df.Longitude, floods_df.Latitude),
            crs="EPSG:4326"
        )
    else:
        # If no floods, create an empty GeoDataFrame with the same CRS
        floods_gdf = gpd.GeoDataFrame(
            columns=["Latitude", "Longitude", "Disaster Type", "Start Year", "geometry"],
            crs="EPSG:4326"
        )

    # Plot and save
    fig, ax = plt.subplots(figsize=(12, 8))
    world.plot(ax=ax, color="#93E9BE", edgecolor="white")

    if not floods_gdf.empty:
        floods_gdf.plot(ax=ax, color="#1E90FF", markersize=10, alpha=0.6, label=f"Floods ({year})")

    # Set fixed axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Maintain the aspect ratio
    ax.set_aspect('equal', adjustable='box')

    plt.title(f"Flood Locations from EMDAT - {year}")
    plt.legend()

    output_path = os.path.join(output_dir_flood, f"floods_{year}.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory

    print(f"Saved: {output_path}")
