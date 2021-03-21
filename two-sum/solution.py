def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # A dictionary to keep track of the seen numbers and their indices.
    seen = dict()

    for i, num in enumerate(nums):
        num_to_find = target - num

        # If the num_to_find is present in seen, we have found 2 numbers.
        # Return [index of the num_to_find, index of the num]
        if num_to_find in seen:
            return [seen[num_to_find], i]

        # Else, insert the number in the dictionary, with the index number.
        else:
            seen[num] = i

    # If no solution is found return None.
    return None


if __name__ == '__main__':
    test_set = [
        ([2, 6, 9, 8, 1, 2, 4], 10, [0, 3]),
        ([5, 6, 9, 8, 5, 2, 1], 7, [4, 5]),
        ([-5, -5, -9, 0, 5, 6, 9, 2], 0, [1, 4]),
        ([5, 2, 3, 8, 9, 4, 5, 6], 200, None)
    ]

    for nums, target, output in test_set:
        assert output == two_sum(nums, target), f'Output must be {output}'
    print("Test passed.")
