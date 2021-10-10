from sklearn.linear_model import LinearRegression

X, y = data[["Flipper Length (mm)"]], data["Body Mass (g)"]

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
y_pred[:5]
