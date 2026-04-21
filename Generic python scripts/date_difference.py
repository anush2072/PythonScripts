
# Calculate the number of days between `date1` and `date2`:
from datetime import datetime

# Ask the user for input dates
date1 = input("Enter the start date and time (format: YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the end date and time (format: YYYY-MM-DD HH:MM:SS): ")

# Convert the input strings to datetime objects
try:
    start_time = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
except ValueError:
    print("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.")
    exit()

# Calculate the difference
time_difference = end_time - start_time

# Get the number of days
days_difference = time_difference.total_seconds() / (24 * 3600)
print(f"Number of days between {date1} and {date2}: {days_difference:.2f} days")