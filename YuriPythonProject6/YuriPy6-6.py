import numpy as np

np_array = np.array([[0,1,2],[4,5,6],[7,8,9]])
print(np_array)
# [[0 1 2]
#  [4 5 6]
#  [7 8 9]]

np_slice3 = np_array[1:-1]
print("[1:-1] = "+str((np_slice3)))
# [1:-1] = [[4 5 6]]

# ref: https://note.nkmk.me/python-slice-usage/