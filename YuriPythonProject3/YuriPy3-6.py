import math

class YuriPythonProject3no6:
  
  def kai_no_koushiki(self):
    D = b**2 - 4*a*c
    kai_no_koushiki_1 = (-b-math.sqrt(D))/2*a
    kai_no_koushiki_2 = (-b+math.sqrt(D))/2*a
    return "解は"+str(kai_no_koushiki_1)+"と"+str(kai_no_koushiki_2)+"です"

print('二次方程式の解を求めます')
print('ax^2 + bx + c = 0')
a = float(input('aを入力してください a:'))
b = float(input('bを入力してください b:'))
c = float(input('cを入力してください c:'))

equation = YuriPythonProject3no6()
equation.a = a
equation.b = b
equation.c = c
print(equation.kai_no_koushiki())

# 二次方程式の解を求めます
# ax^2 + bx + c = 0
# aを入力してください a:1
# bを入力してください b:-3
# cを入力してください c:2
# 解は1.0と2.0です