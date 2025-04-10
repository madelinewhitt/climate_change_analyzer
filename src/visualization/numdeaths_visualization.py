import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os
from shapely.geometry import Point

# Load the CSV file
file_path = "../../data/NaturalDisastersEmDat1900-2025.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Ensure output folder exists for the death maps
output_dir_deaths = "../outputs/death_maps"
os.makedirs(output_dir_deaths, exist_ok=True)

# Get year range
start_year = df["Start Year"].min()
end_year = df["Start Year"].max()

# Load world map from the downloaded shapefile
world = gpd.read_file("../../countries_geopandas/ne_110m_admin_0_countries.shp")

# Define fixed map boundaries (adjust as necessary)
xmin, ymin, xmax, ymax = -180, -90, 180, 90  # Global bounds

# Define a fixed marker size and transparency
marker_size = 30
alpha = 0.7

# Fixed color map for the legend
cmap = "plasma"

# Set a fixed color normalization for the scale key
vmin, vmax = 1, 200000  # Fixed scale for all images

# Loop through each year
for year in range(start_year, end_year + 1):
    # Create a new figure for each year
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the world map once (same size and scale for all years)
    world.plot(ax=ax, color="#93E9BE", edgecolor="white")

    # Filter data for the year and disasters with deaths recorded
    disasters_df = df[
        (df["Start Year"] == year) & 
        (df["Total Deaths"].notna()) &  # Ensure that 'Total Deaths' is not NaN
        (df["Latitude"].notna()) &  # Ensure that latitude is not NaN
        (df["Longitude"].notna())  # Ensure that longitude is not NaN
    ]

    # Create a GeoDataFrame with the latitude and longitude of the disasters
    if not disasters_df.empty:
        disasters_gdf = gpd.GeoDataFrame(
            disasters_df,
            geometry=gpd.points_from_xy(disasters_df.Longitude, disasters_df.Latitude),
            crs="EPSG:4326"
        )

        # Plot with color intensity based on the number of deaths using the chosen colormap
        disasters_gdf.plot(
            ax=ax,
            column="Total Deaths",
            cmap=cmap,  # Higher contrast color map
            markersize=marker_size,
            alpha=alpha,
            legend=False,  # We will add the legend manually at the end
            vmin=vmin,  # Set the fixed minimum for the color scale
            vmax=vmax   # Set the fixed maximum for the color scale
        )

    # Plot the legend at the bottom for each image
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm.set_array([])

    # Adjust the color bar size and position
    cbar = fig.colorbar(sm, ax=ax, orientation='horizontal', fraction=0.04, pad=0.05, label="Number of Deaths")

    # Increase the font size of the color bar labels
    cbar.ax.tick_params(labelsize=14)  # Adjust the label size
    cbar.set_ticks([1, 50000, 100000, 150000, 200000])  # Optional: define specific ticks for clarity

    # Set the axis limits and aspect ratio to keep them constant
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect('equal', adjustable='box')

    plt.title(f"Disaster Death Locations from EMDAT - {year}")
    
    # Save the plot for the current year
    output_path = os.path.join(output_dir_deaths, f"deaths_{year}.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory

    print(f"Saved: {output_path}")
