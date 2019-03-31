# guess the number! ref: https://doc.rust-jp.rs/the-rust-programming-language-ja/1.6/book/guessing-game.html

import random

print("Guess the number!")
print("The number is between 1 and 10 (integer)")
str_your_num = input("Please input your guess:")
your_num = int(str_your_num)

answer = random.randint(1, 10) # 1 <= answer <= 10

if your_num < answer:
  print("Your number is too small.")
elif your_num > answer:
  print("Your number is too big.")
else:
  print("Congratulations! You are correct!")