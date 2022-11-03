# Get a pivot number
# When average time expeected s O(NlogN)
# First create a partition helper function
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j],arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

cList = [2,1,7,6,5,3,4,9,8]
quickSort(cList, 0, 8)
print(cList)