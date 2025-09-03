'''
GRPA 5 - Ancestry Finder - GRADED
Problem statement:
Implement the function `ancestry` which takes a dictionary of parent-child relationships
and recursively computes the sequence of ancestors from a given `present` person 
to a `past` person.

Function Specification:
ancestry(P, present, past):
    A recursive function to compute the sequence of ancestors of a person.

Arguments:
    P: dict, where keys and values are strings representing child → parent
    present: string (current person)
    past: string (target ancestor)

Return:
    result: list of strings (sequence of people from `present` to `past`)
'''

# Solution

def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of a person.

    Arguments:
    P: dict, keys and values are strings (child → parent)
    present: string
    past: string

    Return:
    result: list of strings
    """

    # Base case: if the current person is the target ancestor
    if present == past:
        return [present]

    # Base case: if the current person has no parent in P
    if present not in P:
        return []

    # Recursive case: find the parent's ancestry
    parent = P[present]
    ancestor_path = ancestry(P, parent, past)

    # If an ancestor path exists, prepend the current person
    if ancestor_path:
        return [present] + ancestor_path
    return []
