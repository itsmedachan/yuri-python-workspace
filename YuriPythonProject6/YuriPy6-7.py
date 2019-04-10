import numpy as np

np_array = np.array([0,1,2,3,4,5])
print(np_array)
# [0 1 2 3 4 5]

print(type(np_array))
# <class 'numpy.ndarray'>

list_array = np_array.tolist()
print(type(list_array))
# <class 'list'>

np_array = np.array(list_array)
print(type(np_array))
# <class 'numpy.ndarray'>
