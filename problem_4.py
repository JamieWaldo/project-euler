def check_palindrome(potential_palindrome):
    digits = [int(digit) for digit in str(potential_palindrome)]
    digits_reversed = [int(digit) for digit in reversed(str(potential_palindrome))]
    if digits == digits_reversed:
        return True
    else:
        return False


def problem_4():
    """A palindromic number reads the same both ways. The largest palindrome made from the 
    product of two 2-digit numbers is 9009 = 91 times 99.
    Find the largest palindrome made from the product of two 3-digit numbers."""
    palindrome_list = []
    for num in range(999, 99, -1):
        for numb in range(999, 99, -1):
            potential_palindrome = numb * num
            if check_palindrome(potential_palindrome) == True: 
                palindrome_list.append(potential_palindrome)
            else: 
                continue
    
    
    highest = 0
    for i in palindrome_list:
        if i > highest:
            highest = i
    
    return highest

print(problem_4())