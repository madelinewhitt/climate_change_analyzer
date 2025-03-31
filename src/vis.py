import matplotlib.pyplot as plt
import pandas as pd
from pred import future_df

earthquakesOnlyFP = "../data/earthquakesOnlyFP.csv"
df = pd.read_csv(earthquakesOnlyFP)

plt.scatter(
    future_df["Longitude"],
    future_df["Latitude"],
    c=future_df["Predicted Magnitude"],
    cmap="coolwarm",
    alpha=0.5,
)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Predicted Earthquake Magnitudes (Next 10 Years)")
plt.colorbar(label="Predicted Magnitude")
plt.show()
