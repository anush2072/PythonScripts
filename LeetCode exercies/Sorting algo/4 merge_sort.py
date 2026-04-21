'''
Divides the array into two halves, recursively sorts each half, and then merges them back together.
Time complexity: O(n log n) in worst case.
Space complexity: O(n) due to the additional space used for merging.
'''
def merge(left, right):
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_list.append(left[left_index])
            left_index = left_index + 1
        else:
            merged_list.append(right[right_index])
            right_index = right_index + 1
    
    # Append any remaining elements from the left list
    if left_index < len(left):
        merged_list.extend(left[left_index:])
        
    # Append any remaining elements from the right list
    if right_index < len(right):
        merged_list.extend(right[right_index:])

    return merged_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

# Example Usage:
my_list = [21, 1, 26, 45, -29, 28, 2, 9, 16, 49]
sorted_list = merge_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")


"""
TypeError: slice indices must be integers or None

RootCasue: len(arr) // 2 -vs- len(arr) / 2
    // (Floor Division) -->  The // operator divides the numbers and rounds down to the nearest whole integer
    Example: 11 // 2  =  5

    / (True Division)   -->  The / operator performs standard division and always returns a decimal.
    Example: 11 / 2	= 5.5
"""