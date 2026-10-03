class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        summ=0
        for ch in operations:
            if ch=="C":
                stack.pop()
            elif ch=="D":
                stack.append(stack[-1]*2)
            elif ch=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(ch))  
        for i in stack:
            summ+=i       
        return summ