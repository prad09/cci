import collections

CHAR_SIZE = 256
def check_permutations_sort(input_a, input_b):
    if len(input_a) != len(input_b):
        return False
    return sorted(input_a) == sorted(input_b)

def check_permutation_dict(input_a, input_b):
    if len(input_a) != len(input_b):
        return False
    d = collections.defaultdict(int)
    for char in input_a:
        d[char] += 1
    for char in input_b:
        d[char] -= 1
    return not any(d.itervalues())

def check_permutation_list(input_a, input_b):
    if len(input_a) != len(input_b):
        return False
    char_count = [0] * CHAR_SIZE
    for char in input_a:
        char_count[ord(char)] += 1
    for char in input_b:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False
    return True

def test():
    functions = [check_permutations_sort, check_permutation_dict, check_permutation_list]
    test_cases = [("god", "dog", True), ("god", "dag", False )]
    for fun in functions:
        for inp_a, inp_b, out in test_cases:
            try:
                assert fun(inp_a, inp_b) == out
            except AssertionError:
                print "test_failed"


if __name__ == "__main__":
    test()
