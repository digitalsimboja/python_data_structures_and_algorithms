def flatten(arr):
    flattened = []
    for item in arr:
        if type(item) is list:
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened