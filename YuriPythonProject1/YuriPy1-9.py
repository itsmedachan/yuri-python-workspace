# Prove the following formula
# cos(α) + cos(β) = 2cos1/2(α+β)cos1/2(α-β)

import math

str_α = input("input α:")
α = float(str_α)

str_β = input("input β:")
β = float(str_β)

sum = math.cos(α) + math.cos(β)
print(sum)

prod = 2 * math.cos((α+β)/2) * math.cos((α-β)/2)
print(prod)

print(sum==prod) # True