
def palindrome_permutation(input_str):
    # input_str = input_str.replace(" ", "")
    # input_str = input_str.decode('utf-8').lower()

    checker = 0
    for char in input_str:
        if ord('a') < ord(char) < ord('z'):
            index = ord(char) - ord('a')
        elif ord('A') < ord(char) < ord('Z'):
            index = (ord(char) - ord('A'))
        mask = (1 << index)
        if checker & mask == 0:
            checker |= mask
        else:
            checker &= ~mask
    if checker == 0 or (checker & (checker - 1) == 0):
        return True
    else:
        return False



def test():
    functions = [palindrome_permutation]
    test_cases = [("Tact Coa", True), ("geeksogeeks", True), ("who am I", False)]
    for fun in functions:
        for inp, out in test_cases:
            try:
                assert fun(inp) == out
            except AssertionError:
                print "test_failed"


if __name__ == "__main__":
    test()