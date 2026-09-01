class Solution:
    def isHappy(self, n: int) -> bool:
     seen=set()
     while n!=1:
        if n in seen:
            return False
        seen.add(n)    
        summ=0
        while n>0:
            r=n%10
            summ=summ+r*r
            n=n//10
        n=summ   
     return True    
          
        