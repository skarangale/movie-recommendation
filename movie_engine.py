import pandas as pd

#read data from csv
df = pd.read_csv('dataset/movies_metadata.csv')
print(df.head(10))