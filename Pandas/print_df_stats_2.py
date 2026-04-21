import pandas as pd
from pyspark.sql import DataFrame as SparkDataFrame

def print_df_stats(df):
    if isinstance(df, pd.DataFrame):
        # Pandas DataFrame
        rows, cols = df.shape
        print(f"The DataFrame has {rows} rows and {cols} columns.")
        
        bytes_size = df.memory_usage(deep=True).sum()
        
        if bytes_size < 100 * 1024 ** 2:
            size_mb = bytes_size / (1024 ** 2)
            print(f"The DataFrame size is {size_mb:.2f} MB.")
        else:
            size_gb = bytes_size / (1024 ** 3)
            print(f"The DataFrame size is {size_gb:.2f} GB.")
    
    elif isinstance(df, SparkDataFrame):
        # Spark DataFrame
        rows = df.count()
        cols = len(df.columns)
        print(f"The DataFrame has {rows} rows and {cols} columns.")
        
        # Calculate the size of the DataFrame in memory
        bytes_size = df.rdd.map(lambda row: len(str(row))).reduce(lambda x, y: x + y)
        
        if bytes_size < 100 * 1024 ** 2:
            size_mb = bytes_size / (1024 ** 2)
            print(f"The DataFrame size is {size_mb:.2f} MB.")
        else:
            size_gb = bytes_size / (1024 ** 3)
            print(f"The DataFrame size is {size_gb:.2f} GB.")
    
    else:
        print("The input is neither a Pandas DataFrame nor a Spark DataFrame.")
