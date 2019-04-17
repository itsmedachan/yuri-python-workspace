class Person():
  def __init__(self): 
    self.name = 'Guest'
    self.age = 20

  def judge_age(self):
    if self.age >= 20:
      print("{} is an adult.".format(self.name))
    else:
      print("{} is not an adult yet.".format(self.name))


print("I will judge your age.")
person1 = Person()
person1.name = "Yuki"
person1.age = 25
person1.judge_age()

person2 = Person()
person2.name = "Masa"
person2.age = 18
person2.judge_age()

person3 = Person()
person3.name = "Nana"
person3.age = 20
person3.judge_age()