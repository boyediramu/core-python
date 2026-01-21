# # math operations
# x=10
# y=5
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**y)

# # type conversion
# x="10"
# y=int(x)
# z=5
# print(type(y))
# print(y+z)

# # numbers from user input
# a=int(input("enter a 1st number"))
# b=int(input("enter a 2nd number"))
# print("the sum both two numbers is",a+b)

# # boolean with numbers 
# a=10
# b=20
# greater=a>b
# print(greater)

# challange
# a=int(input("enter the first number "))
# b=int(input("enter the second number"))
# print("the sum is",a+b)
# print("the difference is",a-b)
# print("the product is",a*b)
# if (a>b):
#     print("first number is greater")
# else:
#     print("second number is greater")


# student result analyzer
name=input("enter your name")
pin=int(input("enter your roll no."))

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

for i in each_subjects_marks:
    print(i)
    
print("total obtained marks",total)
print("percentage scored",percentage)
 
if(is_pass):
    print("status     :pass")
else:
    print("status     :fail")
 