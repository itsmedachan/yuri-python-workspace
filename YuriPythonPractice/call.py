import myCalc.calculate as cal
# import パッケージ名.モジュール名 as 省略形
# パッケージ名はディレクトリ名
# モジュール名はファイル名から.pyを除いたもの

a=1
b=2
print("a={}, b={}".format(a,b))
print("a+b={}".format(cal.sum(a,b)))
print("a-b={}".format(cal.diff(a,b)))
print("a*b={}".format(cal.prod(a,b)))
print("a/b={}".format(cal.quot(a,b)))

# Yuris-MacBook-Pro:YuriPythonProject8 yuri$ python call.py
# a=1, b=2
# a+b=3
# a-b=-1
# a*b=2
# a/b=0.5