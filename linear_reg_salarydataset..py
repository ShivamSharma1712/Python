import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv(r"C:\Users\hp\Downloads\Salary_Data.csv")

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Print column names to check for mismatches
print("\nColumn Names in Dataset:")
print(df.columns)

# Check for missing values
print("\nDataset Info:")
print(df.info())

# Selecting relevant columns (ensure correct column name)
df = df[['YearsExperience', 'Salary']]

# Splitting features and target variable
X = df[['YearsExperience']]  # Independent variable
y = df['Salary']  # Dependent variable

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print("\nModel Evaluation:")
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# Visualizing the Regression Line with Training Data
plt.figure(figsize=(8, 5))
plt.scatter(X_train, y_train, color="blue", label="Actual Salary (Training Data)")
plt.plot(X_train, model.predict(X_train), color='red', label="Regression Line")

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression Model on Training Data")
plt.legend()
plt.show()

# Visualizing the Regression Line with Test Data
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color="green", label="Actual Salary (Test Data)")
plt.plot(X_test, y_pred, color='red', label="Regression Line")

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression Model on Test Data")
plt.legend()
plt.show()
