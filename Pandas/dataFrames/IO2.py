
import pandas as pd


# Read just 5 rows to see what's there
df = pd.read_csv("artwork_data.csv", nrows=5)

#print(df)

# Limit columns
df = pd.read_csv("artwork_data.csv", nrows=5,
                 index_col='id',
                 usecols=['id', 'artist'])
#print(df)

df.to_csv("Test1.csv")

print("From generated file")
df = pd.read_csv("Test1.csv", nrows=5)
print(df)
