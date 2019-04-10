import numpy as np

a = [[1,2,3],[4,5,6]]
print(a)
# [[1, 2, 3], [4, 5, 6]]

a = np.array([[1,2,3],[4,5,6]])
print(a)
# [[1 2 3]
#  [4 5 6]]

# a = np.arange(1,7)
# print(a)

print(a+1)
# [[2 3 4]
#  [5 6 7]]

print(a-1)
# [[0 1 2]
#  [3 4 5]]

print(a*2)
# [[ 2  4  6]
#  [ 8 10 12]]

print(a/2)
# [[0.5 1.  1.5]
#  [2.  2.5 3. ]]