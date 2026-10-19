class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        n1 = []
        for i in range(m):
            n1.append(nums1[i])

        n2 = []
        for j in range(n):
            n2.append(nums2[j])
        nums1[:] = n1 + n2
        nums1.sort()
        
        