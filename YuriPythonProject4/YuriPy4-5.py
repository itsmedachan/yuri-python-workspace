listP = [3, -10, 23, 4.5, 3]

listP.append(345)
print(listP)
# [3, -10, 23, 4.5, 3, 345]

print(listP.count(3)) # frequency of 3
# 2

print(listP.index(-10)) # index of -10
# 1

listP.insert(1, 5000) # insert 5000 at index 1
print(listP)
# [3, 5000, -10, 23, 4.5, 3, 345]

x = listP.pop() # returns the last element from the list
print(x)
# 345


listP.remove(23) # deletes elements from the list
print(listP)
# [3, 5000, -10, 4.5, 3]