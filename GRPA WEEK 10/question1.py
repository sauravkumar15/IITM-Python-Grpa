'''
GRPA 1 - Recursive List Reverse - GRADED

Problem statement:
Implement the given function `reverse` which takes a list and returns a new list 
with the elements in reverse order using recursion.

Function Specification:
reverse(L):
    A recursive function to reverse a list L.

    Arguments:
    L: list; type of elements could be anything

    Return:
    result: list
'''

# Solution

def reverse(L):
    """
    A recursive function to reverse a list L

    Arguments:
    L: list; type of elements could be anything

    Return:
    result: list
    """
    if len(L) == 0:
        return []
    else:
        # Take last element + recursively reverse the rest
        return [L[-1]] + reverse(L[:-1])


# Example usage
print(reverse([1, 2, 3, 4]))   # Output: [4, 3, 2, 1]
print(reverse(['a', 'b', 'c'])) # Output: ['c', 'b', 'a']
