class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        r=""
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_items=sorted(d.items(),key=lambda x:x[1],reverse=True)
        for i in sorted_items:
            r=r+i[0]*i[1]
        return r    



        