class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = float('inf')
        b = float('inf')
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                a = abs(sum-target)
                
                if a < b:
                    b = a
                    n = sum
                if sum < target:
                    j += 1
                else:
                    k -= 1
        return n
                