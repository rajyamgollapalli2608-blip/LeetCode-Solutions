class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       n=len(nums)//2
       c=1
       nums.sort()
       for i in range(len(nums)-1):
          if nums[i]==nums[i+1]:
           c+=1 
          else:
            c=1
          if c>n:
            return nums[i]
       return nums[0]


         

        