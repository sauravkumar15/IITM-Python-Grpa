'''
GRPA 4 - Ways to Ascend Steps - GRADED
Problem statement:
Implement the function `steps` which takes a positive integer `n` 
and recursively computes the number of ways to climb `n` steps 
if at a time you can climb 1, 2, or 3 steps.

Function Specification:
steps(n):
    A recursive function to calculate the number of ways 
    to ascend `n` steps using steps of size 1, 2, or 3.

Arguments:
    n: integer (number of steps)

Return:
    result: integer
'''

# Solution

def steps(n):
    """
    A recursive function to compute the number of ways to ascend `n` steps.

    Arguments:
    n: integer

    Return:
    result: integer
    """
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    # Recursive cases
    return steps(n - 1) + steps(n - 2) + steps(n - 3)
