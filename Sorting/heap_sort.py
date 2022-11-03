# Insert data to Binary Heap Tree
# Extract data from the Binary heap
# Best suited for array and not linked list

def heapify(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heapSort(arr):
    n = len(arr)
    for i in range(int(n/2) - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    arr.reverse()

sample = [2,5,1,6,7,8,3,2, 10, 9, 4]
print(sample)
heapSort(sample)
print(sample)