# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Creating the dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7],
    'Score': [40, 50, 60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)

# Step 2: Preparing data for training
X = df[['Hours']].values  # Features (2D array)
y = df['Score'].values    # Target variable (1D array)

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"X_train: {X_train}")
print(f"y_train: {y_train}")
print(f"X_test: {X_test}")
print(f"y_test: {y_test}")

# Step 3: Training the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained successfully.")

# Step 4: Making predictions
y_pred = model.predict(X_test)
print(f"y_pred: {y_pred}")

# Step 5: Visualizing the results
plt.scatter(X, y, color='blue', label='Actual Data')  # Scatter plot of original data
plt.plot(X, model.predict(X), color='red', label='Regression Line')  # Regression line
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Hours vs. Score')
plt.legend()
plt.show()

# Step 6: Printing predictions for test data
print("Predicted scores for test data:")
for i in range(len(X_test)):
    print(f"Hours Studied: {X_test[i][0]}, Actual Score: {y_test[i]}, Predicted Score: {y_pred[i]:.2f}")

# Step 7: Predicting for a new value
new_hours = np.array([[7]])  # Example: Predicting for 7 hours of study
predicted_score = model.predict(new_hours)
print(f"Predicted score for 7 hours of study: {predicted_score[0]:.2f}")

# Step 8: Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
