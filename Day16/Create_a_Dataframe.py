# Create a DataFrame:

# Create a DataFrame with columns: Products, Price, and Stock.

# Add 5 sample rows.

import pandas as pd
# Creating a DataFrame from a dictionary
data = {
    'Product': ['Smartphone','Mobile','Smartwatch','Laptop'],
    'Price': [250, 300000, 150,60000],
    'Stock': [15, 5, 4, 10]
}
df = pd.DataFrame(data)
print(df.to_string(index=False))

# print(df)
