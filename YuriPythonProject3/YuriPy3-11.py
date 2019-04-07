import math

print('πを求めます')
print('π = 4Σ[k=0→∞]((-1)^k)/(2k+1)')

n = int(input('please input n :'))

s = 0
k = 0
while k <= n:
  s += 4 * ( math.pow(-1,k) / (2*k + 1) )
  k += 1

print('π =',s)

# πを求めます
# π = 4Σ[k=0→∞]((-1)^k)/(2k+1)
# please input n :100000
# π = 3.1416026534897203