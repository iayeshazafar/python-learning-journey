## IMPORTS GO HERE
import math 
## END OF IMPORTS


def get_point(grade):
     if grade == "A" or grade == "A+":
          return 4.00
     elif grade == "A-":
          return 3.67
     elif grade == "B+":
          return 3.33
     elif grade == "B":
          return 3.00
     elif grade == "B-":
          return 2.67
     elif grade == "C+":
          return 2.33
     elif grade == "C":
          return 2.00
     elif grade == "C-":
          return 1.67
     elif grade == "D+":
          return 1.33
     elif grade == "D":
          return 1.00
     else :
          return 0.00


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def valid_grade(grade_list):
     possible_grade = ["A+","A","A-","B+","B","B-","C+","C","C-","D+","D"]
     for i in grade_list:
          if i not in possible_grade:
               return False
          return True
def calculate_sgpa(grade_list):
    if grade_list  == None:
         return None
    if  not  valid_grade(grade_list):
         return None
    total_marks = 0 
    total_subject = 0
    for i in grade_list:
        if i != "nothing":
            total_subject = total_subject + 1 
            total_marks = get_point(i) + total_marks
            
    
    if total_subject == 0:
             return 0
        
    s_gpa = total_marks / total_subject 
    return s_gpa
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(grade_list1 , crd_hrs_list):
    if grade_list1  == None or crd_hrs_list == None:
        return None
    if  not  valid_grade(grade_list1):
        return None
    if len(grade_list1) != len(crd_hrs_list):
        return None
    total_credits = 0
    weight_sums = 0
    i = 0
    while i < len(grade_list1):
        grade = grade_list1[i]
        credit_hours =crd_hrs_list[i]
        grade_points = get_point(grade)

        total_credits = total_credits +(grade_points * credit_hours)
        weight_sums = weight_sums + credit_hours
        i = i + 1

    if weight_sums == 0:
         return None

    sgpa = total_credits / weight_sums
    return sgpa
     
     

#### End OF MARKER


if __name__ == '__main__':
    print (calculate_sgpa(["A+", "B", "B+"]))
    print (calculate_sgpa_weighted(['A+'], [4]))
