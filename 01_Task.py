a = input("Enter your Name: ")

def get_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter your Marks for {subject}: "))
            return marks
        except ValueError:
            print("Invalid input! Please enter numbers only.")

m1 = get_marks("subject1")
m2 = get_marks("subject2")
m3 = get_marks("subject3")
m4 = get_marks("subject4")
m5 = get_marks("subject5")

Total = m1 + m2 + m3 + m4 + m5
percentage = (Total / 500) * 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\nStudent Name:", a)
print("Total Marks:", Total)
print("Percentage:", percentage)
print("Grade:", grade)