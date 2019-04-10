import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
# [[1 2 3]
#  [4 5 6]]

# 全要素の和
print(np.sum(a))
# 21

# 列ごとの和
print(np.sum(a,axis=0))
# [5 7 9]

# 行ごとの和
print(np.sum(a,axis=1))
# [ 6 15]