'''
GRPA 1 - Parsing Inputs - GRADED
Problem statement:
Implement the given function `get_freq` where you have to read the input from the standard input 
with the input format given in the docstring of the function and return the output in the required type.

Function Specification:
get_freq(filename):
    Extract frequency information from the file

    Argument:
    filename: string, path to file

    Return:
    result: dictionary; keys are strings, values are integers
'''

# Solution

def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
    filename: string, path to file

    Return:
    result: dictionary; keys are strings, values are integers
    """
    try:
        with open(filename, 'r') as f:
            words = f.readlines()
    except Exception as e:
        return None

    d = {}
    for word in words:
        s_word = word.strip()
        if s_word not in d:
            d[s_word] = 1
        else:
            d[s_word] += 1
    return d
