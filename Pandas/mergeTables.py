import pandas as pd

# create two sample dataframes
df1 = pd.DataFrame({
    'PERSON_ID':       ['A', 'B', 'C', 'D'],
    'CREATION_SET_ID': ['X', 'Y', 'X', 'Z'],
    'value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'PERSON_ID':       ['B', 'C', 'E', 'F'],
    'CREATION_SET_ID': ['Y', 'X', 'Z', 'X'],
    'PERSON_ID_NEW': [5, 6, 7, 8],
    'CREATION_SET_ID_NEW': [55, 66, 77, 88]
})

# perform the outer merge on the two columns
outer_merge_df = pd.merge(df1, df2, how='outer', on=['PERSON_ID', 'CREATION_SET_ID'])
left_merge_df = pd.merge(df1, df2, how='left', on=['PERSON_ID', 'CREATION_SET_ID'])
print(outer_merge_df)
print(left_merge_df)



# Create a sample dataframe
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

# Display the original dataframe
print('Original dataframe:')
print(df)

# Switch the column names
df = df.rename(columns={'a': 'b', 'b': 'a'})

# Display the updated dataframe
print('Updated dataframe:')
print(df)
