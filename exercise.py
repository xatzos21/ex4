#Task1-ex4
#Your task is to write a program which asks the user 
# two times about two integer numbers to compare. 
 
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

