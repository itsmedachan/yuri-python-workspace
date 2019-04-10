import math

class YuriPythonProject5no4:
  
  def rectangle_area(self):
    surroundings = side_a*2 + side_b*2
    rectangle_area = side_a*side_b
    return "周囲は"+str(surroundings)+"、面積は"+str(rectangle_area)+"です"

print('長方形の周囲と面積を求めます')
side_a = float(input('一辺の長さを入力してください a:'))
side_b = float(input('もう一辺の長さを入力してください b:'))

rectangle = YuriPythonProject5no4()
rectangle.side_a = side_a
rectangle.side_b = side_b
print(rectangle.rectangle_area())

# 長方形の周囲と面積を求めます
# 一辺の長さを入力してください a:4
# もう一辺の長さを入力してください b:5
# 周囲は18.0、面積は20.0です