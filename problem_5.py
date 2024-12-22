"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10
 without any remainder. What is the smallest positive number that is evenly divisible by all 
 of the numbers from 1 to 20?"""

def problem_5():
    for i in range(2521, 999999999, 1):
        for k in range (1, 21, 1):
            if i % k != 0:
                break
            elif i % k == 0:
                continue
        if (k == 20) and (i % k == 0):
            return i

print(problem_5())
