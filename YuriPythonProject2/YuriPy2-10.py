import math

str_n = input("Input N : ")
n = int(str_n)

sum = 0
while n > 0:
  sum += 1/(n**2)
  n -= 1
else:
  print("1/1^2 + 1/2^2 + 1/3^2 + ... + 1/N^2 =",sum)

error = abs(math.pi - sum)
print("the error between π and the sum is",error)