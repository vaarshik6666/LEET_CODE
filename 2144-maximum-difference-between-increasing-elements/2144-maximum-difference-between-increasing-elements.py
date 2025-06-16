class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        element = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > element:
                result = max(result, nums[i] - element)
            element = min(element, nums[i])
        return result