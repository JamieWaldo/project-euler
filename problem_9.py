"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which 
a + b + c = 1000.
Find the product abc."""
total = 1000
def problem_9():
    for a in range(total // 3):
        for b in range(total // 2):
            c = total - (a + b)
            if (a*a) + (b*b) == (c*c):
                return a, b, c, a * b * c
            
print(problem_9())
