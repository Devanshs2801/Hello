""""str() In class Python"""
""""class Person:devash
  def __init__(self, name,rollno):
    self.name = name
    self.rollno = rollno
  def __str__(self):
    return f"{self.name},{self.rollno}"    
p1 = Person("Devansh",25)
p2 = Person("Himanshu",18)
print(p1)
print(p2)"""

class school:
    def __init__(self, name,rollno):
      self.name = name
      self.rollno = rollno
    def display(self):
        print(self.name,self.rollno)
class standard(school):
    pass
x=standard("Devansh",25)
x.display()
