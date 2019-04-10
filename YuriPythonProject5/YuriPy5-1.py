import math

# wip
class YuriPythonProject5no1:
  
  def triangle_area(self):
    p = (self.a + self.b + self.c)/2
    squared_area = p*(p-self.a)*(p-self.b)*(p-self.c)
    area = math.sqrt(squared_area)
    return area
  
  def valid(self):
    if self.a >= self.b:
      if self.a >= self.c:
        return self.a < self.b + self.c
      else:
        return self.c < self.a + self.b
    elif self.b >= self.c:
      return self.b < self.c + self.a
    else:
        return self.c < self.a + self.b

side_a = float(input('辺の長さを入力してください a:'))
side_b = float(input('辺の長さを入力してください b:'))
side_c = float(input('辺の長さを入力してください c:'))
triangle = YuriPythonProject5no1()
triangle.a = side_a
triangle.b = side_b
triangle.c = side_c

if not triangle.valid():
  print('invalid length for making triangle')
  side_a = float(input('辺の長さを入力してください a:'))
  side_b = float(input('辺の長さを入力してください b:'))
  side_c = float(input('辺の長さを入力してください c:'))
  triangle = YuriPythonProject5no1()
  triangle.a = side_a
  triangle.b = side_b
  triangle.c = side_c
  triangle.valid()
else:
  print(triangle.triangle_area())