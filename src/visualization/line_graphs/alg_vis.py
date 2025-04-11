import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "../../data/generated_data/predictions.csv"
df = pd.read_csv(file_path)

# Group data by year and disaster type, then sum the total deaths
grouped_data = df.groupby(['Start Year', 'Disaster Type'])['Total Deaths'].sum().reset_index()

# Pivot the data to get years as rows and disaster types as columns
pivot_data = grouped_data.pivot(index='Start Year', columns='Disaster Type', values='Total Deaths')

# Plot the line graph
plt.figure(figsize=(10, 6))

# Plot each disaster type line
for disaster in pivot_data.columns:
    plt.plot(pivot_data.index, pivot_data[disaster], label=disaster)

# Customize the graph
plt.title('Total Deaths by Disaster Type (Algorithms Prediction)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Deaths', fontsize=12)
plt.legend(title='Disaster Type', loc='upper left')
plt.grid(True)

# Save the plot as a PNG file
output_path = "../outputs/total_deaths_by_disaster.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# Display the plot
plt.tight_layout()
plt.show()

print(f"Graph saved as {output_path}")
