import pandas as pd

# create an empty DataFrame with columns 'first_name', 'age', 'city', 'state', and 'zip_code'
df = pd.DataFrame(data={}, columns=['first_name', 'age', 'city', 'state', 'zip_code'])

# check if the DataFrame is empty
if df.empty or df.isnull().any().any():
    print("The df is empty/null values:")
else:
    print("No empty/null columns found.")