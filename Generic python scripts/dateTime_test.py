# 
# ref: https://discuss.python.org/t/deprecating-utcnow-and-utcfromtimestamp/26221

from datetime import datetime
import pytz

print(datetime.utcnow() )
print(datetime.now(pytz.UTC))
print(datetime.now(pytz.UTC).replace(tzinfo=None))
print(datetime.now(pytz.UTC).replace(tzinfo=None).isoformat(' '))


input_string = '12/24/23 19:21'
input_format = '%m/%d/%y %H:%M'
output_format = '%Y-%m-%d %H:%M:%S'

try:
    # Parse the input string using the input format
    date_time_obj = datetime.strptime(input_string, input_format)

    # Convert the datetime object to the desired output format
    output_string = date_time_obj.strftime(output_format)

    print(f"Converted string: {output_string}")
except ValueError as e:
    print(f"Error: {e}")