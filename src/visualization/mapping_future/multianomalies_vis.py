import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os
from shapely.geometry import Point
import numpy as np

# Load the CSV file
file_path = "../../../data/generated_data/anomalies_multialgorithms.csv"
df = pd.read_csv(file_path)

# Ensure output folder exists for the death maps
output_dir_deaths = "../outputs/death_maps"
os.makedirs(output_dir_deaths, exist_ok=True)

# Define fixed map boundaries (adjust as necessary)
xmin, ymin, xmax, ymax = -180, -90, 180, 90  # Global bounds

# Set marker size scaling factor and transparency
alpha = 0.7
size_factor = 0.5  # Increase this factor to make the markers larger

# Define a color map for different disaster types
disaster_colors = {
    'Earthquake': 'red',
    'Flood': 'blue',
    'Storm': 'green',
    'Drought': 'orange',
    'Volcanic activity': 'purple'
}

# Load world map from the downloaded shapefile
world = gpd.read_file("../../../countries_geopandas/ne_110m_admin_0_countries.shp")

# Loop through each year from 1900 to 2034
for year in range(1900, 2035):
    # Create a new figure for each year
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the world map once (same size and scale for all years)
    world.plot(ax=ax, color="#93E9BE", edgecolor="white")

    # Filter data for the current year and disasters with deaths recorded
    disasters_df = df[
        (df["Start Year"] == year) & 
        (df["Total Deaths"].notna()) &  # Ensure that 'Total Deaths' is not NaN
        (df["Latitude"].notna()) &  # Ensure that latitude is not NaN
        (df["Longitude"].notna())  # Ensure that longitude is not NaN
    ]

    # If there is data for the current year, plot the disaster data
    if not disasters_df.empty:
        # Create a GeoDataFrame with the latitude and longitude of the disasters
        disasters_gdf = gpd.GeoDataFrame(
            disasters_df,
            geometry=gpd.points_from_xy(disasters_df.Longitude, disasters_df.Latitude),
            crs="EPSG:4326"
        )

        # Loop over each disaster type to plot with different colors and sizes
        for disaster_type, color in disaster_colors.items():
            type_df = disasters_gdf[disasters_gdf["Disaster Type"] == disaster_type]
            
            if not type_df.empty:
                # Scale marker size based on the number of deaths
                marker_size = np.sqrt(type_df["Total Deaths"]) * size_factor
                
                # Plot each disaster type with different color and size
                type_df.plot(
                    ax=ax,
                    color=color,  # Specify color based on disaster type
                    markersize=marker_size,
                    alpha=alpha,
                    legend=False,  # Legend will be handled later
                )

    # Plot the legend manually at the bottom
    sm = plt.cm.ScalarMappable(cmap="plasma", norm=plt.Normalize(vmin=1, vmax=200000))
    sm.set_array([])

    # Set the axis limits and aspect ratio to keep them constant
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect('equal', adjustable='box')

    # Set the title for the plot
    plt.title(f"Disaster Death Locations from Anomalies (Multi-algorithms) - {year}")

    # Save the plot for the current year
    output_path = os.path.join(output_dir_deaths, f"deaths_{year}.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory

    print(f"Saved: {output_path}")
