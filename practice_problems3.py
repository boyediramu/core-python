# # 1 Print Numbers from 1 to n
# n=5
# for i in range(1,n+1):
#     print(i)

# # 2 Print Numbers from m to n
# n1=3
# n2=7
# for i in range(n1,n2+1):
#    print(i)

# # 3 Print Numbers from n to 1 in Reverse
# num=5
# for i in range(num,0,-1):
#     print(i)

# # 4 . Print Numbers from n to m in Reverse
# num1=10
# num2=6
# for i in range(num1,num2-1,-1):
#     print(i)

# 5 . Sum of n Natural Numbers
# number=int(input("enter a number"))
# sum=0
# for i in range(1,number+1):
#     sum=sum+i
#     # print(f"{i}",end=" ")
# print(sum)

# 6 Factorial of a Number
# number1=int(input("enter a number"))
# product=1
# for i in range(1,number1+1):
#     product=product*i
# print(product)

#  7 Sum of m to n Numbers
# value=int(input("enter a 1st number: "))
# value1=int(input("enter a 2nd number"))

# sum=0
# for i in range(value,value1+1):
#     sum=sum+i
# print(sum)

# 8 product of m to n numbers
# val1=int(input("enter a 1st number"))
# val2=int(input("enter a 2nd number"))

# prod=1
# for i in range(val1,val2+1):
#     prod=prod*i
# print(prod)

# 9 Print Factors of a Number
# n=int(input("enter a number"))

# print(f"factors of {n} is")

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
    
# 10 count factors

# n2=int(input("enter a number"))
# count=0
# for i in range(1,n2+1):
#     if n2%i==0:
#         count=count+1
# print(count)

# 11 prime number
# n3=int(input("enter a number"))

# count=0
# for i in range(1, n3+1):
#     if n3%i==0:
#         count=count+1
# if count==2:
#     print("prime number")
# else:
#     print("not a prime number")

# 12 even numbers from m to n
# m=int(input("enter a number"))
# n=int(input("enter a number"))

# count=0

# for i in range(m,n+1):
#     if i%2==0:
#         print(i)
#         count=count+1
# print("total even numbers are", count)

# 13 odd numbers from m  to n
# m1=int(input("enter a start number"))
# n1=int(input("enter a end number"))

# count1=0
# for i in range(m1,n1+1):
#     if i%2!=0:
#         print(i)
#         count1=count1+1
# print("total odd numbers are", count1)

# 14
m4=int(input("enter a start number"))
n4=int(input("enter a  end number"))

count=0
for i in range(1,n4+1):
    if n4%i==0:
        count=count+1
    elif n4%i!=0:
        count=count+1
print(count)


        

