import numpy as np
import pandas as pd
from prep import model


earthquakesOnlyFP = "../data/earthquakesOnlyFP.csv"
df = pd.read_csv(earthquakesOnlyFP)

future_years = np.arange(2025, 2035)
future_months = np.tile(np.arange(1, 13), len(future_years))


future_latitudes = np.random.uniform(df['Latitude'].min(), df['Latitude'].max(), len(future_years) * 12)
future_longitudes = np.random.uniform(df['Longitude'].min(), df['Longitude'].max(), len(future_years) * 12)


future_df = pd.DataFrame({
    'Start Year': np.repeat(future_years, 12),
    'Start Month': future_months,
    'Latitude': future_latitudes,
    'Longitude': future_longitudes
})



future_df['Predicted Magnitude'] = model.predict(future_df)
print(future_df['Start Year'].value_counts())


print(future_df.head())
