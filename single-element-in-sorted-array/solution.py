
def single_element(nums):
    left = 0
    right = len(nums) - 1

    while(left < right):
        mid = (left + right)//2
        right_is_even = (right - mid) % 2 == 0

        if nums[mid] == nums[mid-1]:
            if right_is_even:
                right = mid - 2
            else:
                left = mid + 1

        elif nums[mid] == nums[mid+1]:
            if right_is_even:
                left = mid + 2
            else:
                right = mid - 1

        else:
            return nums[mid]

    return nums[left]
