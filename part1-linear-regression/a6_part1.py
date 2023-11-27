import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
plt.figure(figsize=(6,4))
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 


# Print out the linear equation and r squared value

# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction

# Create the model in matplotlib and include the line of best fit
plt.scatter(x,y)
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure By Age")
print(f"Correlation between Age and Blood Pressure: {x.corr(y)}")
plt.show()