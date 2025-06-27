# Selection and Indexing:

# Select only the Name column.

# Select the first 3 rows using .iloc.

# Select people older than 30.

import pandas as pd

data = {
    'Name': ['Aditya', 'Piyush', 'Prasad','Sumedh','Jayesh'],
    'Age': [25, 30, 35, 32, 18],
    'City': ['Delhi', 'Kalwan', 'Minidubai','Manmad','Malegoan']
}
df = pd.DataFrame(data)

print(df['Name'])
print(df.iloc[0:3])
print(df[df['Age']>30])



