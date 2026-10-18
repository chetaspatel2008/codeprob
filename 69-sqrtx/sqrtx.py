class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        low=1
        high=x
        while low<=high:
            mid=(low+((high-low)/2))
            mid=int(mid)
            square=mid*mid
            if square==x: return mid
            if square>x:
                high=(mid)-1
            else:
                ans=int(mid)
                low=(mid)+1
        return ans
            
                
