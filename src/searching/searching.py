# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0: # empty array index not found
        return -1
    middle_index = (start + end) // 2 # midway point
    middle_value = arr[middle_index] # value of the midway

    if middle_value == target: # value found 
        return middle_index # return the index of the found value
    else:
        if middle_value < target: # if the midpoint value is less than the target value
            return binary_search(arr, target, middle_index, end) # run binary search starting from the midway point to the end
        if middle_value > target: # if the midpoint value is greater than the target value
            return binary_search(arr, target, start, middle_index) # run binary search starting from the start to the midway point
    
    return -1 # index not found

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
