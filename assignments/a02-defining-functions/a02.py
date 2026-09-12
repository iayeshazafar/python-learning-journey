## IMPORTS GO HERE
import math
from math import pi
## END OF IMPORTS 


#### YOUR CODE FOR get_area GOES HERE ####
def get_area(radius):
    area = pi * pow(radius, 2)
    return area
#### End OF MARKER


#### YOUR CODE FOR output_parameter GOES HERE ####
def output_parameter(radius):
    parameter = 2 * pi * radius
    print("The parameter of the circle with radius",radius, "is",parameter)
    return parameter
#### End OF MARKER  




if __name__ == '__main__': 
    print (get_area(1))
    output_parameter(10) 

