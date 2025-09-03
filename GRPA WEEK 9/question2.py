'''
GRPA 2 - Scalar Multiple Check - GRADED
Problem statement:
Implement the function `linear` which takes two lists of integers `P` and `Q` and an integer `k`,
and recursively determines if `P` is a scalar multiple of `Q` with scalar `k`.

Function Specification:
linear(P, Q, k):
    A recursive function to determine if one list is a scalar multiple of the other.

Arguments:
    P: list of integers
    Q: list of integers
    k: integer

Return:
    result: bool
'''

# Solution

def linear(P, Q, k):
    """
    A recursive function to determine if a list is a scalar multiple of another.

    Arguments:
    P: list of integers
    Q: list of integers
    k: integer

    Return:
    result: bool
    """
    if len(P) != len(Q):
        return False  # Lists must be of the same length

    if len(P) == 0:
        return True  # Both lists are empty, hence scalar multiples

    if P[0] != k * Q[0]:
        return False  # If any element doesn't match, return False

    return linear(P[1:], Q[1:], k)  # Recursively check the rest
