class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        # 1,000 to 999,999 → 1 comma
        if n >= 1000:
            count = min(n, 999999) - 1000 + 1
            ans += count * 1

        # 1,000,000 to 999,999,999 → 2 commas
        if n >= 1000000:
            count = min(n, 999999999) - 1000000 + 1
            ans += count * 2

        # 1,000,000,000 to 999,999,999,999 → 3 commas
        if n >= 1000000000:
            count = min(n, 999999999999) - 1000000000 + 1
            ans += count * 3

        # 1,000,000,000,000 to 999,999,999,999,999 → 4 commas
        if n >= 1000000000000:
            count = min(n, 999999999999999) - 1000000000000 + 1
            ans += count * 4

        # 1,000,000,000,000,000 → 5 commas
        if n >= 1000000000000000:
            count = n - 1000000000000000 + 1
            ans += count * 5

        return ans