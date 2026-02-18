# 1. Write a Python program that takes five different values as input (integer, float, string, boolean, and list) and prints the datatype of each value.

n1=25
n2=25.9
n3="ram"
n4=True
n5=[1,2,3,4,5]
print(type(n1))
print(type(n2))
print(type(n3))
print(type(n4))
print(type(n5))

# 2. Write a Python program to swap the values of two variables without using a third variable using a third variable Display the values before and after swapping.

num1=25
num2=56
print("before swapping", num1, num2)
num1= num1+num2
num2=num1-num2
num1=num1-num2
print("after swapping",num1,num2)

# 3. Type Conversion Challenge Write a Python program that: takes an integer and a float as input converts the integer to float converts the float to integer prints the converted values and their datatypes 

integer=12
floatt=12.9

number1=float(integer)
number2=int(floatt)

print(number1)
print(number2)

print(type(number1))
print(type(number2))

# 4.Arithmetic Operations with Variables

var1=15
var2=20
print(var1+var2)
print(var1-var2)
print(var1*var2)
print(var1/var2)
print(var1//var2)
print(var1%var2)

# 5. String and Numeric Variable Combination

name="ram"
age=25
print(f"my name is {name} and my age is {age}")