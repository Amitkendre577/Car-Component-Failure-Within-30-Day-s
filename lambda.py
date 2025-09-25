# y=int(input("enter the number"))

# double =lambda z: z**5
# print(double(y))

# def Avg (x,y,z):
#     sum=x+y+z
#     avg=int((sum)/3)
#     return avg

# print(Avg(2,3,4))

# import math
# x=int(math.sqrt(64))
# y=math.factorial(10)
# z=math.gcd(10,12)
# print(x)
# print(y)
# print(z)

# x=45

# Write a program to check the datatype of variables using the type() function.
# x=6
# print(type(x))

# # Take user input and convert it into an integer using int() and print its type.
# m= (input("enter something"))
# print(type(int(m)))

# Convert a floating-point number into a string using str() and verify its datatype.
# b=0.9
# print(type(str(b)))

# Use isinstance() to check if a variable is of type list.
# x=[1,2,3,4]
# print(isinstance(x,list))

# Convert a list into a tuple using the tuple() function and display the result.
# list=[1,2]
# print(tuple(list))

# Write a program that converts a number (int/float) into a complex number using the complex() function.
# x=5
# print(complex(x))

# Use the dict() function to convert a list of key-value pairs into a dictionary.
# x=[(1,"a"),(2,"b")]
# print(dict(x))  

# Take a string containing numbers (e.g., "12345") and use int() and float() to convert it into numeric datatypes.
# x="12345"
# print(int(x),",",float(x))

# Check whether a variable is None using the is keyword and type() function.
# x=None
# print(type(x))

# Convert a set into a list using the list() function and remove duplicates from a list using set().
# set1={1,2,3}
# print(list(set1))

# my_list = [1, 2, 2, 3, 3, 3, 4]
# unique_no=list(set(my_list))
# print(unique_no)

# Write a program that takes a mixed list and separates integers, floats, and strings using isinstance().
# a=[1,2.0,'A']
# str=""
# int1=0
# float=0.0

# for i in range (len(a)):
#     if isinstance(len(a) ,int)==True:
#         len(a).append in int1

# Use the bytes() and bytearray() functions to convert a string into bytes and display their types.

# Write a program that uses the frozenset() function and demonstrates that it is immutable.

# Use the ord() and chr() functions to convert characters into their ASCII values and back.

# Demonstrate how to use the memoryview() function with a bytearray and display its datatype.
# a=[1,3,4,2,5,6]
# b=a.sort(reversed=True)
# print(b)


# Basic Level (5 Questions)
# Check Number Type:
# Write a program that takes a number as input and prints whether it is positive, negative, or zero.
# a=int(input("Number"))

# if a<0:
#     print("Negative Number")
# elif a>0:
#     print("Positive Number")
# else:
#     print("Zero")




# Grade Calculator:
# Write a program that takes a student’s marks as input and prints the grade:

# A (marks ≥ 90)

# B (marks ≥ 75 and < 90)

# C (marks ≥ 50 and < 75)

# Fail (marks < 50)
# marks=int(input("Enter Number"))
# if  marks > 90:
#     print("A")
# elif marks > 75 and marks< 90 :
#     print("B")

# elif marks > 50 and marks < 75 :
#     print("c")
# else:
#     print("PLease enter the valid input !")



# # Even, Odd, or Multiple of 5:
# # Take an integer as input.
# num=int(input("Enter"))
# # If it is even and a multiple of 5, print "Even and Multiple of 5".
# if num%2==0 and num%5==0:
#     print("Enven and Multiple of 5")
# # If it is even but not a multiple of 5, print "Even only".
# elif num%2 and num %5!=0:
#     print("Enven Only")
# # If it is odd, print "Odd".
# elif num%2!=0:
#     print("odd")

# # Temperature Category:
# # Ask the user for temperature in Celsius and print:
# temp=float(input("Enter"))
# # "Cold" if temp < 15
# if temp<15:
#     print("Cold")
# # "Warm" if temp is between 15 and 30
# elif temp >15 and temp <30:
#     print("Warm")
# # "Hot" if temp > 30
# elif temp>30:
#     print("Hot")


# # Voting Eligibility:
# # Write a program that checks if a person is eligible to vote:
# age=int(input("Enter"))
# # Age < 18: "Not eligible"
# if age <18:
#     print("Not eligible")
# # Age between 18 and 60: "Eligible"
# elif age >18 and age <60:
#     print("Eligible")
# # Age > 60: "Eligible with senior benefits"
# elif age >60 :
#     print("eligible with senior")

# Intermediate Level (5 Questions)
# Leap Year Checker:
# Take a year as input and check if it is a leap year:
# year=int(input("Enter"))

# if year % 400==0 or (year % 4==0 and  year % 100!=0):
#     print("leap_year")
# else :
#     print("Not_leap")


# Movie Ticket Pricing:
# Ask the user for age and day (weekday/weekend).

# Age < 12 → ₹150 (weekday) or ₹200 (weekend)

# Age 12–60 → ₹250 (weekday) or ₹300 (weekend)

# Age > 60 → ₹100 (weekday) or ₹150 (weekend)
# age = int(input("Enter age: "))
# day = input("Enter day (weekday/weekend): ").lower()

# if age < 12 and day == "weekday":
#     print("Rs.150")
# elif age < 12 and day == "weekend":
#     print("Rs.200")
# elif (age >= 12 and age <= 60) and day == "weekday":
#     print("Rs.250")
# elif (age >= 12 and age <= 60) and day == "weekend":
#     print("Rs.350")
# elif age > 60 and day == "weekday":
#     print("Rs.250")
# elif age > 60 and day == "weekend":
#     print("Rs.300")
# else:
#     print("Invalid Input")



# BMI Calculator:
# Input weight (kg) and height (m) and calculate BMI = weight / (height²).

# BMI < 18.5 → "Underweight"

# 18.5 ≤ BMI < 24.9 → "Normal weight"

# 25 ≤ BMI < 29.9 → "Overweight"

# BMI ≥ 30 → "Obese"

# Electricity Bill Calculation:
# Take number of units consumed and calculate:

# Up to 100 units: ₹5/unit

# 101–200 units: ₹7/unit

# Above 200 units: ₹10/unit

# Triangle Type:
# Take 3 side lengths as input and print the type of triangle:

# If all sides are equal → "Equilateral"

# If two sides are equal → "Isosceles"

# If all sides different → "Scalene"