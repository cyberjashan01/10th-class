import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Generate synthetic data
np.random.seed(42)  # For reproducibility
X = 4 * np.random.rand(50, 1)  # 100 random points in range [0, 2]
y = 4 + 3 * X + np.random.randn(50, 1)  # Linear relation with noise

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = model.predict(X_test)

# Step 5: Plot the results
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.legend()
plt.show()

# Step 6: Evaluate the model
r_squared = model.score(X_test, y_test)
print(f"R^2 Score: {r_squared:.2f}")
