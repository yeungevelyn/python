import numpy
# create an array containing "frog", "cat" and "dog"
array1 = numpy.array(["frog", "cat", "dog"])
# display array items
for item in array1:
    print(item)



# create an array of 10 zeros as 32-bit integers
array2 = numpy.zeros(shape=10,dtype=numpy.int32)
print(array2)
# create an array of 10 boolean Trues
array3 = numpy.ones(shape=10, dtype=numpy.bool)
print(array3)

# create a 2-dimensional array
array4= numpy.array([[8,1,6],[3,5,7],[4,9,2]])
print(array4)

# 2d array representing a 3x4 matrix of ones as 32-bit integers
array5 = numpy.ones(shape=(3,4),dtype=numpy.int64)
print(array5)

# 2d array representing a 3x4 matrix of zeros as 64-bit integers
array6 = numpy.zeros(shape=(3,4),dtype=numpy.int64)
print(array6)
