class Student():
  student_list = []
  def __init__(self): 
    self.name = name
    print("registered {} to the student list".format(self.name))

  def cal_num_of_students(self):
    return len(Student.student_list)

  def output_student_list(self):
    print("Student list has {} students.".format(self.cal_num_of_students()))
    for name in Student.student_list:


s1 = Student()
s1.name = "Taro"
s2 = Student()
s2.name = "Jiro"
s2.output_student_list()