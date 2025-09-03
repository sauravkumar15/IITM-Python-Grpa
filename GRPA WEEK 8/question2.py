'''
GRPA 2 - File Relationship - GRADED
Problem statement:
Implement the given function `relation` where you have to determine the relationship between two files. 
The function should check if the files are exactly equal, if one file is a subset of the other, 
or if they have no relation.

Function Specification:
relation(file1, file2):
    Determine the relationship between two files.

    Arguments:
    file1, file2: strings, paths to two files
    
    Return:
    result: string; one of 'Equal', 'Subset', or 'No Relation'
'''

# Solution

def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
    file1, file2: strings, paths to two files

    Return:
    result: string; one of 'Equal', 'Subset', or 'No Relation'
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = [line.strip() for line in f1]
        lines2 = [line.strip() for line in f2]

    if lines1 == lines2:
        return "Equal"
    elif all(line in lines2 for line in lines1):
        return "Subset"
    else:
        return "No Relation"
