import numpy as np

m = np.matrix([[1,2,3],[4,5,6]])
n = np.matrix([[1,2],[3,4],[5,6]])

product = np.dot(m,n)
print(product)