import pandas as pd

def load_data():
    return pd.read_csv("C:/Users/ankit/Documents/AAAAA SHIWANI/New Project/Python + Power BI/shopping_trends.csv")

# Call the function directly
data = load_data()

print(data.head())


# Checking if there is any missing values
data.isnull().sum()

# Other exploration code
print(data.shape)
print(data.info())
print(data.describe())

