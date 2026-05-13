#  Mini Project: Student Info Card

# Taking input from user
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
favorite_subject = input("Enter favorite subject: ")

# Storing data in dictionary
student = {
    "Name": name,
    "Age": age,
    "Marks": marks,
    "Favorite Subject": favorite_subject
}

# Checking result
if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

# Printing Student Card
print("\n----- STUDENT CARD -----")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Marks:", student["Marks"])
print("Favorite Subject:", student["Favorite Subject"])
print("Result:", result)