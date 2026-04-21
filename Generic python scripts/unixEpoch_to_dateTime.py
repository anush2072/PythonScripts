
# To convert  Unix epoch (January 1, 1970) to a human-readable datetime
from datetime import datetime

# Given timestamp in milliseconds
timestamp_ms = 1732919832985

# Convert to seconds by dividing by 1000
timestamp_s = timestamp_ms / 1000

# Convert to datetime - local time zone
dt_local = datetime.fromtimestamp(timestamp_s)
print(f"Converted `{timestamp_ms}` to local datetime:", dt_local)

# Convert to datetime - UTC time zone
dt = datetime.utcfromtimestamp(timestamp_s)
print(f"Converted `{timestamp_ms}` to UTC datetime:", dt)
