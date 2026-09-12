## IMPORTS GO HERE
import math
## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(student_record):
    if student_record == None:
        return None
    if student_record == []:
        return []
    comulative_marks = []
    for student in student_record:
        roll_no = student[0]
        name = student[1]
        total_marks = 0
        for marks in student[2:]:
            if marks != None:
                total_marks = total_marks + marks
        comulative_marks.append(( roll_no, name, total_marks))
    return comulative_marks

#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(student_record):
    if student_record == None:
        return None
    if len(student_record) == 0:
        return None
    student_marks = find_cumulative_marks(student_record)

    max_marks = 0
    for record in student_marks:
        marks = record [2]
        if marks > max_marks:
            max_marks = marks
    top_student = []
    for record in student_marks:
        roll_no = record[0]
        name = record[1]
        marks = record[2]
        if marks == max_marks:
            top_student.append((roll_no, name))
    if len(top_student) == 1:
        return top_student[0] 
    else:
        return top_student
         


#### End OF MARKER





if __name__ == '__main__':
    results = [
   
    ("p101111", "Ali Khayam", 64, 10),
    ("p101112", "Mudasser Farooq", 50, 24),
    ("p101113", "Tamleek Ali", 10, 20)  
    ]

    print( find_cumulative_marks(results))
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print (find_top_student(results))
    # output: ('p101111', 'Ali Khayam')
