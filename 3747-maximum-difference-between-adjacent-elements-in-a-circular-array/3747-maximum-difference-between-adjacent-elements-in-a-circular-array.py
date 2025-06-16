class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)-1):
            result = max(result, abs(nums[i] - nums[i+1]))
        result = max(result, abs(nums[-1] - nums[0]))
        return result