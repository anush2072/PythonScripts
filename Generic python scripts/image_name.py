import datetime
import random

def generate_image_names(start_date, end_date, num_names):
    """
    Generates a list of image names based on the provided date and time range.
    
    Args:
        start_date (datetime.datetime): The start date and time for the image names.
        end_date (datetime.datetime): The end date and time for the image names.
        num_names (int): The number of image names to generate.
    
    Returns:
        list: A list of generated image names.
    """
    image_names = []
    for _ in range(num_names):
        date_time = start_date + datetime.timedelta(
            seconds=random.randint(0, (end_date - start_date).total_seconds())
        )
        filename = f"PXL_{date_time.strftime('%Y%m%d')}_{date_time.strftime('%H%M%S%f')[:-3]}.jpg"
        image_names.append(filename)
    return image_names

# Example usage
start_date = datetime.datetime(2023, 8, 11, 19, 57, 0)  # August 11, 2023 at 7:57 PM
end_date = datetime.datetime(2023, 8, 12, 0, 0, 0)  # August 12, 2023 at 12:00 AM
num_names = 10

image_names = generate_image_names(start_date, end_date, num_names)
for name in image_names:
    print(name)