# # 01 check even or odd
# num=6
# if(num%2==0):
#     print("even")
# else:
#     print("odd")

# # 02 divisible by 5 but not by 10
# number=25
# if(number%5==0 and number%10!=0):
#     print("the number is divisible by 5 but not by  10")
# else:
#     print("the number is not divisible by 5  and 10")

# # 03 biggest among two numbers
# a=4
# b=7
# if(a>b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# # 04 smallest among two numbers
# num1=4
# num2=7
# if(num1<num2):
#     print("num1 is smaller than mum2")
# else:
#     print("num2 is smaller than num2")

# # 05 divisible by 2,3 and 6
# n=18
# if(n%2==0 and n%3==0 and n%6==0):
#     print("the number is divisible by 2,3 and 6")
# else:
#     ("the number is not divisible")

# # 06 vote eligibility
# age=19
# if(age>=18):
#     print("your eligible for vote")
# else:
#     print("your not  eligible for vote")

# # 07 student pass/fail based on all subjects>=35
# maths=40
# physics=36
# chemistry=30

# if(maths>=35 and physics>=35 and chemistry>=35):
#     print("you passed")
# else:
#     print("you failed")

# # 08 student passes if he passes in at least 2 subjects
# maths=40
# physics=36
# chemistry=30

# pass_count=0
# if(maths>=35):
#     pass_count+=1
# if(physics>=35):
#     pass_count+=1
# if(chemistry>=35):
#     pass_count+=1

# if(pass_count>=2):
#     print("passed")
# else:
#     print("failed")

# l=[23,65,83,1,46,86,78,76,45,55,23,90,49,50]

# for i in range(0, len(l)):
#     if l(i)>50:
#         print(i)




# problem on finding areas and perimeters of square,rectangle and triangle

choose=int(input("enter 1 for square 2 for rectangle 3 for triangle"))

if choose==1:
    side= float(input("enter side"))
    area_of_square=side*side
    perimeter_of_square=4*side
    print("Area of square is",area_of_square)
    print("Perimeter of square is",perimeter_of_square)

elif choose==2:
    length=float(input("enter length"))
    breadth=float(input("enter breadth"))
    area_of_rectangle=length*breadth
    perimeter_of_rectangle=2*(length+breadth)
    print("Area of rectangle is",area_of_rectangle)
    print("Perimeter of rectangle is",perimeter_of_rectangle)

elif choose==3:
    side1=float(input("enter side1"))
    side2=float(input("enter side2"))
    side3=float(input("enter side"))
    area_of_triangle=0.5*side1*side2
    perimeter_of_triangle=side1+side2+side3
    print("Area of triangle is",area_of_triangle)
    print("Perimeter of triangle is",perimeter_of_triangle)
else:
    print("invalid input")


# problem on finding currency break down and time conversion

choose=int(input("Enter choice:\n"
                  "1 for currency break down\n"
                 "2 for time conversion\n"))


if choose==1:
    amount=int(input("enter amount"))
    notes_1000=amount//1000
    remaining_amount=amount%1000
    notes_500=remaining_amount//500
    remaining_change=remaining_amount%500

    print("1000 notes:",notes_1000)
    print("500 notes:",notes_500)
    print("Remaining Amount:",remaining_change)

elif choose==2:
    total_seconds=int(input("enter seconds\n"))

    hours=total_seconds//3600
    remaining_seconds=total_seconds%3600
    minutes=remaining_seconds//60
    seconds=remaining_seconds%60

    print(hours,"Hours")
    print(minutes,"Minutes")
    print(seconds,"Seconds")

else:
    print("Choose a valid option")

# problem on finding student total marks and average of marks

name=input("enter your name\n")
pin=int(input("enter your roll no.\n"))

java=35
python=45
cpp=50
each_subjects_marks=('java:',java,'python:',python,'C++',cpp)

total=java+python+cpp
percentage=total/3
is_pass=percentage>=35

print("student name",name)
print("student roll no",pin)

print("marks obtained in each subject")

print("Java:",java,"Python:",python,"C++:",cpp)
    
print("total obtained marks",total)
print("percentage scored",percentage)
 
if(is_pass):
    print("status:pass")
else:
    print("status:fail")
 


