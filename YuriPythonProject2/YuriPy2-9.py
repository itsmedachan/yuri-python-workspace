str_n = input("Input your number : ")
n = int(str_n)

sum = 0
while n > 0:
  sum += 1/n
  n -= 1
else:
  print("1 + 1/2 + 1/3 + ... + 1/N =",sum)