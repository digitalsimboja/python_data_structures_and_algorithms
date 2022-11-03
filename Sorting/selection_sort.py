# Find the minimum repeatedly and move it to the sorted part

def selectionSort(arr):
    for i in range(len(arr)):
        tempMinIndex = i
        for j in range(i+1, len(arr)):
            if arr[tempMinIndex] > arr[j]:
                tempMinIndex = j
        arr[i], arr[tempMinIndex] = arr[tempMinIndex], arr[i]
    return arr


sample = [2,5,1,6,7,8,3,2, 10, 9, 4]
print(sample)
print(selectionSort(sample))