class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        most_water = 0
        while left < right:
            breadth = right - left
            length = min(height[left],height[right])
            area = length * breadth
            most_water = max(most_water,area)
            if height[left] < height[right] :
                left+=1
            else:
                right-=1
        return most_water