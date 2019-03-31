# 演算子の優先順位
a = 23
b = 10
c = -12
d = 2

x = a*b + c/d
y = a*(b + c/d)
z = (a*b +c)/d

print(x)
# 224.0
print(y)
# 92.0
print(z)
# 109.0