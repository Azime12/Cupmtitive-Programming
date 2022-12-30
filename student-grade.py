def gradingStudents(grades):
    # Write your code here
    grade=[]
    for i in grades:
        if i<38:
            grade.append(i)
        else :
            y=i%5
            if y>=3:
                grade.append(i+(5-y))
            else :
                grade.append(i)
    return grade      
