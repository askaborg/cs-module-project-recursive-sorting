# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    indexA = 0 # index for arrayA
    indexB = 0 # index for arrayB
    mergeIndex = 0 # index of merged arr
          
    # when indexA is less then length of arrayA and
    # indexB is less than arrayB (both arrays contain values)
    while indexA < len(arrA) and indexB < len(arrB):
        # if the value of arrA at the indexA is greater than value of arrB at the indexB
        # set the index of the mergeIndex to the index of A
        # increment the indexA
        if arrA[indexA] < arrB[indexB]: 
            merged_arr[mergeIndex] = arrA[indexA] 
            indexA += 1 
        # the value of arrB at the indexB is greater than arrA at the indexA
        # set the index of the mergeIndex to the index of B
        # increment the indexB
        # increment the mergeIndex
        else: 
            merged_arr[mergeIndex] = arrB[indexB] 
            indexB += 1 
        mergeIndex += 1 
    # when arrayA is not empty but arrayB is
    while indexA < len(arrA): 
        # set the index of the merged_arr to the arrA index
        # increment the indexes
        merged_arr[mergeIndex] = arrA[indexA]
        indexA += 1
        mergeIndex += 1
    # when arrayB not empty
    while indexB < len(arrB): 
        # set the index of the merged_arr to the arrB index
        # increment the indexes
        merged_arr[mergeIndex] = arrB[indexB] 
        indexB += 1
        mergeIndex += 1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # when arr is not empty
    # set the mid variable to be half of the arr
    # set left to be everything up to the middle
    # set right to be everything after the middle
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
