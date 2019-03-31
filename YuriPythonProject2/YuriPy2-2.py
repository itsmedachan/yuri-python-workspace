str_weight = input("Tell me your weight(kg): ")
weight = float(str_weight)

str_height = input("Tell me your height(m): ")
height = float(str_height)

if height > 3:
  print("Please change the unit from 'cm' to 'm'")
  str_height = input("Tell me your height(m): ")
  height = float(str_height)

BMI = weight / ( height * height )
print("Your BMI is: ", BMI)
