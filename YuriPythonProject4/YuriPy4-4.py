import operator
# from django.core.urlresolvers import reverse

list = [3, -10, 23, 4.5, 123]
listA = [3, -10, 23, 4.5, 123]
listB = [3, -10, 23, 4.5, 124]

def cmp(a,b):
  return (a>b) - (a<b)

print(cmp(listA, listB))
# -1

print(len(list))
# 5

print(max(list))
# 123

print(min(list))
# -10

# print(reverse(list))
# print(reversed(list))
