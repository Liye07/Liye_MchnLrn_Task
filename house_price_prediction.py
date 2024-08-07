#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error 

np.random.seed(0)
size = np.random.randint(1000, 5000, 100)
price = size * 200 + np.random.normal(0, 10000, 100)

data = pd.DataFrame({'Size (sq ft)': size, 'Price': price})

X = data['Size (sq ft)']
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

print("Displaying the plot...")

plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.scatter(X_test, predictions, color='red', label='Predicted Prices')
plt.plot(X_test, predictions, color='red')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price')
plt.title('House Price Prediction')
plt.legend()
plt.show()
