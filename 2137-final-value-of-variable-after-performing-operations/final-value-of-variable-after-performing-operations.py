class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for i in operations:
            if "-" in i:
                ans-=1
            if "+" in i:
                ans+=1
        return ans        