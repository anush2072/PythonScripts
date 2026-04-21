import pickle
import pandas as pd

# Replace 'your_pickle_file.pkl' with the path to your pickle file
with open('your_pickle_file.pkl', 'rb') as file:
    data = pickle.load(file)
    # inspect the data
    # print(data)
    
    # load data from pickle file into pandas dataframes
    if isinstance(data, dict):
        dfs = {key: pd.DataFrame(value) for key, value in data.items()}
    elif isinstance(data, list):
        dfs = pd.DataFrame(data)
    else:
        raise ValueError("Unsupported data format")
    
    for key, df in dfs.items():
        print(f"DataFrame for {key}:")
        print(df)
