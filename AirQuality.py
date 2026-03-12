from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Loading the dataset
df = pd.read_csv("/Users/dbuana/Desktop/firstprogram/ispu_dki_all.csv")
print(df.head())

# Pre-processing and data cleaning
if isnull := df.isnull().values.any():
    print(df.dropna().isnull().sum())
    df = df.dropna()

# Feature selection
X = df[["pm10", "so2", "co", "o3", "no2"]]
y = df["max"]

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training Samples: {len(X_train)} \n Testing Samples: {len(X)}")

# Linear Regression Model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred = linear_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Random Forest Regressor Model - A more accurate model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
pearson_corr = np.corrcoef(y_test, y_pred_rf)[0, 1]
print(f"Random Forest Pearson Correlation: {pearson_corr:.2f}")

print(f"Random Forest Mean Squared Error: {mse_rf:.2f}")
print(f"random Forest R^2 Score: {r2_rf:.2f}")

unhealthy_air = df[df["categori"] == "Tidak Sehat"]
unhealthy_features = unhealthy_air[["pm10", "so2", "co", "o3", "no2"]].dropna()

if unhealthy_features.shape[0] > 0:
    unhealthy_pred = rf_model.predict(unhealthy_features)
    df_filtered = unhealthy_air.loc[unhealthy_features.index].copy()
    df_filtered["predicted_max"] = unhealthy_pred
    print(f"df_filtered shape: {df_filtered.shape}")
    print(df_filtered[["max", "predicted_max"]].head())
else:
    print("No unhealthy air quality data available.")
    df_filtered = pd.DataFrame()

# Plotting Random Forest Results
sns.scatterplot(x=y_test, y=y_pred_rf, color="Red", label="Random Forest Predictions")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color="black", linewidth=2, label="Ideal Fit")

if not df_filtered.empty:
    plt.scatter(df_filtered["max"], df_filtered["predicted_max"], alpha=0.7, color="green", label="Unhealthy Air Predictions")
    plt.xlabel("Actual Max Values")
    plt.ylabel("Predicted Max Values")
    plt.title("Random Forest Regression on the Unhelathy Level of Air Quality of DKI Jakarta")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    pass

plt.xlabel("Actual Max Values")
plt.ylabel("Predicted Max Values")
plt.title("Random Forest Regression on Air Quality of DKI Jakarta")
plt.legend()
plt.grid(True)
plt.show()

# Time Series Implementation
df_time = pd.read_csv("/Users/dbuana/Desktop/firstprogram/ispu_dki_all.csv", parse_dates=["tanggal"])
df_time = df_time.sort_values(by="tanggal")
df_time = df_time.set_index("tanggal")

X_time = df_time[["pm10", "so2", "co", "o3", "no2"]]
y_time = df_time["max"]

split_index = int(len(df_time) * 0.8)
X_train_time, X_test_time = X_time.iloc[:split_index], X_time.iloc[split_index:]
y_train_time, y_test_time = y_time.iloc[:split_index], y_time.iloc[split_index:]

rf_model.fit(X_train_time, y_train_time)
y_pred_time = rf_model.predict(X_test_time)

sns.scatterplot(x = y_test_time, y = y_pred_time, color="blue", label="Time Series Random Forest Predictions")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color="black", linewidth=2, label="Ideal Fit")
plt.xlabel("Max Values")
plt.ylabel("Predicted Max Values")
plt.title("Time Series Random Forest Regression on Air Quality of DKI Jakarta")
plt.legend()
plt.grid(True)
plt.show()
