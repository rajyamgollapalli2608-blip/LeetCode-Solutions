class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        # Find first and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i in range(n):
            x = ord(s[i]) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Try to create a valid substring starting at each character's first occurrence
        for i in range(n):
            x = ord(s[i]) - ord('a')

            if i != first[x]:
                continue

            l = i
            r = last[x]
            j = l
            valid = True

            while j <= r:
                y = ord(s[j]) - ord('a')

                # This character appeared before l,
                # so we cannot make a valid substring starting at l
                if first[y] < l:
                    valid = False
                    break

                r = max(r, last[y])
                j += 1

            if valid:
                intervals.append((l, r))

        # Choose maximum number of non-overlapping intervals.
        # If the number is same, shorter total length is preferred.
        intervals.sort(key=lambda x: (x[1], x[0]))

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans