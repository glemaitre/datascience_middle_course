data = data[data["Sex"] != "."]
X, y = data.drop(columns=target_name), data[target_name]
