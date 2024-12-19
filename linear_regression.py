import numpy as np

x = np.array([2,3,5,7,9])
y = np.array([4.2,3.2,5.3,11.3,13.6])

x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y- y_mean))
denominator = np.sum((x - x_mean) ** 2)
slope = numerator/denominator
intercept = y_mean - slope * x_mean
print(f"Equation: y = {intercept:.2f}+{slope:.2f}x")

advertising_spend =6
predicted_sales = intercept + slope * advertising_spend
print(f"Predicted sales for $6 adverstisng spend: {predicted_sales:.2f}")
