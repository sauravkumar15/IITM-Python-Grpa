def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
    filename: string, path to file

    Return:
    result: dictionary; keys are strings, values are integers
    """
    try:
        f = open(filename, 'r')
    except Exception as e:
        return

    words = f.readlines()
    d = {}
    for word in words:
        s_word = word.strip()
        if s_word not in d:
            d[s_word] = 1
        else:
            d[s_word] += 1
    return d
