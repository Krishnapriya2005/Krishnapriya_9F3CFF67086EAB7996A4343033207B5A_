class Student:
  def _init_(self, name, roll_number, cgpa):
   self.name = name 
   self.roll_number = roll_number
   self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list,key=lambda student: 
                                student.cgpa,reverse = True)
  return sorted_students
students = [ Student("prabha","5052",7.8),
               Student("hanish","5051",8.9),
               Student("jaya","5040",7.0),
               Student("nithya","5045",6.0),
               Student("sowmiya","5060",8.5),
               Student("kiruthi","5030",7.5)
             ]
sorted_students = sort_students(students)
print("\n\n")
print(" ****************** ")
print("\tNAME \t\t\t\t REGNO \t\t\t PERCENTAGE ")
print(" ****************** ")
for student in sorted_students:
  print("Name: {}, \t Roll Number: {}, \tCGPA: {}" .format(student.name, 
                                                    student.roll_number, student.cgpa))