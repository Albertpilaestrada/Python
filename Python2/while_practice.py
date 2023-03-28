import math
#part1

i=1

while i<=10:
    print("repit")
    i=i+1
print("the end")

#part2

edad=int(input("Enter your age: "))

while edad<5 or edad>100:
    print("Enter a real age please")
    edad=int(input("Enter your age: "))

print("Thanks can pass")

#part3

num=int(input("enter a number"))
trys=0

while num<0:
    print("you can't find the square root of a negative number, dummy")
    trys=trys+1

    if trys==3:
        print("NO more trys, dummy")
        break
    num=int(input("enter a number"))
    
if trys<3:
    result=math.sqrt(num)
    print("The sqare root of "+str(num)+" is "+str(result))