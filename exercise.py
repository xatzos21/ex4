#Task1-ex4
#Your task is to write a program which asks the user 
#two times about two integer numbers to compare. 

count = 1
while count <= 2:

    x =int(input('Enter first number:'))
    y =int(input('Enter second number:'))
    if x < y:
        print('Second number is greater than the first')
    if x != y:
        print ('Numbers are not equal')
    if x <= y:
        print("Second number is greater than or equal to first number")
    if x or y >= 1000:
        print("Big numbers")

    count += 1


    #Task2-ex4
    #Your task is to write a Python program to convert 
    #month name to a number of days. 
    

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
x = str(input("Input the name of Month:"))
if x == str("January" or "March"or "May" or "July" or "August" or "October" or "December"):
    print("Number of days: 31 days")
elif x == str("April" or "June" or "September" or "November"):
    print("Number of days: 30 days")
else:
    print("Number of days: 28 days")