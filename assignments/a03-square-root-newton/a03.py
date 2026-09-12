## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def good_enough(guess, x):
    if abs(guess * guess - x ) < 0.1 :
        return True
    else :
        return False

    
def sqrt(x, guess = 0):
   if x == 0:
       return None
   if good_enough(guess, x):
        return guess
   else :
        new_guess = improve_guess(guess, x)
        return sqrt(x , new_guess)


#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(num1, num2):
    arithmetic_mean = (num1 + num2) / 2
    return arithmetic_mean

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(a, x):
    if a == 0:
       a = a + 1
    guess = average(a, x /a)
    return guess
    

#### End OF MARKER




if __name__ == '__main__':
    print (sqrt(36))
