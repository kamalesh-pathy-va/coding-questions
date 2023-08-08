'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
'''

# I ended up writing the worst possible binary search algorithm


def search(nums, target):
    if target == nums[0]:
        return 0
    elif target == nums[len(nums) - 1]:
        return len(nums) - 1
    if len(nums) < 2:
        return -1
    if target > nums[0]:
        prev = nums[0]
        i = 1
        while prev < nums[i]:
            if target == nums[i]:
                return i
            prev = nums[i]
            i += 1
            if i == len(nums):
                break
        return -1
    elif target < nums[len(nums) - 1]:
        nex = nums[len(nums) - 1]
        i = len(nums) - 2
        while nex > nums[i]:
            if target == nums[i]:
                return i
            nex = nums[i]
            i -= 1
        return -1
    return -1


# Or can use builtin functions like this Which ended up being much more efficient
# def search(nums, target):
#     if target in nums:
#         return nums.index(target)
#     else:
#         return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
