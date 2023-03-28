#part1

for i in [1,2,3]:
    print("Hi")

#part2

#email=False
count=0
my_email=input("enter an email: ")

#for i in "vikingo@gmail.com":
for i in my_email:
    if (i=="@" or i=="."):
        count=count+1

#if email==True:
if count==2:
    print("email correct")
else:
    print("email incorrect")

#part3

for i in range(5):
    #print(i)
    #print("hola")
    print(f"variable value {i}")
    
#part4

valid=False

email=input("enter an email: ")

for i in range(len(email)):
    if email[i]=="@":
        valid=True

if valid:
    print("email correct")
else:
    print("email incorrect")
