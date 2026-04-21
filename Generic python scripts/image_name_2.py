import os
import random
from datetime import datetime, timedelta

def rename_files():
    start_time = datetime(2025, 7, 20, 3, 7, 0)
    end_time = datetime(2025, 7, 20, 4, 24, 0)
    directory = '<FOLDER_PATH_HERE>'

    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            file_path = os.path.join(directory, filename)
            file_datetime = datetime.fromtimestamp(os.path.getmtime(file_path))

            # Generate a random time between start_time and end_time
            random_time = start_time + timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))

            new_filename = f"PXL_{random_time.strftime('%Y%m%d_%H%M%S')}.jpg"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)

if __name__ == '__main__':
    rename_files()