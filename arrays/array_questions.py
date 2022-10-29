def solutionArray(arr, target):
    
    for i in range(len(arr)):
        for k in range(i):
            if arr[i] + arr[k] == target:
                return [i, k]

nums = [3,3]
result = solutionArray(nums, 6)
print(result)