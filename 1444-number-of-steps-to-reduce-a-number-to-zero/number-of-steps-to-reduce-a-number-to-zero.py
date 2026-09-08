class Solution:
    def numberOfSteps(self, num: int) -> int:
       c=0
       while num>0:
        if num%2==0:
            ans=num//2
            num=ans
            c+=1
        else:
            ans=num-1
            num=ans
            c+=1
       return c     