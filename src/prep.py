import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

#df = pd.read_csv("earthquakesOnlyFP.csv")
earthquakesOnlyFP = "../data/earthquakesOnlyFP.csv"
df = pd.read_csv(earthquakesOnlyFP)

df = df.dropna(axis=1, how='all')

features = ['Start Year', 'Start Month', 'Latitude', 'Longitude']
target = 'Magnitude'

df = df.dropna(subset=['Magnitude'])  

df = df[~df['Magnitude'].isin([np.inf, -np.inf])] 

df['Magnitude'] = np.clip(df['Magnitude'], 0, 10)

X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

model = xgb.XGBRegressor(n_estimators=400, learning_rate=0.03)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print(f'Mean Squared Error: {mse}')



