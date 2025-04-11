import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the CSV file
csv_filename = "../../data/multipredictions.csv"  # Replace with your actual file path
df = pd.read_csv(csv_filename)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Start Year'], df['Total Deaths'], color='blue', alpha=0.5, label="Predicted Deaths")
X = df[['Start Year']]
y = df['Total Deaths']
model = LinearRegression()
model.fit(X, y)

# Get the slope and intercept of the trend line
slope = model.coef_[0]
intercept = model.intercept_ 
y_pred = model.predict(X)
plt.plot(df['Start Year'], y_pred, color='red', label="Trend Line", linewidth=2)

plt.xlabel('Year')
plt.ylabel('Total Deaths')
plt.title('Predicted Disaster Deaths by Year with Trend Line')
plt.legend()
slope_text = f"Slope: {slope:.2f}"
plt.text(2025, 4500, slope_text, fontsize=12, color='red', ha='left', va='bottom')

# Save the plot as an image
output_path = "../outputs/multi_alg.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.grid(True)
plt.show()
