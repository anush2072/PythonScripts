'''
Scans the list to find the minimum element and moves it to the beginning
Time complexity: O(n^2) in worst case.
Space complexity: O(1) as it is an in-place sorting algorithm.
'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example Usage:
list = [21, 1, 26, 45, -29, 28, 2, 9, 16, 49]
print(f"Original list: {list}")
sorted_list = selection_sort(list)
print(f"Sorted list: {sorted_list}")
