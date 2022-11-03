# Sinking sort
# We repeatedly take two pairs and continue to swap with the greater value to the right
# When list is sorted
# Space efficient
# Avoid if time is concern because this takes O(n^2)
def bubbleSort(arr):
    for i in range(len(arr) -1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
           
    return arr


sample = [2,5,1,6,7,8,3,2, 10, 9, 4]
print(sample)
print(bubbleSort(sample))