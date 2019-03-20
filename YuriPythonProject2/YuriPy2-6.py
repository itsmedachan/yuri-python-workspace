str_temperature = input("What is the temperature today? (celsius) : ")
temperature = int(str_temperature)

if temperature >= 27:
  message = "It's hot today."
elif temperature >= 20:
  message = "It's warm and pleasant today."
elif temperature >= 14:
  message = "It's coolish today."
else:
  message = "It's cold today."

print(message)