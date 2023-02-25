# pip install numpy
import numpy as np
my_list = [1, 2, 3]

arr = np.array(my_list)
print(arr)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = print(np.array(my_mat))

print(np.arange(0, 10))
print(np.arange(0, 10, 2)) # add step

print(np.zeros((5, 5)))
print(np.ones((5, 5)))

print(np.linspace(0, 5, 10)) # number of values

print(np.eye(5)) #identity matrix

# random number - uniform distribution
print(np.random.rand(5, 5))

# random number - normal distribution
print(np.random.randn(5, 5))

# random number - integer
print(np.random.randint(0, 100))

# Reshape
arr = np.arange(25)
print(arr.reshape(5, 5))

# from numpy.random import randint
# randint(0, 50, 10)
ranarr = np.random.randint(0, 50, 10)
print(ranarr)
print(ranarr.max()) # max value
print(ranarr.argmax()) # position

# Array indexing