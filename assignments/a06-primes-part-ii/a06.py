## IMPORTS GO HERE
import math
## END OF IMPORTS
def get_rounded_number(num):
    x = math.floor(num)
    x = num - x

    if x == 0:
        return num
    elif x < 0.5:
        return math.floor(num)
    else:
        return math.ceil(num)

    
def is_prime(num):
    if num <= 1:
        return None
    num = int(num)    
    for i in range(2, num):
        if num % i == 0: 
            return False
            
    return True

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###

def output_prime_factors(num):
    num = get_rounded_number(num)
    for i in range(1 , num + 1):
        if num % i == 0 :
            factors = i
            if is_prime(factors):
                print (factors)
    
#### End OF MARKER

### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(n):

    if n < 0:
        return None
    
    diff = n - int(n)
    if not diff == 0:
        return None
    
    last_prime = 0
    prime_founds = 0
    i = 0
    while prime_founds != n:

        if is_prime(i):
            prime_founds = prime_founds + 1
            last_prime = i
        i = i + 1

    return last_prime
#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(34)
    print(get_nth_prime(1.3))
