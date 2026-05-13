"""Student Report Card System

Take:

student name
5 subject marks

Print:

total
average
grade
"""

student_name=["Amey"]
sub_marks1=["chem:",67]
sub_marks2=["phy:",90]
sub_marks3=["robotics:",99]
sub_marks4=["maths:",98]
sub_marks5=["programming:",80]




total=sub_marks1[1]+sub_marks2[1]+sub_marks3[1]+sub_marks4[1]+sub_marks5[1]


average=(sub_marks1[1]+sub_marks2[1]+sub_marks3[1]+sub_marks4[1]+sub_marks5[1])/5


grade=(average==86.8 and "Grade A"  or "Fail")

"""
This is my first Python project after learning the basics of strings,
 variables, data types, lists, and tuples.
  I created this project to practice and improve 
  my understanding of these fundamental 
  Python concepts.
"""

print(total,average,grade)
