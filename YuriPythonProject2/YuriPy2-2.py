str_weight = input("Tell me your weight(kg): ")
weight = int(str_weight)

str_height = input("Tell me your height(m): ")
height = int(str_height)

if height > 3
  print("Please change the unit from 'cm' to 'm'")
  str_height = input("Tell me your height(m): ")
  height = int(str_height)
end

BMI = weight / ( height * height )
print("Your BMI is: ", BMI)
