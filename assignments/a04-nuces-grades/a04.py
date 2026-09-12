## IMPORTS GO HERE
import math
## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
    
def get_grade(total_marks):
     if total_marks <= 0 or total_marks > 100:
          return None
     x = total_marks
     if   x >= 90:
          return  "A+"  
     elif x >= 86:
          return  "A"  
     elif x >= 82:
          return  "A-"  
     elif x >= 78:
          return  "B+"  
     elif x >= 74:
          return "B"
     elif x >= 70:
          return " B-"  
     elif x >= 66:  
          return  "C+"  
     elif x >= 62:
          return  "C"  
     elif x >= 58:
          return  "C-"  
     elif x >= 54:
          return  "D+"  
     elif x >= 50:
          return  "D"  
     else:
          return  "F"


#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
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

def calculate_sgpa(grade1, grade2 ,grade3):
     total_marks = 0 
     total_subject = 0
     if grade1 != "nothing":
          total_subject = total_subject + 1 
          total_marks = get_point(grade1) + total_marks
     if grade2 != "nothing":
          total_subject = total_subject + 1 
          total_marks = get_point(grade2) + total_marks 
     if grade3 != "nothing":
          total_subject = total_subject + 1 
          total_marks = get_point(grade3)  + total_marks 
     if total_subject == 0:
          return 0

     s_gpa = total_marks / total_subject 
     
     return s_gpa
#### End OF MARKER




if __name__ == '__main__':
    print (get_grade(89.50))
    print (calculate_sgpa('C-', 'D+', 'nothing'))
