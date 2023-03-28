print("Access verification")

user_age=int(input("Introduce your age: "))

if user_age<18:
    print("Can't pass")
elif user_age>100:
    print("Don't lie")
else:
    print("Can pass")

student_note=int(input("Introduce your note: "))

if student_note<5:
    print("insufficient")
elif student_note<6:
    print("sufficient")
elif student_note<7:
    print("good")
elif student_note<9:
    print("notable")
else:
    print("outstanding")
