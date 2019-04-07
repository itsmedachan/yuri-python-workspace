print('eを求めます')
print('e^x = 1 + x/1! + x^2/2! + x^3/3! + ...')


x = int(input('please input x :'))

s = 0
factorial = 1
i = 0
while i <= x:
  factorial = factorial*(i+1)
  s += (x**i)/factorial
  i += 1

print('e^x =',s)
print('e =',s**(1/x))

# eを求めます
# e^x = 1 + x/1! + x^2/2! + x^3/3! + ...
# please input x :100
# e^x = 1.5215509996380548e+41
# e = 2.581207183848627