# ref: https://homepage45.net/unit/discomfort.htm
# 不快指数 DI = 0.72 x (Td + Tw) + 40.6  [Td:乾球(℃), Tw:温球(℃)]
# 不快指数 DI = 0.81xT+0.01U(0.99T-14.3)+46.3  [T:気温(℃), U:湿度(%)]

def calculate_discomfort_index(t, u):
  di = 0.81*t + 0.01*u*(0.99*t - 14.3) + 46.3
  return di


print('不快指数を計算します')
temp = float(input("気温を入力してください(℃): "))
humid = float(input("湿度を入力してください(%): "))

print(calculate_discomfort_index(temp, humid))