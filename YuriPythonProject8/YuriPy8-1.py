class People():
  visitor = 0 # クラス変数
  def __init__(self): 
    People.visitor += 1
    self.name = '' # インスタンス変数

  def echo_name(self):
    print("Hello, I am {}.".format(self.name))  # 文字列.format(変数)
    print("\t You are the {}th visitor.".format(People.visitor))


student1 = People()
student1.name = "Taro"
student1.echo_name()

student2 = People()
student2.name = "Jiro"
student2.echo_name()