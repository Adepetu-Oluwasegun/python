# with a class you can essentially define your own datatypes. a class is an overview of what a datatype is
# creating a class called student
class Student:

  def __init__(self, name, course, gpa, is_on_probation, year_of_study): 
    self.name = name
    self.course = course
    self.gpa = gpa
    self.is_on_probation = is_on_probation
    self.year_of_study = year_of_study

  def on_hon_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      False