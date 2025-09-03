'''
GRPA 3 - Goals by Country - GRADED
Problem statement:
Implement the given function `get_goals` where you have to read data from a file and 
calculate the number of players from a specified country and their total cumulative goals.

Function Specification:
get_goals(filename, country):
    Get the count of players and their cumulative goals for this country.

    Arguments:
    filename: string
    country: string

    Return:
    result: tuple; (integer, integer) 
            → First element: number of players from the country
            → Second element: total goals scored by those players
'''

# Solution

def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
    filename: string
    country: string

    Return:
    result: tuple; (integer, integer)
    """
    P_count = 0
    G_count = 0
    with open(filename) as fh:
        info_list = fh.readlines()
        for i in info_list:
            if country in i:
                P_count += 1
                test = i.split(",")
                G_count += int(test[2])
    return (P_count, G_count)
