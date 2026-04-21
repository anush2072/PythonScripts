'''
Repeatedly compares adjacent elements and swaps them if they are in the wrong order. 
It is simple but slow, with a time complexity of O(n^2).
Time complexity: O(n^2) in worst case.
Space complexity: O(1) as it is an in-place sorting algorithm.
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


# Example Usage:
list = [21, 1, 26, 45, -29, 28, 2, 9, 16, 49]
print(f"Original list: {list}")
sorted_list = bubble_sort(list)
print(f"Sorted list: {sorted_list}")
