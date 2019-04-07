import math

class YuriPythonProject3no2:
  
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

variables = YuriPythonProject3no2()
variables.a = a
variables.b = b
variables.c = c
print(variables.biggest_variable())

# ひとつめの変数を入力してください :3
# ふたつめの変数を入力してください :5
# みっつめの変数を入力してください :1
# 最大値は5.0です