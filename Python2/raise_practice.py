import math

#part1

def assesses_age(age):
    
    if age<0:
        raise TypeError("Negative age is not allowed")
    
    if age<20:
        return "You are very young"
    elif age<40:
        return "You are young"
    elif age<65:
        return "You are mature"
    elif age<100:
        return "Take care yourself"
    
#print(assesses_age(12))

#part2

def root_calc(num):
    if num<0:
        raise ValueError("The number cannot be negative")
    else:
        return math.sqrt(num)
    
op1=int(input("Enter a number: "))

try:
    print(root_calc(op1))
except ValueError as negativenumbererror:
    print(negativenumbererror)

print("Program ended")