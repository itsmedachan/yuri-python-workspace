import math

print('I will convert your binary number into decimal number.')
bi_str = input('please input your binary number :')

length = len(bi_str)
i = 0
dec_num = 0
while i <= length-1:
  dec_num += int(bi_str[i]) * int( math.pow(2, length-1-i) )
  i += 1

print('The decimal number is',dec_num)

# I will convert your binary number into decimal number.
# please input your binary number :101
# The decimal number is 5