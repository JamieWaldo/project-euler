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

def problem_3():
    """The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?"""
    factors = []
    number = 600851475143
    sqrt_number = int(600851475143 ** 0.5)
    

    for num in range(5, sqrt_number):
        if number % num == 0:
            if is_prime(num) == True:

                factors.append(num)

    return factors

print(problem_3())