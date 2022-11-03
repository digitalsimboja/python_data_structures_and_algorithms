def linearSearch(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

sample = [20,40,30,50, 90]
print(linearSearch(sample, 90))