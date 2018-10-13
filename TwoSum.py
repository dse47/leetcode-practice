class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Brute force solution
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:],i+1):
                if num1 + num2 == target:
                    return i, j