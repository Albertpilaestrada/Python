print("Student grade evaluation program")

studentnote=input()

def evaluation(note):
    assessment="Approved"
    if note < 5:
        assessment="Fail"
    return assessment

print(evaluation(int(studentnote)))