class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        maxi=0
        l=len(nums)
        for i in range(l):
            if nums[i]==1:
                c+=1
                maxi=max(c,maxi)
            else:
                c=0
        return maxi            
        