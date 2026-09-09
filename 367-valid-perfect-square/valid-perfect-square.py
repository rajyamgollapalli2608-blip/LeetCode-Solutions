class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        h=num
        while l<=h:
            mid=(l+h)//2
            if mid*mid==num:
                return True
            if mid*mid>num:
                h=mid-1
            else:
                l=mid+1 
        return False           