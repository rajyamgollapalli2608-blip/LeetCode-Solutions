class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=[]
        i=1
        while len(l)<k:
            if i not in arr:
                l.append(i)
            i+=1
        return l[k-1]

