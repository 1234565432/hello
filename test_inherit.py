class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def showinfo(self):
        print('this string is from parent', self.name, self.age)
class Child(Parent):
    def __init__(self, name, age, toy_number):
        Parent.__init__(self, name, age)
        self.toynumber = toy_number
    def child_showinfo(self):
        print('this is from child class', self.toynumber)
zhouyunqaing = Child('zhouyunqiang', 24, 5)
zhouyunqaing.showinfo()
zhouyunqaing.child_showinfo()
