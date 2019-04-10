import numpy as np

np_array1 = np.array([[0,1],[2,3]])
np_array2 = np.array([[4,5],[6,7]])

np_vstack = np.vstack([np_array1,np_array2])
print(np_vstack)
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]]

np_hstack = np.hstack([np_array1,np_array2])
print(np_hstack)
# [[0 1 4 5]
#  [2 3 6 7]]