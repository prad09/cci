
def URLify_comp(inp, inp_length):
    return ''.join('%20' if char == ' ' else char for char in inp[:inp_length])


def URLify_replace(inp, inp_length):
    return inp[:inp_length].replace(' ', '%20')

def URLify_check_Spaces_and_fill(inp_string, inp_length):
    inp = list(inp_string[:inp_length])
    result_length = len(inp_string)
    for i in range(result_length - inp_length):
        inp.append(' ')
    space_index_list = [index for index, char in enumerate(inp_string[:inp_length]) if char == ' ']
    index = result_length - 1
    while index >= 0:
        inp_length -= 1
        if inp_length in space_index_list:
            inp[index] = '0'
            inp[index - 1] = '2'
            inp[index - 2] = '%'
            index -= 2
        else:
            inp[index] = inp_string[inp_length]
        index -= 1
    return ''.join(inp)


def test():
    functions = [URLify_replace, URLify_comp, URLify_check_Spaces_and_fill]
    test_cases = [('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

    for fun in functions:
        for inp, length, out in test_cases:
            try:
                assert fun(inp, length) == out
            except AssertionError:
                print "test_failed"





if __name__ == "__main__":
    test()