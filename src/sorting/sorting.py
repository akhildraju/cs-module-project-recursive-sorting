# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    merged_arr = []

    # Your code here
    leftIndex, rightIndex = 0, 0

    while leftIndex < len(arrA) and rightIndex < len(arrB):
        if arrA[leftIndex] < arrB[rightIndex]:
            merged_arr.append(arrA[leftIndex])
            leftIndex += 1
        else:
            merged_arr.append(arrB[rightIndex])
            rightIndex += 1
            
    merged_arr += arrA[leftIndex:]
    merged_arr += arrB[rightIndex:]

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
 
    midIndex = int(len(arr) / 2)
      
    arrA = merge_sort(arr[:midIndex])
    arrB = merge_sort(arr[midIndex:])

    return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

