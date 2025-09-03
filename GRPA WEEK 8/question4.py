'''
GRPA 4 - Matrix to Words - GRADED
Problem statement:
Implement the given function `num_to_words` where you have to take a matrix (list of lists) of digits 
and write it into a file named "words.csv". Each digit in the matrix should be converted into its 
corresponding word. Rows of the matrix should be written on separate lines, with words separated by commas.

Function Specification:
num_to_words(mat):
    Convert a matrix of numbers into their word representations and save to "words.csv".

    Arguments:
    mat: list of lists (matrix of integers from 0 to 9)

    Return:
    None
'''

# Solution

def num_to_words(mat):
    """
    Convert matrix to file

    Argument:
    mat: list of lists

    Return:
    None
    """
    d = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    f = open("words.csv", "w")
    n = len(mat)
    for i in range(n):
        for j in range(n):
            line = f"{d[mat[i][j]]}"
            if j != n - 1:
                line += ","
            f.write(line)
        if i != n - 1:
            f.write("\n")
    f.close()
