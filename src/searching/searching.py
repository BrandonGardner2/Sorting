# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while high > 0:
        middle = (low+high)//2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            low = middle
        elif arr[middle] > target:
            high = middle
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    elif target == arr[middle]:
        return middle
    elif target < arr[middle]:
        return binary_search_recursive(arr, target, 0, middle)
    elif target > arr[middle]:
        return binary_search_recursive(arr, target, middle, high)
    # TO-DO: add missing if/else statements, recursive calls

    # low = 0
    # high = len(arr) - 1

    # if <
    # low = 0
    # high = middle

    # if >
    # low = middle
    # high = high
