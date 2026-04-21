import pandas as pd


def print_df_stats(df):
    # Get the shape of the DataFrame
    rows, cols = df.shape
    print(f"The DataFrame has {rows} rows and {cols} columns.")

    # Get the size of the DataFrame in bytes
    bytes_size = df.memory_usage(deep=True).sum()

    # Convert the size to MB or GB
    # If the DataFrame size is less than 100MB, it is represented in MB
    # If the DataFrame size is greater than or equal to 100 MB, it is represented in GB
    if bytes_size < 100 * 1024 ** 2:
        size_mb = bytes_size / (1024 ** 2)
        print(f"The DataFrame size is {size_mb:.2f} MB.")
    else:
        size_gb = bytes_size / (1024 ** 3)
        print(f"The DataFrame size is {size_gb:.2f} GB.")
        

if __name__ == '__main__':
    parquet_file = '<FILE_PATH_HERE>'
    try:
        df = pd.read_parquet(parquet_file, engine='pyarrow')
        print_df_stats(df)
    except:
        import pyarrow.parquet as pq
        # Read the Parquet file metadata
        parquet_metadata = pq.read_metadata(parquet_file)

        # Get the total number of rows
        num_rows = parquet_metadata.num_rows

        print(f"parquet_metadata: Number of rows in the Parquet file: {num_rows}")  

        # Get the column names and data types
        column_names = [field.name for field in parquet_metadata.schema.to_arrow_schema().fields]
        column_types = [field.type for field in parquet_metadata.schema.to_arrow_schema().fields]

        print("Column names and data types:")
        for col_name, col_type in zip(column_names, column_types):
            print(f"  {col_name}: {col_type}")