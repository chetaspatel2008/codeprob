class Solution:
    def search(self, nums: list[int], target: int) -> int:
    
        for i in range(len(nums)):
            if target not in nums:
                return -1
            elif nums[i] == target:
                return nums.index(nums[i])