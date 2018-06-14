# Find permutations of a given List
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (len(nums) == 0):
            return [[]]
        if (len(nums) == 1):
            return [nums]
        result = []
        i = 0
        while i < len(nums):
            temp = []
            if (i == 0):
                temp = self.permute(nums[1:])
            elif (i == len(nums) - 1):
                temp = self.permute(nums[:len(nums)-1])
            else:
                temp = self.permute(nums[:i] + nums[i+1:])
            result.extend([[nums[i]] + element for element in temp])
            i += 1
        return result
