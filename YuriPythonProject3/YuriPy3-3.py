import math

class YuriPythonProject3no3:
  
  def circle_area(self):
    circumference_length = 2*math.pi*radius
    circle_area = math.pi*radius*radius
    return "円周は"+str(circumference_length)+"、面積は"+str(circle_area)+"です"
        

print('円の円周と面積を求めます')
radius = float(input('半径を入力してください :'))

circle = YuriPythonProject3no3()
circle.radius = radius
print(circle.circle_area())

# 円の円周と面積を求めます
# 半径を入力してください :10
# 円周は62.83185307179586、面積は314.1592653589793です