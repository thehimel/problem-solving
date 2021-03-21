def integer(roman):
    # Initialize a dictionary of symbol and values
    symbol_value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    second_last_index = len(roman) - 1
    result = 0

    # Now traverse the roman string from index 0 to the second last index.
    # Compare value of the present symbol with the value of the next symbol.
    # If the present value is smaller than the next value, reduce the
    # present value from the result. Else add it with the result.

    for i in range(second_last_index):
        present_value = symbol_value[roman[i]]
        next_value = symbol_value[roman[i+1]]

        if present_value < next_value:
            result -= present_value
        else:
            result += present_value

    # At last, add the value of the last symbol.
    result += symbol_value[roman[-1]]

    return result


if __name__ == '__main__':
    test_set = [
        ('XLV', 45),
        ('MMMMMCMXCV', 5995),
        ('XCV', 95),
        ('DCCC', 800),
        ('CDLXXXII', 482),
    ]

    for roman, output in test_set:
        assert output == integer(roman)

    print('Test Passed.')
