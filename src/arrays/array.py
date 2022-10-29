from array import *
import numpy as np

# create an array
my_array = array('i', [1, 2, 3, 4, 5, 6])
print(my_array)

# traverse an array
for i in my_array:
    print(i)

# access an element with the index
print('The first element:', my_array[0])

#insert element at the end of array
my_array.append(7)
print(my_array)

#insert using insert method
my_array.insert(0, 0)
print(my_array)

# extend an array
my_arr = array('i', [ 8, 9])
my_array.extend(my_arr)
print(my_array)

# add fromList
myList  = [20, 22]
my_array.fromlist(myList)
print(my_array)

my_arr.reverse()
print(my_arr)
print(my_arr.count(8))

# create 2D array using numpy
twoDArray = np.array([[1,2,3], [4,5,6], [7,8,9]])

def traverse(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])
print('2D ARRAY:')
traverse(twoDArray)

def searchTDArray(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                print('The value is located at ' + str(i) +','+ str(j))

searchTDArray(twoDArray, 4)