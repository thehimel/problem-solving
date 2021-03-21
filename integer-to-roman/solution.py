def roman(num):
    """
    Function to convert an integer to roman numeral.

    :type num: int
    :rtype: str
    """

    if type(num) is not int:
        raise TypeError("Invalid input.")

    if num <= 0:
        raise ValueError("Roman numbers can only be positive. " +
                         "Please enter a positive integer.")

    # Define a list with tuples as integer and roman equivalent
    value_symbol = [
        (1000, 'M'), (900, 'CM'), (500, 'D'),
        (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    # Define the result as a blank string
    result = ''

    # Go from larger to smaller value
    for value, symbol in value_symbol:

        # Divide the number by the integer value.
        count = num//value

        # If the division is greater than zero.
        if count > 0:
            # Add that many symbol(s) with the result.
            # Here '*' is not multiplication. 'M' * 3 = 'MMM'.
            result += symbol * count

        num %= value

    # Return the result
    return result
