"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10,001st prime number?"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def problem_7():
    too_short = True
    prime_list = []
    n = 1
    while too_short:
        
        if is_prime(n) == True: 
            prime_list.append(n)
            
        if len(prime_list) == 10001:
            too_short = False
            return prime_list[-1]
        n += 1        
print(problem_7())
         

