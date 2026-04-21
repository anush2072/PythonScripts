'''
Takes one element at a time and inserts it into its correct position within a growing sorted subarray. 
Efficient for small or nearly sorted data (O(n) in best case).
Time complexity: O(n^2) in worst case.
Space complexity: O(1) as it is an in-place sorting algorithm.
'''
def insertion_sort(arr):
    n= len(arr)
    result = [None]*n
    for i in range(n):
        result[i] = arr[i]
        j = i
        while j > 0:
            if result[j] < result[j-1]:
                result[j], result[j-1] = result[j-1], result[j]
                j = j-1
            else:
                break

    return result


# In-place approach (modifies original list instead if creating place holder)
def insertion_sort_v2(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key
    
    return arr


# Example Usage:
list = [21, 1, 26, 45, -29, 28, 2, 9, 16, 49]
print(f"Original list: {list}")
sorted_list = insertion_sort_v2(list)
print(f"Sorted list: {sorted_list}")
