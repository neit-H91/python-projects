import pandas as pd
from datetime import datetime

df = pd.read_csv('Data/raw/imdb_top_1000.csv')

min = 1895

max = datetime.now().year

# df['Released_Year'] = df['Released_Year'].apply(lambda x: 1 if x.between(min,max).any() else 0,axis=1)

# print(df)

# print(df.dtypes)

# Find duplicates based on Released_Year and Title
duplicates = df[df.duplicated(subset=['Released_Year', 'Series_Title'], keep=False)]

if duplicates.empty:
    print("All Released_Year + Title combinations are unique ✅")
else:
    print("Duplicate Released_Year + Title found:")
    print(duplicates)
