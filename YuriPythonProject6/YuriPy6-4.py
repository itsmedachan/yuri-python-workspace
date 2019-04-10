import numpy as np

np_array = np.array([0,1,2,3,4,5])
print(np_array)
# [0 1 2 3 4 5]

np_slice = np_array[1:3] # start =< x < stop
print(np_slice)
# [1 2]
# ref: https://note.nkmk.me/python-slice-usage/