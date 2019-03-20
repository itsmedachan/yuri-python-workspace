str_score = input("Input your score: ")
score = int(str_score)

if score >= 90:
  grade = "A"
  comment = "Excellent"
elif score >= 80:
  grade = "B"
  comment = "Very good"
elif score >= 70:
  grade = "C"
  comment = "Good"
elif score >= 60:
  grade = "D"
  comment = "You can do better"
else:
  grade = "F"
  comment = "ナマケモノ"

print("Your grade is: ", grade)
print(comment)