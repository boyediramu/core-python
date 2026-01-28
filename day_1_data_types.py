# # '''primitive data types''' 
# # integer
# a=10 
# b=20
# print("the sum of two numbers is",a+b)

# # float
# price=99.99
# print("the price is",price)

# # string
# name="ram"
# print("my name is ",name)

# # boolean
# x=True
# print(type(x))

# result=10>5
# print(result)

# # integer + string
# age=25
# print("im",age," years old")

# # None type
# data=None
# print(type(data))

# # '''practice set'''
# # problem solving
# name=input("enter your name")
# age=int(input("enter your age"))
# print(f"hello {name} your age is {age}")

# # even or odd
# num=int(input("enter a number"))
# if num%2==0:
#     print("the number is even")
# else:
#     print ("the number is odd")

# # to check is the number is positive or negative or zero
# num=int(input("enter a number"))
# if num>0:
#     print("the number is positive")
# elif(num<0):
#     print("the number is negative")
# else:
#     print("the number is zero")

# # vote eligibility
# age=int(input("enter your age"))
# if age>=18:
#     print("your eligible for  vote")
# else:
#     print("your not eligible for vote")

# # simple calculator
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# print("sum of",a+b)
# print("difference of",a-b)
# print("product of ",a*b)
# print("division of",a/b)

# # string length and type
# name=input('enter any text to find  length and its type')
# print(len(name))
# print(type(name))

# # swap of two number 
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# a, b = b, a

# print("After swap:")
# print("a =", a)
# print("b =", b)

# # type conversion
# a=input("enter a number")
# b=int(input("enter a number"))
# print(type(a))
# print(type(b))
# print(str(a)+str(b))

# # age category
# age=int(input("enter your age"))
# if(age>13):
#     print("child")
# elif(age<=19):
#     print("teenager")
# elif(age<=59):
#     print("adult")
# else:
#     print("senior citizen")

# # student grade system
# name=input("enter your name")
# id=int(input("enter your roll number"))

# print("each subject marks")

# java=int(input("enter your java marks"))
# python=int(input("enter your python marks"))
# cpp=int(input("enter your c++ marks"))

# print("java=",java,"python=",python,"cpp=",cpp)

# total=java+python+cpp
# print("your total marks is",total)

# marks=int(input("enter your total  marks to know your grade"))

# if(marks>=90):
#     print("grade A")
# elif(marks>=75):
#     print("grade B")
# elif(marks>=50):
#     print("grade C")
# else:
#     print("fail")

# # login validation
# username="ram"
# password="1235"

# user=input("enter your username")
# passw=input("enter your password")

# if(username==user and password==passw):
#     print("login successful")
# else:
#     print("invalid credentials")
    
# # salary tax
# salary=float(input("enter your salary"))
# if(salary<=25000):
#     tax=0
# elif(salary<=50000):
#     tax= salary*0.5
# else:
#     tax=salary*0.8

# print("your tax is", tax)

# # finding indexing value  and printing indexing word by using for loop
# # used to find big sentence and  paragraphs without counting words
# s="python is very easy to learn and understand "
# y=(s.split())# converts string to list 
# print(y)
# print(len(y))
# for i in range(0,8):# range of list
#     print(i,y[i])
# print(y[3])

# '''non primitive data types'''

# list
# numbers=[1,2,8,10,15] # list
# name="python is very easy to learn "# string
# fruits=["appale","banana","orange"]# list
# fruits.append("mango")# for updating the list 
# fruits.remove("banana")# remove the value from list
# print(fruits)
# print(type(numbers))# to know the type of variable
# print(len(numbers)) # to know the length of list
# print(numbers[2]) # to print particular index value in list
# print(numbers)# printing the whole list
# print(name.split)# converting string to list


# # using for loop in list
# nums=[2,5,3]
# print(nums)
# for i in nums:
#     print(i*2)

# #using conditional statements in list
# colors=["red","green","blue","yellow"]

# if "black" in colors:
#     print("yes blue is present in list")
# elif "red" in colors:
#     print("yes red is present in list")
# else:
#     print("no color found")

# tuple
colors = ("red", "green", "blue")
n= (1,5,9,3,6,6)
print(colors[1])
print(n)
print(colors)

#set
ids={1,2,2,3,5,9,8}#ordered and not allow duplicates
print(ids)

#dictionary
student={
    "name":"ram",
    "age":25,
    "college":"vmeg"
}
print(student)
print(student["name"])
print(len(student))





