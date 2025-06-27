# Inspect the DataFrame:

# Use .head() and .tail() to view your data.

# Use .info() and .describe() to understand the structure.

import pandas as pd

data = {
    'Product': ['Smartphone','Mobile','Smartwatch','Laptop','Dell'],
    'Price': [250, 300000, 150,60000,45000],
    'Stock': [15, 5, 4, 10, 6]
}
df = pd.DataFrame(data)

# # First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# # Columns
print(df.columns)

# Info about data types
print(df.info())

# Statistical summary
print(df.describe())