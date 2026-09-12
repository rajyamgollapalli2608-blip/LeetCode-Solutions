class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store original index
        arr = []
        for i in range(n):
            arr.append((intervals[i][0], intervals[i][1], intervals[i][2], i))

        # Sort by ending point
        arr.sort(key=lambda x: x[1])

        # Ending points
        ends = []
        for x in arr:
            ends.append(x[1])

        # prev[i] = number of intervals we can consider
        # before interval i without overlapping
        prev = []
        for i in range(n):
            start = arr[i][0]

            l = 0
            h = i

            while l < h:
                mid = (l + h) // 2

                if ends[mid] < start:
                    l = mid + 1
                else:
                    h = mid

            prev.append(l)

        # dp[k] = best answer using at most k intervals
        dp = [[(-1, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):

                # Don't take current interval
                best = dp[k][i - 1]

                # Take current interval
                start, end, value, index = arr[i - 1]

                old_score, old_indices = dp[k - 1][prev[i - 1]]

                new_score = old_score + value
                new_indices = tuple(sorted(old_indices + (index,)))

                if new_score > best[0]:
                    best = (new_score, new_indices)

                elif new_score == best[0]:
                    if new_indices < best[1]:
                        best = (new_score, new_indices)

                dp[k][i] = best

        return list(dp[4][n][1])