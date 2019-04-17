# wip
def cal(n):
  i = 0
  num = 0
  while i < n:
    num += n%2*(10**i)
    n = n//2
    if n == 1:
      