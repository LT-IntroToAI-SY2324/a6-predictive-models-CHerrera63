import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("final-project/Emplyee-info.csv")
x = data["Typical Hours"].values
y = data["Hourly Rate"].values

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 1)
xtrain = xtrain.reshape(-1,1)

model = LinearRegression().fit(xtrain, ytrain)
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(xtrain, ytrain)

print("Model's Linear Equation: y=",coef, "x+", intercept)
print("R Squared value:", r_squared)

# reshape the xtest data into a 2D array
xtest = xtest.reshape(-1,1)

# get the predicted y values for the xtest values - returns an array of the results
predict = model.predict(xtest)

# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)

# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = predict[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    print("x value:", float(x_coord), "Predicted y value:", predicted_y, "Actual y value:", actual)

plt.figure(figsize=(5,4))

#creates a scatter plot and labels the axes
plt.scatter(xtrain,ytrain, c="purple", label="Training Data")
plt.scatter(xtest, ytest, c="blue", label="Testing Data")

plt.scatter(xtest, predict, c="red", label="Predictions")

plt.xlabel("Typical Hours")
plt.ylabel("Hourly Rate")
plt.title("Hourly Rate by Typical Hours")
plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()