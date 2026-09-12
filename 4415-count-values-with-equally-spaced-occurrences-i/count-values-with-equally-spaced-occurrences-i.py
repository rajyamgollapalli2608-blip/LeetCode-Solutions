class Solution:
    def countSpecialIntegers(self, nums: List[int]) -> int:
        pos = {}

        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)

        ans = 0

        for x in pos:
            if len(pos[x]) == 3:
                i1 = pos[x][0]
                i2 = pos[x][1]
                i3 = pos[x][2]

                if i2 - i1 == i3 - i2:
                    ans += 1

        return ans