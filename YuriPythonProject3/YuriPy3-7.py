import math

# ref: http://tarohere.com/archives/938
print("二桁の数を当てるゲームをします")
your_num = int(input('二桁の数を入力してください :'))
print('その数字に7333を足します')
print(str(your_num+7333))
print('その数を3倍にします')
print(str((your_num+7333)*3))
print('その平方根をとります')
print(str(math.sqrt((your_num+7333)*3)))
guess_num = int(input('その小数点以下一桁めと二桁めを並べた二桁の数を教えてください :'))
print('考え中.....')

if guess_num < 32:
  guess_num += 100

answer = guess_num - 32

print('Your number is '+str(answer)+' !')

# 二桁の数を当てるゲームをします
# 二桁の数を入力してください :30
# その数字に7333を足します
# 7363
# その数を3倍にします
# 22089
# その平方根をとります
# 148.62368586466962
# その小数点以下一桁めと二桁めを並べた二桁の数を教えてください :62
# 考え中.....
# Your number is 30 !