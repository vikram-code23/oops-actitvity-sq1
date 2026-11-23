 
# ML-Based Addition Calculator

import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Training Dataset
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [10, 20],
    [20, 30],
    [50, 60],
    [100, 200],
    [200, 300]
])

y = np.array([3, 5, 7, 9, 11, 30, 50, 110, 300, 500])

# 2. Create ML Model
model = LinearRegression()

# 3. Train the Model
model.fit(X, y)

# 4. Get User Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 5. Predict Result
new_input = np.array([[num1, num2]])
prediction = model.predict(new_input)

# 6. Display Result
print("ML Predicted Result:", round(prediction[0], 2))
