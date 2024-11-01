import pickle

with open(
    "Machine Learning A-Z/Part 2 - Regression/Section 5 - Multiple Linear Regression/Python/linear_regression_model.pkl",
    "rb",
) as file:
    model = pickle.load(file)

pred = model.predict([[0.0, 0.0, 1.0, 165349.2, 136897.8, 471784.1]])
print(pred)
