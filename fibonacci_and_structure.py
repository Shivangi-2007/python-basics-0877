# Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Structure-like class

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


print("\n\nStudent Details")

name = input("Enter name: ")
roll_no = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

s = Student(name, roll_no, marks)

print("Name:", s.name)
print("Roll No:", s.roll_no)
print("Marks:", s.marks)
