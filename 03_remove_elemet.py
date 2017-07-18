"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        num = len(nums)
        for j in range(num):
            for i in range(len(nums)):
                if nums[i] == val:
                    del nums[i]
                    break
        
        return len(nums)

if __name__ == "__main__":
    solution = Solution()
    list_a = [3, 2, 2, 3]
    res = solution.removeElement(list_a, 3)
    print(res)
