def callback_checker(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return callback_checker(arr[1:], cb)
    return True

def isOdd(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(callback_checker([3,4,6,7,7], isOdd))