CHAR_SIZE = 256
# unique characters
def unique_chars_set(input_string):
    assert all('a' <= char <= 'z' for char in input_string)
    if len(input_string) > ((ord('z') - ord('a')) + 1):
        return False
    chars_set = set()
    for char in input_string:
        if char in chars_set:
            return False
        chars_set.add(char)
    return True

def unique_chars_set_short(input_string):
    if len(set(input_string)) == len(input_string):
        return True
    else:
        return False
def unique_chars_sort(input_string):
    assert all('a' <= char <= 'z' for char in input_string)
    if len(input_string) > (ord('z')- ord('a')) + 1:
        return False
    input_sorted = sorted(input_string)
    prev_char = None
    for char in input_sorted:
        if char == prev_char:
            return False
        prev_char = char
    return True

def unique_chars_list(input_string):
    assert all('a' <= char <= 'z' for char in input_string)
    if len(input_string) > (ord('z') - ord('a')) + 1:
        return False
    char_list = [False] * CHAR_SIZE
    for char in input_string:
        ind = ord(char)
        if char_list[ind]:
            return False
        else:
            char_list[ind] = True
    return True

def unique_chars_bit(input_string):
    assert all('a' <= char <= 'z' for char in input_string)
    if len(input_string) > (ord('z') - ord('a')) + 1:
        return False
    checker = 0
    for char in input_string:
        index = ord(char) - ord('a')
        if(checker & (1 << index)) > 0:
            return False
        else:
            checker |= (1 << index)
    return True

def test():
    functions = [unique_chars_set, unique_chars_set_short, unique_chars_sort, unique_chars_list, unique_chars_bit]
    test_cases = [('hello', False), ('azerty', True)]

    for fun in functions:
        for arg, ret in test_cases:
            try:
                assert fun(arg) == ret
            except AssertionError:
                print "test_failed"


if __name__ == "__main__":
    test()
