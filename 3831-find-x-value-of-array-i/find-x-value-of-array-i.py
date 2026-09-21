class Solution:
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Subarray containing only num
            r = num % k
            new_dp[r] += 1

            # Extend previous subarrays
            for old_r in range(k):
                new_r = (old_r * r) % k
                new_dp[new_r] += dp[old_r]

            # Add counts
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result