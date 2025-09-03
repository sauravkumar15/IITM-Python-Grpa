'''
GRPA 3 - Collatz Sequence Call Count - GRADED
Problem statement:
Implement the function `collatz` which takes a positive integer `n` (1 ≤ n ≤ 32,000) 
and recursively computes the number of calls needed to reach 1 
following the Collatz sequence rules.

Collatz Rules:
- If n is 1: stop (base case)
- If n is even: next term is n / 2
- If n is odd: next term is 3 * n + 1

Function Specification:
collatz(n):
    A recursive function to compute the number of calls to reach 1.

Arguments:
    n: integer (1 ≤ n ≤ 32,000)

Return:
    result: integer
'''

# Solution

def collatz(n):
    """
    A recursive function to compute the number of calls to reach 1 
    following the Collatz sequence rules.

    Arguments:
    n: integer (1 ≤ n ≤ 32,000)

    Return:
    result: integer
    """
    if n == 1:
        return 0  # Base case: no more calls if n is 1

    if n % 2 == 0:
        return 1 + collatz(n // 2)  # n is even: divide by 2
    else:
        return 1 + collatz(3 * n + 1)  # n is odd: multiply by 3 and add 1
