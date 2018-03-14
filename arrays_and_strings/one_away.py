
def one_away_bits(input_a, input_b):
    if abs(len(input_a) - len(input_b)) > 1:
        return False
    checker = 0
    long_str = ""
    max_length = max(len(input_a), len(input_b))
    if len(input_a) == max_length:
        long_str = input_a
    else:
        long_str = input_b
    for i in xrange(0, max_length):
        if i < len(input_a) and i < len(input_b):
            if ord('a') < ord(input_a[i]) < ord('z') and ord('a') < ord(input_b[i]) < ord('z'):
                index_a = ord(input_a[i]) - ord('a')
                index_b = ord(input_b[i]) - ord('a')
                mask_a, mask_b = 1 << index_a, 1 << index_b
                if mask_a != mask_b:
                    if checker & mask_a == 0:
                        checker |= mask_a
                    else:
                        checker &= ~mask_a
                    if checker & mask_b == 0:
                        checker |= mask_b
                    else:
                        checker &= ~mask_b
        else:
            if ord('a') < ord(long_str[i]) < ord('z'):
                index = ord(long_str[i]) - ord('a')
                mask = 1 << index
                if mask != mask:
                    if checker & mask == 0:
                        checker |= mask
                    else:
                        checker &= ~mask
    bin_count = bin(checker).count('1')
    if bin_count <= 2:
        return True
    else:
        return False

def one_away(input_a, input_b):
    len_diff = len(input_a) - len(input_b)
    if abs(len_diff) > 1:
        return False
    if len_diff == -1:
        input_a, input_b = input_b, input_a
    index_a = 0
    index_b = 0
    found_diff = False
    while index_a < len(input_a) and index_b < len(input_b):
        if input_a[index_a] != input_b[index_b]:
            if found_diff:
                return False
            found_diff = True
            if len_diff == 0:
                index_b += 1
        else:
            index_b += 1
        index_a += 1
    return True


def test():
    functions = [one_away_bits, one_away]
    test_cases = [("pale", "ple", True), ("pales", "pale", True), ("pale", "bale", True), ("pale", "bae", False)]
    for fun in functions:
        for inp_a, inp_b, out in test_cases:
            try:
                assert fun(inp_a, inp_b) == out
            except AssertionError:
                print inp_a, inp_b, "test_failed"

if __name__ == "__main__":
    test()