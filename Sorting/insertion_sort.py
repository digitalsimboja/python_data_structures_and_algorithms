# When you need to sort continous stream of numbers and wamt to keep them sorted
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


sample = [2,5,1,6,7,8,3,2, 10, 9, 4]
print(sample)
print(insertionSort(sample))