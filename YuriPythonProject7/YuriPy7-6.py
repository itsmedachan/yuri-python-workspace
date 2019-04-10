import pickle

dic = {'apple':0, 'banana':1, 'orange':2}
f =open('../YuriPy7-6.py', 'wb')
pickle.dump(dic, f)
print(dic)


# ref: https://techacademy.jp/magazine/15826