## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(num):
    if num <= 1:
        return None
    num = int(num)    
    for i in range(2, num):
        if num % i == 0: 
            return False
            
    return True
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(num):
    num = int(num)
    for i in range(1 , num + 1):
        if num % i == 0 :
            print (i)
        
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(num):
    num = int(num)
    for i in range(num, 1, -1):
        if is_prime(i):
            return i  
    
    return None
#### End OF MARKER



if __name__ == '__main__':
    print (is_prime(19.01))  # should return True

    # print (get_largest_prime(10))  # should return 7
    # # print (get_largest_prime(100000) ) # bonus, try with 100k

    # output_factors(10)  # should output -- 1 2 5 10 -- one on each line
