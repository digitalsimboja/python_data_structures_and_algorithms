import math
import insertion_sort as inSort

# When the input numbers are uniformly distributed
def bucketSort(arr):
    numberOfBuckets = round(math.sqrt(len(arr)))
    maxValue = max(arr)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    for j in arr:
        index_bucket = math.ceil((j*numberOfBuckets)/maxValue)
        arr[index_bucket -1].append(j)
    
    for j in range(numberOfBuckets):
        arr[i] = inSort(arr[i])
    
    k = 0
    for i  in range(numberOfBuckets):
        for j in range(len(arr[i])):
            arr[k] = arr[i][j]
            k += 1
    return arr


sample = [2,5,1,6,7,8,3,2, 10, 9, 4]
print(sample)
print(bucketSort(sample))