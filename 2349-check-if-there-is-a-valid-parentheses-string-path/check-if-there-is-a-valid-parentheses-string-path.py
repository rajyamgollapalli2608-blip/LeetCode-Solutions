class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # First character must be '('
        if grid[0][0] == ')':
            return False

        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    dp[j].add(1)
                    continue

                current = set()

                # From top
                if i > 0:
                    current.update(dp[j])

                # From left
                if j > 0:
                    current.update(dp[j - 1])

                change = 1 if grid[i][j] == '(' else -1

                dp[j] = set()

                for balance in current:
                    new_balance = balance + change

                    if new_balance >= 0:
                        dp[j].add(new_balance)

        return 0 in dp[n - 1]