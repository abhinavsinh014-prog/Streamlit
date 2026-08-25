import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

np.random.seed(42)
n_samples = 2000

sqft = np.random.normal(1800, 700, n_samples).clip(400, 6000)
bedrooms = np.random.randint(1, 6, n_samples)
bathrooms = np.random.randint(1, 4, n_samples) + np.random.choice([0, 0.5], n_samples)
age = np.random.uniform(0, 80, n_samples)
distance_to_city = np.random.uniform(0.5, 40, n_samples)
crime_rate = np.random.exponential(3, n_samples).clip(0, 25)
school_rating = np.random.uniform(1, 10, n_samples)

price = (
    50000
    + 180 * sqft
    + 8000 * bedrooms
    + 12000 * bathrooms
    - 800 * age
    - 1500 * distance_to_city
    - 2000 * crime_rate
    + 9000 * school_rating
    + np.random.normal(0, 25000, n_samples)
).clip(50000, None)

df = pd.DataFrame({
    "sqft": sqft,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "age_years": age,
    "distance_to_city_miles": distance_to_city,
    "crime_rate": crime_rate,
    "school_rating": school_rating,
    "price": price
})
print("Dataset shape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nFirst 5 rows:\n", df.head())
print("\nSummary statistics:\n", df.describe())

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=120)
plt.close()

plt.figure(figsize=(7, 5))
plt.scatter(df["sqft"], df["price"], alpha=0.2, s=10)
plt.xlabel("Square Footage")
plt.ylabel("House Price (USD)")
plt.title("Square Footage vs House Price")
plt.tight_layout()
plt.savefig("income_vs_price.png", dpi=120)
plt.close()

X = df.drop(columns=["price"])
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

print("\nModel Intercept:", round(model.intercept_, 3))
coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", key=abs, ascending=False)
print("\nFeature Coefficients (standardized):\n", coef_df)

y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMSE:  {mse:,.2f}")
print(f"RMSE: ${rmse:,.0f}  (typical prediction error in dollars)")
print(f"MAE:  ${mae:,.0f}")
print(f"R2:   {r2:.4f}")

plt.figure(figsize=(7, 6))
plt.scatter(y_test, y_pred, alpha=0.3, s=12)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', linewidth=2, label="Perfect prediction")
plt.xlabel("Actual House Price (USD)")
plt.ylabel("Predicted House Price (USD)")
plt.title("Actual vs Predicted House Values")
plt.legend()
plt.tight_layout()
plt.savefig("actual_vs_predicted.png", dpi=120)
plt.close()

residuals = y_test - y_pred
plt.figure(figsize=(7, 5))
plt.scatter(y_pred, residuals, alpha=0.3, s=12)
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
plt.xlabel("Predicted House Price (USD)")
plt.ylabel("Residual (Actual - Predicted)")
plt.title("Residual Plot")
plt.tight_layout()
plt.savefig("residual_plot.png", dpi=120)
plt.close()

print("\nAll plots saved.")


st.title("House prediction")
sqft = st.number_input("Square feet")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
age_years = st.number_input("age")
distance_to_city = st.number_input("distance_to_city")
crime_rate = st.number_input("Crime rate")
school_rating = st.number_input("School rating (1-10)")

print("\nEnter details for the house you want to price:")
new_house = {
    "sqft": sqft,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "age_years": age_years,
    "distance_to_city_miles": distance_to_city,
    "crime_rate": crime_rate,
    "school_rating": school_rating
}

new_house_df = pd.DataFrame({k: [v] for k, v in new_house.items()})

new_house_df = new_house_df[X.columns]
new_house_scaled = scaler.transform(new_house_df)
predicted_price = model.predict(new_house_scaled)[0]

print("\n--- New House Prediction ---")
for feature, value in new_house.items():
    print(f"{feature}: {value}")
if predicted_price:
    st.write(f"Predicted Price: ${predicted_price:,.0f}")