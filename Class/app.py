from student import Student

student1 = Student("fola", "computer science", 3.5, False, 4) #object student is the instance of class student
student2 = Student("shola", "chemistry", 1.5, True, 6)

print(student1.gpa)
print(student1.course)
print(student1.name)
print(student1.is_on_probation)
print(student1.year_of_study)
print(student1.on_hon_roll())
print(student2.on_hon_roll())