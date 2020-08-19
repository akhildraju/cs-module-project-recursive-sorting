# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1
    if target < arr[start] or target > arr[end]:
        return -1
        
    slice = arr[start:end]
                                
    minIndex = 0
    maxIndex = len(slice) - 1
    midIndex = int(maxIndex / 2)
    midValue = slice[midIndex]
            
    if target > midValue: 
        return binary_search(arr, target, midIndex+1, end)
            
    if target < midValue: 
        return binary_search(arr, target, start, midIndex)
            
    if target is midValue: 
        return arr.index(target)
    else: 
        return -1 



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

