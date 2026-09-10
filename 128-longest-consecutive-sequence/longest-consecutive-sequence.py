class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lon=0
        cur=0
        nums=set(nums)
        for i in nums:
            if i-1 not in nums:
                cur=i
                len=1
                while cur+1 in nums:
                    len+=1
                    cur+=1
                lon=max(lon,len)        
        return lon        