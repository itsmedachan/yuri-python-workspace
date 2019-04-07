import math

class YuriPythonProject3no1:
  
  def triangle_area(self):
    p = (self.a + self.b + self.c)/2
    squared_area = p*(p-self.a)*(p-self.b)*(p-self.c)
    area = math.sqrt(squared_area)
    return area

side_a = float(input('辺の長さを入力してください a:'))
side_b = float(input('辺の長さを入力してください b:'))
side_c = float(input('辺の長さを入力してください c:'))

triangle = YuriPythonProject3no1()
triangle.a = side_a
triangle.b = side_b
triangle.c = side_c
print(triangle.triangle_area())

# 辺の長さを入力してください a:3
# 辺の長さを入力してください b:4
# 辺の長さを入力してください c:5
# 6.0