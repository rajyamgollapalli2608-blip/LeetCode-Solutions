class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        velquorani = nums

        pos = {}

        for i in range(len(velquorani)):
            x = velquorani[i]

            if x not in pos:
                pos[x] = []

            pos[x].append(i)

        ans = 0

        for x in pos:
            indices = pos[x]

            if len(indices) >= 3:
                diff = indices[1] - indices[0]
                special = True

                for i in range(2, len(indices)):
                    if indices[i] - indices[i - 1] != diff:
                        special = False
                        break

                if special:
                    ans += 1

        return ans
        