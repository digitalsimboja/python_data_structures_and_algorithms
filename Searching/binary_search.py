# works on sorted arrays
# arr must be a sorted array
import math
def binarySearch(arr, value):
    start = 0
    end = len(arr) -1
    middle = math.floor((start + end)/2)
    while not(arr[middle] == value) and start <= end:
        if value < arr[middle]:
            end = middle -1
        else:
            start = middle + 1
        middle = math.floor((start + end)/2)
    if arr[middle] == value:
        return middle
    else:
        return -1
    

sample = [20,40,30,50, 90]
print(binarySearch(sample, 90))