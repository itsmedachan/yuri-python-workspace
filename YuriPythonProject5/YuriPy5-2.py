import math

class YuriPythonProject5no2:
  
  def biggest_variable(self):
    if a >= b:
      if a >= c:
        return "最大値は"+str(a)+"です"
      else:
        return "最大値は"+str(c)+"です"
    elif b >= c:
      return "最大値は"+str(b)+"です"
    else:
        return "最大値は"+str(c)+"です"
        

a = float(input('ひとつめの変数を入力してください :'))
b = float(input('ふたつめの変数を入力してください :'))
c = float(input('みっつめの変数を入力してください :'))

variables = YuriPythonProject5no2()
variables.a = a
variables.b = b
variables.c = c
print(variables.biggest_variable())
