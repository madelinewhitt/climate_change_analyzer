import geodatasets
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import os

# Load the EMDAT Excel file
file_path = "../../data/gpkgData/public_emdat_incl_hist_2025-02-22.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Ensure output folder exists for volcanic activity
output_dir_volcanic = "../outputs/volcanic_maps"
os.makedirs(output_dir_volcanic, exist_ok=True)

# Get year range
start_year = df["Start Year"].min()
end_year = df["Start Year"].max()

# Load world map once
world = gpd.read_file(geodatasets.get_path("naturalearth.land"))

# Define fixed map boundaries (adjust as necessary)
xmin, ymin, xmax, ymax = -180, -90, 180, 90  # Global bounds

# Loop through each year and plot volcanic activity
for year in range(start_year, end_year + 1):
    volcanic_df = df[
        (df["Disaster Type"] == "Volcanic activity") &
        (df["Start Year"] == year)
    ].dropna(subset=["Latitude", "Longitude"])

    # Check the number of volcanic incidents for this year
    print(f"Year: {year}, Volcanic Data Size: {volcanic_df.shape}")

    # If there are any volcanic incidents for the year, process them
    if not volcanic_df.empty:
        volcanic_gdf = gpd.GeoDataFrame(
            volcanic_df,
            geometry=gpd.points_from_xy(volcanic_df.Longitude, volcanic_df.Latitude),
            crs="EPSG:4326"
        )
    else:
        # If no volcanic incidents for the year, create an empty GeoDataFrame
        volcanic_gdf = gpd.GeoDataFrame(
            columns=["Latitude", "Longitude", "Disaster Type", "Start Year", "geometry"],
            crs="EPSG:4326"
        )

    # Plot and save
    fig, ax = plt.subplots(figsize=(12, 8))
    world.plot(ax=ax, color="#93E9BE", edgecolor="white")

    if not volcanic_gdf.empty:
        volcanic_gdf.plot(ax=ax, color="#FC4508", markersize=10, alpha=0.6, label=f"Volcanoes ({year})")

    # Set fixed axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Maintain the aspect ratio
    ax.set_aspect('equal', adjustable='box')

    plt.title(f"Volcanic Activity Locations from EMDAT - {year}")
    plt.legend()

    # Save the figure for this year
    output_path = os.path.join(output_dir_volcanic, f"volcanics_{year}.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory

    print(f"Saved: {output_path}")
