import pandas as pd
import numpy as np
import unittest

# Define the calculateSGStats function
def calculateSGStats(x):
    # Calculate statistics for the input array 'x'
    temp = np.zeros(11)
    temp[0] = np.sum(~np.isnan(x))
    temp[1] = np.nanmean(x)
    temp[2] = np.sum(x <= 50)
    temp[3] = np.sum(x <= 80)
    temp[4] = np.sum(x >= 300)
    temp[5] = np.sum((x >= 40) & (x < 55))
    temp[6] = np.sum((x >= 55) & (x < 70))
    temp[7] = np.sum((x >= 70) & (x < 180))
    temp[8] = np.sum((x >= 180) & (x < 250))
    temp[9] = np.sum((x >= 250) & (x < 300))
    temp[10] = np.sum((x >= 300) & (x < np.inf))
    return temp

class TestCalculateSGStats(unittest.TestCase):
    def test_calculate_sg_stats(self):
        # Create a sample DataFrame with 'year', 'month', and 'SG' columns
        data = {
            'year': [2022, 2022, 2023, 2023],
            'month': [11, 12, 1, 2],
            'SG': [100, 150, 80, 120]
        }
        df = pd.DataFrame(data)
        
        # Apply the calculateSGStats function and convert the result to a nested list
        result = df.groupby(['year', 'month'])['SG'] \
            .apply(calculateSGStats) \
            # .unstack(fill_value=0) \
            # .reset_index() \
            # .values.tolist()

        print(result)
        
        # # Expected result
        expected_result = [
            [2022, 11, 2, 125.0, 0, 0, 0, 2, 0, 0, 0],
            [2022, 12, 2, 150.0, 0, 0, 0, 2, 0, 0, 0],
            [2023, 1, 2, 80.0, 0, 0, 0, 2, 0, 0, 0],
            [2023, 2, 2, 120.0, 0, 0, 0, 2, 0, 0, 0]
        ]

        # # Assert the actual result matches the expected result
        # self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
