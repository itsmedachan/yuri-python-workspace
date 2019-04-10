list = [1, 100, 10, 1000, 10000, 20000, 20, 2000, 200]
print(list)
# [1, 100, 10, 1000, 10000, 20000, 20, 2000, 200]

list.append(2)
print(list)
# [1, 100, 10, 1000, 10000, 20000, 20, 2000, 200, 2]

list.clear()
print(list)
# []

list = [1, 100, 10, 1000, 10000, 20000, 20, 2000, 200, 2, 100]
list_copied = list.copy()
print(list_copied)
# [1, 100, 10, 1000, 10000, 20000, 20, 2000, 200, 2, 100]

print(list.count(100))
# 2

list.extend('100')
print(list)
# [1, 100, 10, 1000, 10000, 20000, 20, 2000, 200, 2, 100, '1', '0', '0']

print(list.index(1)) # returns the index of the first element with the specified value
# 0 # 1 is at the index[0]

list.insert(3, 20)
print(list)
# [1, 100, 10, 20, 1000, 10000, 20000, 20, 2000, 200, 2, 100, '1', '0', '0']


list.pop(6) # removes the element at the specified position, index 6 is 20000 in this list
print(list)
# [1, 100, 10, 20, 1000, 10000, 20, 2000, 200, 2, 100, '1', '0', '0']


list.remove(1) # removes the element at the specified value
print(list)
# [100, 10, 20, 1000, 10000, 20, 2000, 200, 2, 100, '1', '0', '0']


list.reverse()
print(list)
# ['0', '0', '1', 100, 2, 200, 2000, 20, 10000, 1000, 20, 10, 100]


list.pop(0)
list.pop(0)
list.pop(0)
print(list)
# [100, 2, 200, 2000, 20, 10000, 1000, 20, 10, 100]

list.sort()
print(list)
# [2, 10, 20, 20, 100, 100, 200, 1000, 2000, 10000]