# print the path of the Python interpreter that is currently running your Python script
import sys
print(sys.executable, "\n")

import os
# Iterate over the keys and values of the environ dictionary
for key, value in os.environ.items():
    if(key.lower().__contains__('secret') or key.lower().__contains__('token')):
        continue
    print(f"{key} = {value}")

# Run the "pip list" command and capture its output
import subprocess
output = subprocess.check_output(["pip", "list"])
print("\n", output.decode("utf-8"))

# Print pandas version
import pandas as pd
print("pandas version:", pd.__version__)
