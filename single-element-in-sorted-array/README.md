# Single ELement in a Sorted Array

## Problem Statement

You're given a list of numbers where all the numbers are presented twice except one number that appears only once. Find this element that appears only one.
The solution must have a time complexity of O(log(n)) and space complexity of O(1).

## Example

- Input: [1, 1, 2, 3, 3, 4, 4, 6, 6]
  - Output: 2

- Input: [1, 1, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8]
  - Output: 6

## Explanation

[Single Element in Sorted Array - Michael Muinos](https://youtu.be/4Gi8uAz666s)

## Solution

- The approach follows a binary search technique as the solution must be O(log(n)).
- Check if the right side of the mid is even or not.
- If the mid and the left adjacent numbers are the same and the right is even, that means the target is on the left side. Thus point right to the mid-2. If the right is not even, that means the target is on the left side, point the left to mid + 1.
- If the mid and the right adjacent numbers are the same and the right is even, that means the target is on the right side. Thus, point the left to mid + 2. If the right is not even, the target is on the left side, point the right to mid - 1.
- If the nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1], that means, we have got our target, and that is nums[mid].
- If left is not less than right, and we have not found the target yet. Then, nums[left] is the target.
