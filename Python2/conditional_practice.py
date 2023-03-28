#part4

print("Optative subject: Graphics Informatics - Software Test - Usability and Stability")
subject=input("Choose your optative subject")

subject=subject.lower()

if subject in ("graphics informatics","software test","usability and stability"):
    print("Chosen subject"+subject)
else:
    print("The chosen subject is not on the list")


#part3

school_dist=int(input("enter your distance to school in km: "))
num_brethren=int(input("enter the number of brethren in the school: "))
family_salary=int(input("enter your total family salary: "))

#if school_dist>40 and num_brethren>2 and family_salary<=20000:
if school_dist>40 and num_brethren>2 or family_salary<=20000:
    print("You can have a scholarship")
else:
    print("you can't have a scholarship")

#2part

ceo_salary=int(input("Introduce the ceo salary: "))
print("CEO Salary is: "+str(ceo_salary))

dir_salary=int(input("Introduce the dir salary: "))
print("Dir Salary is: "+str(dir_salary))

leader_salary=int(input("Introduce the leader salary: "))
print("Leader Salary is: "+str(leader_salary))

employe_salary=int(input("Introduce the employe salary: "))
print("Employe Salary is: "+str(employe_salary))

if employe_salary<leader_salary<dir_salary<ceo_salary:
    print("All seems normal")
else:
    print("Something smells bad")

#1part

age=7

if 0<age<100:
    print("Correct age")
else:
    print("Incorrect age")