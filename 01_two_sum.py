"""
TWO SUM
Given an array of integers, return indices of the
two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""


class Solution:

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        else:
            get_num = {}
            for i in range(len(nums)):
                if nums[i] in get_num:
                    return [get_num[nums[i]], i]
                else:
                    get_num[target - nums[i]] = i

if __name__ == "__main__":
    list_1 = [1, 3, 4, 5, 8]
    solu = Solution()
    solu.two_sum(list_1, 8)
