class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = []
        n = len(nums)
        low = 0
        high = n-1
        first_occurence = -1
        last_occurence = -1

        while (low <= high):
            mid = (low + high) // 2

            if (nums[mid] == target):
                first_occurence = mid
                high = mid -1

            elif (nums[mid] < target):
                low = mid + 1
            
            else:
                high = mid - 1

        res.append(first_occurence)

        low = 0
        high = n-1

        while (low <= high):
            mid = (low + high) // 2

            if (nums[mid] == target):
                last_occurence = mid
                low = mid + 1

            elif (nums[mid] < target):
                low = mid + 1
            
            else:
                high = mid - 1

        res.append(last_occurence)
        return res
        