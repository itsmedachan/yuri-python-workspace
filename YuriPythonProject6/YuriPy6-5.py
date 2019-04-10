import numpy as np

np_array = np.array([[0,1,2],[4,5,6],[7,8,9]])
print(np_array)
# [[0 1 2]
#  [4 5 6]
#  [7 8 9]]

np_slice2 = np_array[1:2,0:1]
print("[1:2,0:1] = "+str(np_slice2))
# [1:2,0;1] = [[4]]

np_slice2 = np_array[1:,0:]
print("[1:,0:] = ")
print(np_slice2)
# [1:,0:] = 
# [[4 5 6]
#  [7 8 9]]

np_slice2 = np_array[:2,:1]
print("[:2,:1] = ")
print(np_slice2)
# [:2,:1] = 
# [[0]
#  [4]]

# ref: https://note.nkmk.me/python-slice-usage/