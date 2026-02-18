# name=input("enter your name")
# id=int(input("enter your roll number"))
# marks=int(input("enter your marks"))


# if(marks>=90):
#     print("you got grade A")
# elif(marks>=80):
#     print("you got grade B")
# elif(marks>=70):
#     print("you got grade c")
# else:
#     print("you failed")

# # problem on find even or odd number and prime number

# choose=int(input("Enter 1 for to find even or odd numbers\n" 
# "Enter 2 for to find prime numbers \n"))

# if choose==1:
#     num=int(input("enter a number\n"))
#     if(num%2==0):
#         print("The entered number is even")
#     else:
#         print("The entered number is odd")

# if choose==2:
#     number=int(input("enter a number\n"))
#     if(number<=1):
#         print("Please enter a number greater than 1")
#     else:
#         is_prime=True

#         for i in range(2,number):
#             if(number%i==0):
#                 is_prime=False
#                 break
#         if(is_prime):
#             print("The entered number is a prime number")
#         else:
#             print("The entered number is not a prime number")

# # problem on finding voting eligibility

# age=int(input("enter your age: "))

# if age>=18:
#     id=input("Do you have voter id (yes/No): ")
#     if id=="yes":
#         print("your are eligible follow the next steps")
        

#         print("Select party to confirm your vote\n")
#         print("1.BJP\n")
#         print("2.BRS\n")
#         print("3.CONG\n")
#         print("4.TDP\n")

#         party=int(input("please select party from above list:"))


#         if party==1:
#             print("your vote is confirmed")
#             print("Party:BJP")
#         elif party==2:
#             print("your vote is confirmed")
#             print("Party:BRS")
#         elif party==3:
#             print("your vote is confirmed")
#             print("Party:CONG")
#         elif party==4:
#             print("your vote is confirmed")
#             print("Party:TDP")

#         else:
#             print("invalid party selection")
#     else:
#         print("you are not eligible (NO VOTER ID)")
# else:
#     print("you are not eligible (BELOW 18 YEARS)")

# # problem on finding leap year

# year=int(input("enter a year:"))

# if year%4==0:
#     print("the year is leap year")
# else:
#     print("the year is not a leap year")

#   user loan eligibility
print("WELCOME TO HDB FINANCIAL SERVICES\n")
print(" SELECT YOUR LOAN TYPE\n")

print("1.Home loan\n")
print("2.Personal loan\n")
print("3. Car loan\n")

loan_type=int(input("enter your loan type: "))
name=(input("enter your name: "))
age=int(input("enter your age: "))
pan=input("enter your pan number: ")
aadhar=int(input("enter your aadhar number: "))
credit_score=int(input("enter your credit score: "))

if age>=21 and credit_score>=750:
    
    if loan_type==1:
        print("please wait  we are checking your eligibility...")
        print("you are eligible for home loan")
    elif loan_type==2:
        print("please wait  we are checking your eligibility...")
        print("you are eligible for personal loan")
    elif loan_type==3:
        print("please wait  we are checking your eligibility...")
        print("you are eligible for car loan")
    else:
        print("invalid Loan type")

else:
    print("your are not eligible for loan did not meet our criteria")


    










