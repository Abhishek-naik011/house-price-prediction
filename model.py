import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# simple dataset (you can replace with your dataset later)
data = {
    "area": [500, 1000, 1500, 2000],
    "bedrooms": [1, 2, 3, 4],
    "price": [100000, 200000, 300000, 400000]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

# save model
pickle.dump(model, open("model.pkl", "wb"))