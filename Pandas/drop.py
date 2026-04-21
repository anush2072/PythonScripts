import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [6, 7, 8, 9, 10],
                   'C': [11, 12, 13, 14, 15]})

# filter the rows based on column A and assign to df
df = df.drop(df[(df['A'] == 2) | (df['A'] == 4)].index)

print(df)
