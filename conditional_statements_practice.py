# 1. Smart Traffic Signal

signal = input("Enter signal color (red/yellow/green): ")
emergency = input("Is emergency vehicle approaching? (True/False): ")
emergency = emergency == "True"

if emergency:
    print("Override signal for emergency vehicles")
elif signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Slow down")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal color")

# 2.Loan Eligibility Checker

name=input("enter your name:")
age=int(input("enter your age"))
credit_score=750

if age>=21 and credit_score>=750:
    print("you are eligible for loan")
else:
    print("you are not eligible for loan")

# 3.  Triangle Type Identifier

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
elif side1 != side2 and side2 != side3 and side1 != side3:
    print("Scalene Triangle")
else:
    print("Invalid input")

# 4.Electricity Bill Slab Logic

units = int(input("Enter the number of units consumed: "))

if units<=100:
    print("your electricity bills is 0")
elif units>100 and  units<=300:
    print("your electricity bills is ",units*5)
else:
    print("your electricity bills is ",units*10)

# 5.Exam Result Analyzer

marks = int(input("Enter your marks: "))

if marks>=75:
    print("distinction")
elif marks>=60 and  marks<75:
    print("first class")
elif marks>=50 and marks<60:
    print("second class")
elif marks>=35 and marks<50:
    print("pass")
else:
    print("fail")