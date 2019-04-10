# サイコロを２回降るプログラム
# 同じ目が出たら'lucky'と言う
import random

class YuriPythonProject5no5:

  def checktheluck(self):
    if self.first == self.second:
      return "Yay! You are lucky!"
    else:
      return "Oh, sorry. You must be lucky next time."

dice1 = random.randint(1, 6) # 1 <= dice <= 6
dice2 = random.randint(1, 6) # 1 <= dice <= 6

print('サイコロを２回振ります')
input('１回目です。意気込みをどうぞ！>')
print("the number of the dice is", dice1)
input('２回目です。意気込みをどうぞ！>')
print("the number of the dice is", dice2)

challenge = YuriPythonProject5no5()
challenge.first = dice1
challenge.second = dice2
print(challenge.checktheluck())

# サイコロを２回振ります
# １回目です。意気込みをどうぞ！>a
# the number of the dice is 5
# ２回目です。意気込みをどうぞ！>a
# the number of the dice is 5
# Yay! You are lucky!