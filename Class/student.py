# with a class you can essentially define your own datatypes. a class is an overview of what a datatype is
# creating a class called student
class Student:

  def __init__(self, name, major, gpa, is_on_probation): 
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation