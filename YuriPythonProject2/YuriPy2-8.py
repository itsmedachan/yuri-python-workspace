str_n = input("Input N : ")
n = int(str_n)

sum = 0
while n > 0:
  sum += n
  n -= 1
else:
  print("1 + 2 + 3 + ... + N =",sum)