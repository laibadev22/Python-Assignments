
a= input("Enter your Name: ")

m1=int(input("Enter your Marks for subject1: "))
m2=int(input("Enter your Marks for subject2: "))
m3=int(input("Enter your Marks for subject3: "))
m4=int(input("Enter your Marks for subject4: "))
m5=int(input("Enter your Marks for subject5: "))

Total= m1+m2+m3+m4+m5
percentage =(Total/500)*100

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


print("n\ Student Name: ",a)
print("Total Marks: ", Total)
print("percentage: ",percentage)
print("Grade:",grade)