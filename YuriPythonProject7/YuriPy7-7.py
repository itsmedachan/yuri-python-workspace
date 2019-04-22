import numpy as np
import pickle

f = open('/Users/yuri/sophia/YuriPythonWorkspace/YuriPythonProject7/dic.pickle', 'rb')
dic = pickle.load(f)

print(dic)
print(dic.keys())
print(dic.values())

# {'apple': 0, 'banana': 1, 'orange': 2}
# dict_keys(['apple', 'banana', 'orange'])
# dict_values([0, 1, 2])