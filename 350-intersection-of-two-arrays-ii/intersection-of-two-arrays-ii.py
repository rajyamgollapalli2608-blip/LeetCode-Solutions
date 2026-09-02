class Solution:
 def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    d={}
    ans=[]
    for i in nums1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1    
    for i in nums2:
        if i in d and d[i]>=1:
            ans.append(i)
            d[i]-=1
    return ans        
