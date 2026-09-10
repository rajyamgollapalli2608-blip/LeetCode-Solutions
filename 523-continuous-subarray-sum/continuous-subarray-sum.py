class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r_map = {0: -1}
        pref = 0

        for i, num in enumerate(nums):
            pref += num
            rem = pref % k

            if rem in r_map:
                index = i - r_map[rem]

                if index >= 2:
                    return True
            else:
                r_map[rem] = i

        return False