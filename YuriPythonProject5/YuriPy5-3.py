import math

class YuriPythonProject5no3:
  
  def circle_area(self):
    circumference_length = 2*math.pi*radius
    circle_area = math.pi*radius*radius
    return "円周は"+str(circumference_length)+"、面積は"+str(circle_area)+"です"
        

print('円の円周と面積を求めます')
radius = float(input('半径を入力してください: '))

circle = YuriPythonProject5no3()
circle.radius = radius
print(circle.circle_area())

# 円の円周と面積を求めます
# 半径を入力してください: 2
# 円周は12.566370614359172、面積は12.566370614359172です